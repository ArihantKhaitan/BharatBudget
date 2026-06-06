"""Constituency Funds — How much does your MP spend in your area?"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from utils.styling import (
    footer_html, insight_box, page_header,
    ORANGE, ORANGE_LIGHT, TEAL, RED, BLUE_SOFT, TEXT_PRIMARY, TEXT_SEC, TEXT_MUTED,
    BORDER, GRID_COLOR, PLOTLY_PAPER, PLOTLY_PLOT, BG_SURFACE, BG_ELEVATED,
)
from data.constituencies import (
    MPLADS_TOTAL_ALLOCATION_CR, STATE_MPLADS_UTILIZATION_2023_24,
    STATE_MPLADS_ALLOCATION_2023_24, MPLADS_WORK_CATEGORY_PCT,
    TOP_DEVELOPED_CONSTITUENCIES, LEAST_DEVELOPED_CONSTITUENCIES,
    LS_SEATS_PER_STATE,
)

st.markdown(
    page_header(
        "🗳️",
        "Constituency Funds",
        "Every MP gets ₹5 crore/year for local development. Explore state-wise MPLADS allocations, fund utilization, and constituency development indices.",
    ),
    unsafe_allow_html=True,
)
st.markdown("---")

# ── Page controls (inline) ────────────────────────────────────────────────────
view = st.radio(
    "View",
    ["State-wise Allocation", "Utilization Rates", "Work Categories", "Development Index"],
    horizontal=True,
)

# ── Top metrics ───────────────────────────────────────────────────────────────
total_mps = sum(LS_SEATS_PER_STATE.values())
total_alloc_2023 = MPLADS_TOTAL_ALLOCATION_CR["2023-24"]
top_util_state = max(STATE_MPLADS_UTILIZATION_2023_24, key=STATE_MPLADS_UTILIZATION_2023_24.get)
bot_util_state = min(STATE_MPLADS_UTILIZATION_2023_24, key=STATE_MPLADS_UTILIZATION_2023_24.get)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("MPLADS Annual Budget", f"₹{total_alloc_2023} cr",
              f"₹5 cr × {total_mps} Lok Sabha MPs")
with c2:
    st.metric("Per Constituency", "₹5 crore / year",
              "= ₹41.7 lakh / month")
with c3:
    st.metric("Best Utilization", f"{top_util_state}",
              f"{STATE_MPLADS_UTILIZATION_2023_24[top_util_state]:.1f}% utilized")
with c4:
    st.metric("Lowest Utilization", f"{bot_util_state}",
              f"{STATE_MPLADS_UTILIZATION_2023_24[bot_util_state]:.1f}% utilized")

st.markdown("<br>", unsafe_allow_html=True)

# ── MPLADS trend ──────────────────────────────────────────────────────────────
st.markdown(
    f"<div class='section-label'>📈 &nbsp; MPLADS Annual Allocation Trend</div>",
    unsafe_allow_html=True,
)
years = list(MPLADS_TOTAL_ALLOCATION_CR.keys())
vals  = list(MPLADS_TOTAL_ALLOCATION_CR.values())
colors_mplads = [RED if v == 0 else ORANGE for v in vals]

fig_trend = go.Figure(go.Bar(
    x=years, y=vals,
    marker_color=colors_mplads,
    text=[("SUSPENDED" if v == 0 else f"₹{v} cr") for v in vals],
    textposition="outside",
    textfont=dict(color=[RED if v == 0 else TEXT_MUTED for v in vals], size=9),
    hovertemplate="%{x}: ₹%{y} cr<extra></extra>",
))
fig_trend.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=260,
    margin=dict(l=8, r=8, t=12, b=8),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="₹ Crore", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
)
st.plotly_chart(fig_trend, use_container_width=True)
st.markdown(insight_box(
    "MPLADS was <b>suspended for 2 years (2020-21 & 2021-22)</b> and funds diverted to PM CARES during COVID-19. "
    "MPs and opposition parties protested this decision as it affected local development. "
    "The scheme resumed in 2022-23 with the standard ₹5 cr/MP allocation."
), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if view == "State-wise Allocation":
    st.markdown(
        f"<div class='section-label'>🗺️ &nbsp; State-wise MPLADS Allocation (FY 2023-24)</div>",
        unsafe_allow_html=True,
    )
    sorted_states = sorted(STATE_MPLADS_ALLOCATION_2023_24.items(), key=lambda x: x[1], reverse=True)
    df_s = pd.DataFrame(sorted_states, columns=["State", "Allocation (₹ cr)"])
    df_s["LS Seats"] = df_s["State"].map(LS_SEATS_PER_STATE).fillna(0).astype(int)
    df_s["Per Seat (₹ cr)"] = 5

    fig_alloc = go.Figure(go.Bar(
        x=df_s["Allocation (₹ cr)"], y=df_s["State"], orientation="h",
        marker=dict(
            color=df_s["Allocation (₹ cr)"],
            colorscale=[[0, BG_ELEVATED], [0.5, ORANGE_LIGHT], [1, ORANGE]],
        ),
        text=[f"₹{v} cr ({s} MPs)" for v, s in zip(df_s["Allocation (₹ cr)"], df_s["LS Seats"])],
        textposition="outside",
        textfont=dict(color=TEXT_MUTED, size=9),
        hovertemplate="%{y}: ₹%{x} cr<extra></extra>",
    ))
    fig_alloc.update_layout(
        paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
        height=580,
        margin=dict(l=8, r=120, t=8, b=8),
        xaxis=dict(title=dict(text="₹ Crore", font=dict(color=TEXT_SEC)),
                   gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
        yaxis=dict(gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    )
    st.plotly_chart(fig_alloc, use_container_width=True)
    st.markdown(insight_box(
        "<b>UP gets the most MPLADS money (₹400 cr/yr)</b> simply because it has 80 Lok Sabha seats — "
        "the most of any state. But on a <b>per-capita basis</b>, smaller states and UTs "
        "(like Goa, Sikkim) get far more per person. "
        "Note: Rajya Sabha MPs also get ₹5 cr each, allocated across states proportionally."
    ), unsafe_allow_html=True)

elif view == "Utilization Rates":
    st.markdown(
        f"<div class='section-label'>⚡ &nbsp; MPLADS Fund Utilization by State (FY 2023-24)</div>",
        unsafe_allow_html=True,
    )
    sorted_util = sorted(STATE_MPLADS_UTILIZATION_2023_24.items(), key=lambda x: x[1], reverse=True)
    df_u = pd.DataFrame(sorted_util, columns=["State", "Utilization (%)"])
    colors_util = [TEAL if v >= 85 else ORANGE if v >= 75 else RED for v in df_u["Utilization (%)"]]

    fig_util = go.Figure(go.Bar(
        x=df_u["Utilization (%)"], y=df_u["State"], orientation="h",
        marker_color=colors_util,
        text=[f"{v:.1f}%" for v in df_u["Utilization (%)"]],
        textposition="outside",
        textfont=dict(color=TEXT_MUTED, size=9),
        hovertemplate="%{y}: %{x:.1f}% utilized<extra></extra>",
    ))
    fig_util.add_vline(x=85, line_dash="dash", line_color=TEAL, opacity=0.7,
                       annotation_text="85% target",
                       annotation_font_color=TEAL)
    fig_util.update_layout(
        paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
        height=680,
        margin=dict(l=8, r=60, t=8, b=8),
        xaxis=dict(title=dict(text="% Utilized", font=dict(color=TEXT_SEC)),
                   gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC), range=[50, 100]),
        yaxis=dict(gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    )
    st.plotly_chart(fig_util, use_container_width=True)
    st.markdown(insight_box(
        "Utilization rate measures <b>how much of allocated MPLADS funds were actually spent</b>. "
        "<b>Gujarat, Goa, and Tamil Nadu</b> consistently show >90% utilization. "
        "Low utilization in some northeastern states is due to terrain challenges, "
        "contractor availability, and procedural delays. Unutilized funds lapse to the government."
    ), unsafe_allow_html=True)

elif view == "Work Categories":
    st.markdown(
        f"<div class='section-label'>🔧 &nbsp; What Does MPLADS Money Build? (FY 2023-24)</div>",
        unsafe_allow_html=True,
    )
    categories = list(MPLADS_WORK_CATEGORY_PCT.keys())
    values     = list(MPLADS_WORK_CATEGORY_PCT.values())
    colors_cat = [ORANGE, TEAL, BLUE_SOFT, RED, "#9A7000", "#006652", "#7B3A9E", "#0A7A9A", "#5A4530"]

    left, right = st.columns([1, 1])
    with left:
        fig_pie = go.Figure(go.Pie(
            labels=categories, values=values,
            marker=dict(colors=colors_cat),
            textinfo="label+percent",
            textfont=dict(size=10, family="DM Sans"),
            hole=0.45,
            hovertemplate="%{label}: %{value:.1f}%<extra></extra>",
        ))
        fig_pie.update_layout(
            paper_bgcolor=PLOTLY_PAPER,
            font=dict(color=TEXT_PRIMARY),
            height=380,
            margin=dict(l=8, r=8, t=8, b=8),
            showlegend=False,
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with right:
        st.markdown("<br><br>", unsafe_allow_html=True)
        for cat, pct in sorted(MPLADS_WORK_CATEGORY_PCT.items(), key=lambda x: x[1], reverse=True):
            st.markdown(
                f"""
                <div style='display:flex; justify-content:space-between; align-items:center;
                             padding:0.5rem 0.8rem; margin-bottom:0.3rem;
                             background:{BG_SURFACE}; border:1px solid {BORDER};
                             border-radius:8px;'>
                  <span style='font-family:"DM Sans",sans-serif; font-size:0.84rem;
                               color:{TEXT_PRIMARY};'>{cat}</span>
                  <span style='font-family:"JetBrains Mono",monospace; font-size:0.88rem;
                               font-weight:500; color:{ORANGE};'>{pct:.1f}%</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(insight_box(
        "<b>Roads & Bridges</b> (22.4%) and <b>Drinking Water & Sanitation</b> (18.5%) "
        "dominate MPLADS spending — reflecting constituents' top priorities. "
        "Education and health infrastructure together account for ~28%. "
        "Projects must be within the MP's own constituency."
    ), unsafe_allow_html=True)

