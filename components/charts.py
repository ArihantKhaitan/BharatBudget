"""Reusable Plotly chart functions for BharatBudget."""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

from utils.styling import (
    get_plotly_layout, MINISTRY_COLOR_MAP,
    ORANGE, TEAL, RED, BLUE_SOFT, TEXT_MUTED, NAVY_LIGHT,
    PLOTLY_PAPER_BG, PLOTLY_PLOT_BG, TEXT_MAIN, NAVY_CARD,
)


def fmt_lcr(val: float) -> str:
    """Format a Lakh Crore value: '₹3.18 L cr'"""
    if val is None:
        return "N/A"
    return f"₹{val:.2f} L cr"


def treemap_chart(year_data: dict, value_key: str = "allocated", title: str = "") -> go.Figure:
    """Ministry-wise treemap for a single year."""
    ministries, values, colors = [], [], []
    for ministry, data in year_data.items():
        val = data.get(value_key)
        if val is not None and val > 0:
            ministries.append(ministry)
            values.append(val)
            colors.append(MINISTRY_COLOR_MAP.get(ministry, "#546E7A"))

    fig = go.Figure(go.Treemap(
        labels=ministries,
        parents=[""] * len(ministries),
        values=values,
        marker=dict(colors=colors, line=dict(width=1.5, color="#0B1437")),
        textinfo="label+percent root",
        textfont=dict(size=12, color="#ffffff"),
        hovertemplate="<b>%{label}</b><br>Allocation: ₹%{value:.2f} L cr<br>Share: %{percentRoot:.1%}<extra></extra>",
        pathbar=dict(visible=False),
    ))
    layout = get_plotly_layout(title, height=460)
    layout.pop("xaxis", None)
    layout.pop("yaxis", None)
    fig.update_layout(**layout)
    return fig


def bar_top10(year_data: dict, value_key: str = "allocated",
              title: str = "", total: float = None) -> go.Figure:
    """Horizontal bar chart — top 10 ministries."""
    items = [
        (m, d.get(value_key, 0) or 0)
        for m, d in year_data.items()
        if d.get(value_key) is not None
    ]
    items.sort(key=lambda x: x[1], reverse=True)
    items = items[:10]
    items.reverse()  # largest at top after orientation='h'

    names = [i[0] for i in items]
    vals  = [i[1] for i in items]
    clrs  = [MINISTRY_COLOR_MAP.get(n, ORANGE) for n in names]
    pcts  = [f"{v/total*100:.1f}%" if total else "" for v in vals]

    fig = go.Figure(go.Bar(
        x=vals, y=names, orientation="h",
        marker=dict(color=clrs, line=dict(width=0)),
        text=[f"{fmt_lcr(v)}  {p}" for v, p in zip(vals, pcts)],
        textposition="outside",
        textfont=dict(color=TEXT_MUTED, size=11),
        hovertemplate="<b>%{y}</b><br>%{x:.2f} L cr<extra></extra>",
    ))
    layout = get_plotly_layout(title, height=400)
    layout["xaxis"]["title"] = "₹ Lakh Crore"
    layout["margin"]["r"] = 100
    fig.update_layout(**layout)
    fig.update_yaxes(tickfont=dict(size=11))
    return fig


def multiline_chart(df: pd.DataFrame, x_col: str, y_cols: list,
                    title: str = "", y_label: str = "₹ Lakh Crore",
                    color_map: dict = None) -> go.Figure:
    """Multi-series line chart for trend comparison."""
    fig = go.Figure()
    palette = [ORANGE, TEAL, RED, BLUE_SOFT, "#CE93D8", "#FFF176",
               "#80CBC4", "#F48FB1", "#A5D6A7"]
    for i, col in enumerate(y_cols):
        if col not in df.columns:
            continue
        clr = (color_map or {}).get(col, palette[i % len(palette)])
        fig.add_trace(go.Scatter(
            x=df[x_col], y=df[col], name=col, mode="lines+markers",
            line=dict(color=clr, width=2.5),
            marker=dict(size=7, color=clr),
            hovertemplate=f"<b>{col}</b><br>%{{x}}: %{{y:.2f}}<extra></extra>",
        ))
    layout = get_plotly_layout(title, height=400)
    layout["yaxis"]["title"] = y_label
    layout["legend"]["orientation"] = "h"
    layout["legend"]["y"] = -0.2
    fig.update_layout(**layout)
    return fig


def yoy_bar(df: pd.DataFrame, ministry: str, title: str = "") -> go.Figure:
    """Year-on-year % change bar chart for a single ministry."""
    vals = df["allocated"].pct_change() * 100
    colors = [TEAL if v >= 0 else RED for v in vals]

    fig = go.Figure(go.Bar(
        x=df["year"], y=vals,
        marker=dict(color=colors),
        text=[f"{v:+.1f}%" if not pd.isna(v) else "" for v in vals],
        textposition="outside",
        textfont=dict(color=TEXT_MUTED, size=11),
        hovertemplate="%{x}: %{y:+.1f}%<extra></extra>",
    ))
    layout = get_plotly_layout(title or f"{ministry} — Year-on-Year % Change", height=320)
    layout["yaxis"]["title"] = "% Change"
    layout["yaxis"]["zeroline"] = True
    layout["yaxis"]["zerolinecolor"] = NAVY_LIGHT
    fig.update_layout(**layout)
    return fig


