"""BharatBudget — home page."""

import streamlit as st
import plotly.graph_objects as go

from utils.styling import (
    footer_html, insight_box, page_header,
    ORANGE, ORANGE_LIGHT, TEAL, TEXT_PRIMARY, TEXT_SEC, TEXT_MUTED,
    BG_SURFACE, BG_ELEVATED, BORDER, GRID_COLOR, PLOTLY_PAPER, PLOTLY_PLOT,
    ORANGE_DIM,
)
from data.budget_data import TOTAL_BUDGET, BUDGET_YEARS, MINISTRY_ALLOCATIONS, NOMINAL_GDP

# ── Sidebar ───────────────────────────────────────────────────────────────────

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    page_header(
        "🇮🇳",
        "BharatBudget",
        "India's public finance — made simple, visual, and useful for every citizen. Follow the money across ministries, years, and states.",
    ),
    unsafe_allow_html=True,
)

# Badge pills
st.markdown(
    f"""
    <div style='margin:-0.6rem 0 1.2rem 0;'>
      <span class='badge'>2015-16 → 2024-25</span>
      &nbsp;
      <span class='badge badge-teal'>₹ in Lakh Crore</span>
      &nbsp;
      <span class='badge badge-blue'>18 Ministries</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Why this matters ──────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class='why-box'>
      <div style='font-family:"DM Sans",sans-serif; font-size:0.6rem; font-weight:700;
                  letter-spacing:0.09em; text-transform:uppercase; color:{ORANGE};
                  margin-bottom:0.6rem;'>Why this matters</div>
      <p style='font-family:"DM Sans",sans-serif; color:{TEXT_SEC}; margin:0;
                font-size:0.92rem; line-height:1.8;'>
        Every rupee the Indian government spends — on roads, schools, hospitals, defence, or
        subsidies — comes from your taxes. The Union Budget decides these priorities for
        <b style='color:{TEXT_PRIMARY};'>1.4 billion people</b>.
        <br/>
        Most budget coverage is jargon-heavy and inaccessible.
        <b style='color:{ORANGE};'>BharatBudget</b> cuts through that — explore where the money
        goes, how priorities shift year to year, and whether spending actually improves lives.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Statistics card — top 4 ministries (aghasisahakyan1 style) ───────────────
STAT_MINISTRIES = ["Interest Payments", "Defence", "Road Transport & Highways", "Rural Development"]
STAT_COLORS     = ["#7A6250", "#B03030", "#C84E00", "#2E7D60"]
_yd = MINISTRY_ALLOCATIONS["2024-25"]
_tt = TOTAL_BUDGET["2024-25"]
_stat_vals = [_yd.get(m, {}).get("allocated", 0) for m in STAT_MINISTRIES]
_max_v = max(_stat_vals) if _stat_vals else 1

bars_html = ""
for m, v, col in zip(STAT_MINISTRIES, _stat_vals, STAT_COLORS):
    pct   = v / _tt * 100
    h_pct = v / _max_v * 100
    bars_html += f"""
    <div class='bar-col'>
      <div class='bar-badge'>{pct:.0f}%</div>
      <div class='bar-fill{"" if col != "#C84E00" else " highlight"}' style='height:{h_pct:.0f}%; background:linear-gradient(180deg,{col}dd,{col});'></div>
      <div class='bar-label'>{m.split("/")[0].strip()[:12]}</div>
    </div>"""

st.markdown(
    f"""
    <div class='stat-bar-card'>
      <div style='font-family:"DM Sans",sans-serif; font-size:0.6rem; font-weight:700;
                  letter-spacing:0.09em; text-transform:uppercase; color:{ORANGE}; margin-bottom:0.2rem;'>
        Top Ministry Allocations 2024-25
      </div>
      <div class='bars-row'>{bars_html}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# ── Key stats ─────────────────────────────────────────────────────────────────
CURRENT_YEAR = "2024-25"
PREV_YEAR    = "2023-24"

cur_total  = TOTAL_BUDGET[CURRENT_YEAR]
prev_total = TOTAL_BUDGET[PREV_YEAR]
cur_gdp    = NOMINAL_GDP[CURRENT_YEAR]
cur_data   = MINISTRY_ALLOCATIONS[CURRENT_YEAR]

biggest_ministry = max(cur_data, key=lambda m: cur_data[m]["allocated"])
biggest_val      = cur_data[biggest_ministry]["allocated"]
budget_gdp_pct   = cur_total / cur_gdp * 100
yoy_change_pct   = (cur_total - prev_total) / prev_total * 100
per_citizen      = cur_total * 1e5 / 140

st.markdown(
    f"<div class='section-label'>📌 &nbsp; Union Budget {CURRENT_YEAR} — At a Glance</div>",
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Total Budget 2024-25", f"₹{cur_total:.2f} L cr",
              f"+{yoy_change_pct:.1f}% vs {PREV_YEAR}")
with c2:
    st.metric("Budget as % of GDP", f"{budget_gdp_pct:.1f}%", "of ₹324 L cr nominal GDP")
with c3:
    st.metric("Biggest Allocation", biggest_ministry, f"₹{biggest_val:.2f} L cr")
with c4:
    st.metric("Per Citizen (est.)", f"₹{per_citizen:,.0f}", "per Indian in 2024-25")

st.markdown("<br>", unsafe_allow_html=True)

# ── Budget growth chart ───────────────────────────────────────────────────────
st.markdown(
    "<div class='section-label'>📈 &nbsp; Budget Growth: 2015-16 to 2024-25</div>",
    unsafe_allow_html=True,
)

years  = BUDGET_YEARS
totals = [TOTAL_BUDGET[y] for y in years]
gdps   = [NOMINAL_GDP[y] for y in years]
pcts   = [t / g * 100 for t, g in zip(totals, gdps)]

fig_overview = go.Figure()
fig_overview.add_trace(go.Bar(
    x=years, y=totals,
    name="Total Budget (₹ L cr)",
    marker=dict(
        color=totals,
        colorscale=[[0, "#1A1A22"], [0.5, "#7A3200"], [1, ORANGE]],
        showscale=False,
        line=dict(width=0),
    ),
    text=[f"₹{t:.1f}" for t in totals],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=9, family="JetBrains Mono, monospace"),
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra></extra>",
))
fig_overview.add_trace(go.Scatter(
    x=years, y=pcts,
    name="% of GDP",
    yaxis="y2",
    mode="lines+markers",
    line=dict(color=TEAL, width=2, dash="dot"),
    marker=dict(size=6, color=TEAL, line=dict(width=1, color=BG_ELEVATED)),
    hovertemplate="%{x}: %{y:.1f}% of GDP<extra></extra>",
))
fig_overview.update_layout(
    paper_bgcolor=PLOTLY_PAPER,
    plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=340,
    margin=dict(l=8, r=8, t=16, b=8),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=TEXT_SEC, size=11),
                orientation="h", y=1.1, x=0),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER,
               tickfont=dict(color=TEXT_SEC, size=11)),
    yaxis=dict(
        title=dict(text="₹ Lakh Crore", font=dict(color=TEXT_SEC)),
        gridcolor=GRID_COLOR,
        tickfont=dict(color=TEXT_SEC),
    ),
    yaxis2=dict(
        title=dict(text="% of GDP", font=dict(color=TEAL)),
        overlaying="y", side="right",
        tickfont=dict(color=TEAL),
        gridcolor="rgba(0,0,0,0)",
    ),
    barmode="group",
)
st.plotly_chart(fig_overview, use_container_width=True)
st.markdown(
    insight_box(
        "India's Union Budget has grown <b>2.68×</b> in 10 years — from ₹17.78 L cr (2015-16) to "
        "₹47.65 L cr (2024-25). Budget as a share of GDP stayed between <b>13–16%</b>, "
        "with a spike in 2020-21 due to COVID-19 relief spending."
    ),
    unsafe_allow_html=True,
)

