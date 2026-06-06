"""Follow the Money — Multi-year ministry trend comparisons."""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from utils.styling import (
    GLOBAL_CSS, footer_html, insight_box, page_header,
    ORANGE, ORANGE_LIGHT, TEAL, RED, TEXT_MUTED, TEXT_SEC, TEXT_PRIMARY,
    NAVY_LIGHT, NAVY_CARD, BEIGE, BEIGE_MUTED, PLOTLY_PAPER, PLOTLY_PLOT,
    BORDER, GRID_COLOR,
)
from data.budget_data import BUDGET_YEARS, MINISTRY_ALLOCATIONS, TOTAL_BUDGET, COMPARISON_MINISTRIES
from components.charts import multiline_chart, yoy_bar

st.set_page_config(
    page_title="Follow the Money — BharatBudget",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
def build_ministry_df(ministries: list, value_key: str = "allocated") -> pd.DataFrame:
    rows = []
    for year in BUDGET_YEARS:
        row = {"year": year, "total": TOTAL_BUDGET[year]}
        for m in ministries:
            val = MINISTRY_ALLOCATIONS[year].get(m, {}).get(value_key)
            row[m] = val if val is not None else np.nan
        rows.append(row)
    return pd.DataFrame(rows)


MINISTRY_COLORS = {
    "Defence":                   "#E84040",
    "Education":                 "#4FC3F7",
    "Health & Family Welfare":   "#BA68C8",
    "Agriculture & Allied":      "#81C784",
    "Railways":                  "#FFB347",
    "Road Transport & Highways": ORANGE,
    "Rural Development":         "#00C49A",
    "Jal Shakti / Water":        "#29B6F6",
}

PALETTE = [ORANGE, "#E84040", "#7EB8FF", "#00C49A", "#C07BDB", "#6DBF7E", "#FF9A4D", "#4DC8E8"]

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        f"<div style='font-family:\"Playfair Display\",Georgia,serif; font-size:1.05rem; "
        f"font-weight:700; color:{ORANGE}; padding:1rem 0 0.2rem 0;'>💸 Follow the Money</div>",
        unsafe_allow_html=True,
    )
    selected_ministries = st.multiselect(
        "Compare ministries",
        COMPARISON_MINISTRIES,
        default=["Defence", "Education", "Health & Family Welfare", "Road Transport & Highways"],
    )
    show_pct_gdp = st.checkbox("Show as % of total budget", value=False)
    st.markdown("---")
    focus_ministry = st.selectbox("Deep-dive ministry (YoY chart)", COMPARISON_MINISTRIES, index=0)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    page_header(
        "💸",
        "Follow the Money",
        "How have India's budget priorities shifted over the last decade? Compare ministries, track trends, and find the story behind the numbers.",
    ),
    unsafe_allow_html=True,
)
st.markdown("---")

if not selected_ministries:
    st.warning("Please select at least one ministry from the sidebar.")
    st.stop()

df = build_ministry_df(selected_ministries)

# ── Multi-year line chart ─────────────────────────────────────────────────────
st.markdown(
    "<div class='section-header'>📈 Allocation Trends (2015-16 to 2024-25)</div>",
    unsafe_allow_html=True,
)

if show_pct_gdp:
    plot_df = df.copy()
    for m in selected_ministries:
        if m in plot_df.columns:
            plot_df[m] = plot_df[m] / plot_df["total"] * 100
    y_label = "% of Total Budget"
    title   = "Ministry share of total Union Budget (%)"
else:
    plot_df = df.copy()
    y_label = "₹ Lakh Crore"
    title   = "Ministry-wise Allocation — ₹ Lakh Crore"

fig_trend = multiline_chart(
    plot_df, x_col="year", y_cols=selected_ministries,
    title=title, y_label=y_label, color_map=MINISTRY_COLORS,
)
st.plotly_chart(fig_trend, use_container_width=True)

# Auto-generated insight
if "Defence" in selected_ministries and "Education" in selected_ministries:
    d_latest = MINISTRY_ALLOCATIONS["2024-25"]["Defence"]["allocated"]
    e_latest = MINISTRY_ALLOCATIONS["2024-25"]["Education"]["allocated"]
    ratio    = d_latest / e_latest
    st.markdown(
        insight_box(
            f"In 2024-25, India spends <b>₹{ratio:.1f} on Defence for every ₹1 on Education</b>. "
            f"Both have grown, but the defence-to-education ratio has widened from "
            f"{MINISTRY_ALLOCATIONS['2015-16']['Defence']['allocated']/MINISTRY_ALLOCATIONS['2015-16']['Education']['allocated']:.1f}x "
            f"(2015-16) to {ratio:.1f}x (2024-25)."
        ),
        unsafe_allow_html=True,
    )
else:
    first_m = selected_ministries[0]
    v_start = MINISTRY_ALLOCATIONS["2015-16"].get(first_m, {}).get("allocated", 0) or 0
    v_end   = MINISTRY_ALLOCATIONS["2024-25"].get(first_m, {}).get("allocated", 0) or 0
    growth  = (v_end - v_start) / v_start * 100 if v_start else 0
    st.markdown(
        insight_box(
            f"<b>{first_m}</b> has grown <b>{growth:.0f}%</b> over the decade — "
            f"from ₹{v_start:.2f} L cr (2015-16) to ₹{v_end:.2f} L cr (2024-25)."
        ),
        unsafe_allow_html=True,
    )