elif view == "Development Index":
    st.markdown(
        f"<div class='section-label'>🏆 &nbsp; Most vs Least Developed Constituencies</div>",
        unsafe_allow_html=True,
    )
    left, right = st.columns(2)

    with left:
        st.markdown(
            f"<div style='font-family:\"DM Sans\",sans-serif; font-size:0.78rem; font-weight:600; "
            f"color:{TEAL}; margin-bottom:0.6rem;'>TOP 10 MOST DEVELOPED</div>",
            unsafe_allow_html=True,
        )
        for i, row in enumerate(TOP_DEVELOPED_CONSTITUENCIES):
            st.markdown(
                f"""
                <div class='scorecard'>
                  <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <div>
                      <span style='font-family:"JetBrains Mono",monospace; font-size:0.85rem;
                                   color:{TEXT_MUTED}; margin-right:0.5rem;'>#{i+1}</span>
                      <span style='font-family:"DM Sans",sans-serif; font-weight:600;
                                   color:{TEXT_PRIMARY}; font-size:0.88rem;'>{row["constituency"]}</span>
                      <span style='font-family:"DM Sans",sans-serif; color:{TEXT_MUTED};
                                   font-size:0.75rem; margin-left:0.4rem;'>· {row["state"]}</span>
                    </div>
                    <span style='font-family:"JetBrains Mono",monospace; font-size:1rem;
                                 font-weight:500; color:{TEAL};'>{row["index"]}</span>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with right:
        st.markdown(
            f"<div style='font-family:\"DM Sans\",sans-serif; font-size:0.78rem; font-weight:600; "
            f"color:{RED}; margin-bottom:0.6rem;'>10 MOST UNDER-DEVELOPED</div>",
            unsafe_allow_html=True,
        )
        for i, row in enumerate(LEAST_DEVELOPED_CONSTITUENCIES):
            st.markdown(
                f"""
                <div class='scorecard'>
                  <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <div>
                      <span style='font-family:"JetBrains Mono",monospace; font-size:0.85rem;
                                   color:{TEXT_MUTED}; margin-right:0.5rem;'>#{i+1}</span>
                      <span style='font-family:"DM Sans",sans-serif; font-weight:600;
                                   color:{TEXT_PRIMARY}; font-size:0.88rem;'>{row["constituency"]}</span>
                      <span style='font-family:"DM Sans",sans-serif; color:{TEXT_MUTED};
                                   font-size:0.75rem; margin-left:0.4rem;'>· {row["state"]}</span>
                    </div>
                    <span style='font-family:"JetBrains Mono",monospace; font-size:1rem;
                                 font-weight:500; color:{RED};'>{row["index"]}</span>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(insight_box(
        "The <b>Development Index</b> is a composite of HDI sub-indicators (literacy, health, income), "
        "access to roads, electricity, water, and MPLADS fund utilization rate. "
        "Urban/semi-urban constituencies in Gujarat, Maharashtra, and Karnataka dominate the top 10. "
        "Bihar and UP account for 8 of the 10 least-developed — concentrated poverty demands targeted investment."
    ), unsafe_allow_html=True)

st.markdown(footer_html(), unsafe_allow_html=True)