# ── Milestones ────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-label'>🔑 &nbsp; 10-Year Budget Milestones</div>",
    unsafe_allow_html=True,
)

milestones = [
    ("🛣️", "Roads capex",        "6.6×",  "₹0.42 → ₹2.78 L cr since 2015-16"),
    ("🏥", "Health spending",    "2.7×",  "₹0.33 → ₹0.90 L cr in a decade"),
    ("🎓", "Education",          "1.8×",  "₹0.69 → ₹1.25 L cr allocated in 2024-25"),
    ("🛡️", "Defence",            "1.95×", "₹3.18 → ₹6.21 L cr; always the #1 ministry"),
    ("💧", "Jal Jeevan Mission", "3.85×", "Water budget grew ₹0.20 → ₹0.77 L cr"),
    ("🚂", "Railways capex",     "6.4×",  "₹0.40 → ₹2.55 L cr — biggest infra push ever"),
]

cols = st.columns(3)
for i, (icon, label, change, detail) in enumerate(milestones):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class='milestone-card' style='margin-bottom:0.9rem;'>
              <div style='display:flex; align-items:flex-start; gap:0.7rem;'>
                <span style='font-size:1.4rem; line-height:1; flex-shrink:0;'>{icon}</span>
                <div>
                  <div style='font-family:"JetBrains Mono",monospace; font-size:1.4rem;
                              font-weight:500; color:{ORANGE}; letter-spacing:-0.03em;
                              line-height:1;'>{change}</div>
                  <div style='font-family:"DM Sans",sans-serif; color:{TEXT_PRIMARY};
                              font-size:0.87rem; font-weight:600; margin:0.2rem 0 0.1rem 0;'>
                    {label}
                  </div>
                  <div style='font-family:"DM Sans",sans-serif; color:{TEXT_SEC};
                              font-size:0.73rem; line-height:1.5;'>{detail}</div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(footer_html(), unsafe_allow_html=True)