# ── Ratio comparison: "Did India prioritise X over Y?" ────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-header'>⚖️ Priority Ratio: Did India prioritise X over Y?</div>",
    unsafe_allow_html=True,
)

ratio_col1, ratio_col2 = st.columns(2)
with ratio_col1:
    m_numerator = st.selectbox("Ministry A (numerator)", COMPARISON_MINISTRIES, index=0)
with ratio_col2:
    remaining = [m for m in COMPARISON_MINISTRIES if m != m_numerator]
    m_denom   = st.selectbox("Ministry B (denominator)", remaining, index=1)

ratio_years, ratio_vals = [], []
for year in BUDGET_YEARS:
    va = MINISTRY_ALLOCATIONS[year].get(m_numerator, {}).get("allocated")
    vb = MINISTRY_ALLOCATIONS[year].get(m_denom, {}).get("allocated")
    if va is not None and vb and vb > 0:
        ratio_years.append(year)
        ratio_vals.append(va / vb)

fig_ratio = go.Figure()
colors_ratio = [TEAL if v > 1 else "#E57373" for v in ratio_vals]
fig_ratio.add_trace(go.Bar(
    x=ratio_years, y=ratio_vals,
    marker=dict(color=colors_ratio),
    hovertemplate="%{x}<br>%{y:.2f}x<extra></extra>",
    text=[f"{v:.2f}×" for v in ratio_vals],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=10),
))
fig_ratio.add_hline(y=1.0, line_dash="dot", line_color=ORANGE, opacity=0.7,
                    annotation_text="1:1 parity", annotation_font_color=ORANGE)
fig_ratio.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=BEIGE),
    height=300,
    margin=dict(l=16, r=16, t=10, b=16),
    xaxis=dict(gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
    yaxis=dict(title=f"Ratio ({m_numerator[:20]} ÷ {m_denom[:20]})",
               gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
)
st.plotly_chart(fig_ratio, use_container_width=True)

if ratio_vals:
    direction = "increased" if ratio_vals[-1] > ratio_vals[0] else "decreased"
    st.markdown(
        insight_box(
            f"The ratio of <b>{m_numerator}</b> to <b>{m_denom}</b> spending has "
            f"<b>{direction}</b> from <b>{ratio_vals[0]:.2f}×</b> (2015-16) to "
            f"<b>{ratio_vals[-1]:.2f}×</b> (2024-25). "
            f"A ratio above 1 means {m_numerator} gets more money; below 1 means {m_denom} does."
        ),
        unsafe_allow_html=True,
    )

# ── YoY % change deep-dive ────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-header'>📊 Year-on-Year % Change: {focus_ministry}</div>",
    unsafe_allow_html=True,
)

focus_df = pd.DataFrame([
    {"year": y, "allocated": MINISTRY_ALLOCATIONS[y].get(focus_ministry, {}).get("allocated")}
    for y in BUDGET_YEARS
]).dropna(subset=["allocated"])

fig_yoy = yoy_bar(focus_df, focus_ministry)
st.plotly_chart(fig_yoy, use_container_width=True)

vals_focus = focus_df["allocated"].tolist()
max_jump   = max(zip(focus_df["year"].tolist()[1:],
                     [((b-a)/a*100) for a,b in zip(vals_focus, vals_focus[1:])]),
                key=lambda x: abs(x[1]))
st.markdown(
    insight_box(
        f"<b>{focus_ministry}</b>'s biggest single-year jump was in "
        f"<b>{max_jump[0]}</b> at <b>{max_jump[1]:+.1f}%</b>. "
        f"Green bars = year-on-year increase; red bars = cut or slowdown."
    ),
    unsafe_allow_html=True,
)

# ── All-ministry ranked table ─────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<div class='section-header'>📋 Full Ministry-wise Comparison Table</div>",
    unsafe_allow_html=True,
)

year_a = st.selectbox("From year", BUDGET_YEARS, index=0, key="cmp_from")
year_b = st.selectbox("To year",   BUDGET_YEARS[::-1], index=0, key="cmp_to")

table_rows = []
for m in MINISTRY_ALLOCATIONS[year_a]:
    va = MINISTRY_ALLOCATIONS[year_a].get(m, {}).get("allocated")
    vb = MINISTRY_ALLOCATIONS[year_b].get(m, {}).get("allocated")
    if va is not None and vb is not None:
        chg = (vb - va) / va * 100
        table_rows.append({
            "Ministry": m,
            f"{year_a} (₹ L cr)": f"₹{va:.2f}",
            f"{year_b} (₹ L cr)": f"₹{vb:.2f}",
            "Change": f"{chg:+.1f}%",
            "_chg": chg,
        })

table_rows.sort(key=lambda x: x["_chg"], reverse=True)
for r in table_rows:
    del r["_chg"]

if table_rows:
    st.dataframe(pd.DataFrame(table_rows), use_container_width=True, hide_index=True)

st.markdown(footer_html(), unsafe_allow_html=True)