def scatter_correlation(x_vals: list, y_vals: list, labels: list,
                        x_label: str, y_label: str, title: str = "",
                        trendline: bool = True) -> go.Figure:
    """Scatter plot with optional linear trendline."""
    fig = go.Figure()

    # Scatter points
    fig.add_trace(go.Scatter(
        x=x_vals, y=y_vals,
        mode="markers+text",
        text=labels,
        textposition="top center",
        textfont=dict(size=10, color=TEXT_MUTED),
        marker=dict(
            size=10, color=x_vals,
            colorscale=[[0, NAVY_LIGHT], [1, ORANGE]],
            showscale=True,
            colorbar=dict(
                title=dict(text=x_label, font=dict(color=TEXT_MUTED, size=10)),
                tickfont=dict(color=TEXT_MUTED, size=9),
            ),
            line=dict(width=1, color=TEXT_MAIN),
        ),
        hovertemplate=f"<b>%{{text}}</b><br>{x_label}: %{{x:.2f}}<br>{y_label}: %{{y:.2f}}<extra></extra>",
    ))

    # Trendline
    if trendline and len(x_vals) >= 3:
        x_arr = np.array(x_vals, dtype=float)
        y_arr = np.array(y_vals, dtype=float)
        mask  = ~np.isnan(x_arr) & ~np.isnan(y_arr)
        if mask.sum() >= 2:
            m, b = np.polyfit(x_arr[mask], y_arr[mask], 1)
            xs = np.linspace(x_arr[mask].min(), x_arr[mask].max(), 100)
            fig.add_trace(go.Scatter(
                x=xs, y=m * xs + b,
                mode="lines",
                name="Trend",
                line=dict(dash="dot", color=TEAL, width=1.5),
                hoverinfo="skip",
            ))

    layout = get_plotly_layout(title, height=380)
    layout["xaxis"]["title"] = x_label
    layout["yaxis"]["title"] = y_label
    fig.update_layout(**layout)
    return fig


def bubble_map_india(state_df: pd.DataFrame, value_col: str,
                     label_col: str = "state",
                     title: str = "State-wise Central Allocation") -> go.Figure:
    """Scatter-geo bubble map centred on India."""
    max_val = state_df[value_col].max()

    fig = go.Figure(go.Scattergeo(
        lon=state_df["lon"],
        lat=state_df["lat"],
        text=state_df[label_col],
        customdata=state_df[[value_col]],
        mode="markers",
        marker=dict(
            size=state_df[value_col] / max_val * 55 + 6,
            color=state_df[value_col],
            colorscale=[[0, "#1E3A5F"], [0.4, "#FF9933"], [1.0, "#E84040"]],
            showscale=True,
            colorbar=dict(
                title=dict(text="₹ per capita", font=dict(color=TEXT_MUTED, size=10)),
                tickfont=dict(color=TEXT_MUTED, size=9),
                bgcolor=PLOTLY_PAPER_BG,
            ),
            opacity=0.85,
            line=dict(width=1, color="#fff"),
        ),
        hovertemplate="<b>%{text}</b><br>₹%{customdata[0]:,.0f} per capita<extra></extra>",
    ))

    fig.update_geos(
        scope="asia",
        center=dict(lat=22.5, lon=82.5),
        projection_scale=4.8,
        showcoastlines=True,
        coastlinecolor=NAVY_LIGHT,
        showland=True, landcolor="#131E3A",
        showocean=True, oceancolor="#0B1437",
        showlakes=True, lakecolor="#0B1437",
        showrivers=False,
        showcountries=True, countrycolor=NAVY_LIGHT,
        bgcolor=PLOTLY_PAPER_BG,
    )

    layout = get_plotly_layout(title, height=520)
    layout.pop("xaxis", None)
    layout.pop("yaxis", None)
    layout["geo"] = dict(bgcolor=PLOTLY_PAPER_BG)
    fig.update_layout(**layout)
    return fig


def donut_chart(labels: list, values: list, title: str = "") -> go.Figure:
    """Donut chart for category breakdown."""
    colors = [MINISTRY_COLOR_MAP.get(l, ORANGE) for l in labels]
    fig = go.Figure(go.Pie(
        labels=labels, values=values,
        hole=0.55,
        marker=dict(colors=colors, line=dict(width=1.5, color="#0B1437")),
        textinfo="percent",
        textfont=dict(color=TEXT_MAIN, size=11),
        hovertemplate="<b>%{label}</b><br>₹%{value:.2f} L cr (%{percent})<extra></extra>",
    ))
    layout = get_plotly_layout(title, height=380)
    layout.pop("xaxis", None)
    layout.pop("yaxis", None)
    layout["legend"]["orientation"] = "v"
    layout["legend"]["x"] = 1.0
    fig.update_layout(**layout)
    return fig


def gauge_chart(value: float, reference: float, title: str,
                suffix: str = " L cr") -> go.Figure:
    """Bullet/gauge for current vs previous year."""
    fig = go.Figure(go.Indicator(
        mode="number+delta",
        value=value,
        delta=dict(reference=reference, relative=True,
                   increasing=dict(color=TEAL),
                   decreasing=dict(color=RED),
                   valueformat=".1%"),
        number=dict(prefix="₹", suffix=suffix,
                    font=dict(color=TEXT_MAIN, size=30)),
        title=dict(text=title, font=dict(color=TEXT_MUTED, size=13)),
    ))
    fig.update_layout(
        paper_bgcolor=PLOTLY_PAPER_BG,
        height=140,
        margin=dict(l=10, r=10, t=10, b=10),
    )
    return fig
