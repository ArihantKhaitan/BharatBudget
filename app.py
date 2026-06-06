"""BharatBudget — India's Union Budget Explorer
Run with: streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go

from utils.styling import (
    GLOBAL_CSS, footer_html, insight_box,
    ORANGE, ORANGE_LIGHT, TEAL, BEIGE, BEIGE_MUTED, BEIGE_DIM,
    BG_CARD, BG_RAISED, BORDER, GRID_COLOR, PLOTLY_PAPER, PLOTLY_PLOT,
    WHITE,
    # Legacy aliases
    TEXT_MUTED, NAVY_CARD, NAVY_LIGHT,
)
from data.budget_data import TOTAL_BUDGET, BUDGET_YEARS, MINISTRY_ALLOCATIONS, NOMINAL_GDP

st.set_page_config(
    page_title="BharatBudget — India's Public Finance Tracker",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        f"""
        <div style='padding:1.2rem 0.5rem 0.5rem 0.5rem;'>
          <div style='display:flex; align-items:center; gap:0.6rem; margin-bottom:0.4rem;'>
            <span style='font-size:1.6rem;'>🇮🇳</span>
            <div>
              <div style='font-size:1.15rem; font-weight:700; color:{ORANGE};
                          letter-spacing:-0.01em;'>BharatBudget</div>
              <div style='font-size:0.7rem; color:{BEIGE_MUTED}; letter-spacing:0.04em;
                          text-transform:uppercase;'>Public Finance Tracker</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        f"<p style='font-size:0.75rem; color:{BEIGE_MUTED}; padding:0 0.3rem 0.6rem;'>"
        "Use the pages listed in Streamlit's navigation above to explore the dashboard."
        "</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        f"<p style='font-size:0.7rem; color:{BEIGE_DIM}; padding:0 0.3rem;'>"
        f"Data: <a href='https://indiabudget.gov.in' style='color:{ORANGE};'>indiabudget.gov.in</a> · "
        f"<a href='https://data.gov.in' style='color:{ORANGE};'>data.gov.in</a> · RBI DBIE · MOSPI"
        "</p>",
        unsafe_allow_html=True,
    )

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div style='padding:0.5rem 0 1.5rem 0;'>
      <div class='page-title'>BharatBudget</div>
      <p style='color:{BEIGE_MUTED}; font-size:0.95rem; margin:0.2rem 0 0.8rem 0;'>
        India's Union Budget — made simple, visual, and useful for every citizen.
      </p>
      <span class='badge'>2015-16 → 2024-25</span>
      &nbsp;
      <span class='badge badge-teal'>₹ in Lakh Crore</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Why this matters ──────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div style='background:{BG_CARD}; border:1px solid {BORDER};
                border-radius:14px; padding:1.3rem 1.6rem; margin-bottom:1.8rem;'>
      <div style='font-size:0.65rem; font-weight:600; letter-spacing:0.07em;
                  text-transform:uppercase; color:{ORANGE}; margin-bottom:0.5rem;'>
        Why this matters
      </div>
      <p style='color:{BEIGE_MUTED}; margin:0; font-size:0.9rem; line-height:1.75;'>
        Every rupee the Indian government spends — on roads, schools, hospitals, defence, or
        subsidies — comes from your taxes. The Union Budget decides these priorities for
        <b style='color:{BEIGE};'>1.4 billion people</b>.
        <br><br>
        Most budget coverage is jargon-heavy and inaccessible.
        <b style='color:{ORANGE};'>BharatBudget</b> cuts through that — explore where the money
        goes, how priorities shift year to year, and whether spending actually improves lives.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

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
    f"<div class='section-header'>📌 Union Budget {CURRENT_YEAR} — At a Glance</div>",
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
    "<div class='section-header'>📈 Budget Growth: 2015-16 to 2024-25</div>",
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
        colorscale=[[0, "#1A1A22"], [0.5, "#8B3A00"], [1, ORANGE]],
        showscale=False,
        line=dict(width=0),
    ),
    text=[f"₹{t:.1f}" for t in totals],
    textposition="outside",
    textfont=dict(color=BEIGE_MUTED, size=9),
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra></extra>",
))
fig_overview.add_trace(go.Scatter(
    x=years, y=pcts,
    name="% of GDP",
    yaxis="y2",
    mode="lines+markers",
    line=dict(color=TEAL, width=2, dash="dot"),
    marker=dict(size=5, color=TEAL),
    hovertemplate="%{x}: %{y:.1f}% of GDP<extra></extra>",
))
fig_overview.update_layout(
    paper_bgcolor=PLOTLY_PAPER,
    plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=BEIGE, family="Inter, sans-serif"),
    height=320,
    margin=dict(l=8, r=8, t=12, b=8),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=BEIGE_MUTED, size=11),
                orientation="h", y=1.1, x=0),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=BEIGE_MUTED, size=11)),
    yaxis=dict(title=dict(text="₹ Lakh Crore", font=dict(color=BEIGE_MUTED)),
               gridcolor=GRID_COLOR, tickfont=dict(color=BEIGE_MUTED)),
    yaxis2=dict(title=dict(text="% of GDP", font=dict(color=TEAL)),
                overlaying="y", side="right",
                tickfont=dict(color=TEAL),
                gridcolor="rgba(0,0,0,0)"),
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
st.markdown("---")
st.markdown(
    "<div class='section-header'>🔑 10-Year Budget Milestones</div>",
    unsafe_allow_html=True,
)

milestones = [
    ("🛣️ Roads capex",        "6.6×",  "₹0.42 → ₹2.78 L cr since 2015-16"),
    ("🏥 Health spending",    "2.7×",  "₹0.33 → ₹0.90 L cr in a decade"),
    ("🎓 Education",          "1.8×",  "₹0.69 → ₹1.25 L cr allocated in 2024-25"),
    ("🛡️ Defence",            "1.95×", "₹3.18 → ₹6.21 L cr; always the #1 ministry"),
    ("💧 Jal Jeevan Mission", "3.85×", "Water budget grew ₹0.20 → ₹0.77 L cr"),
    ("🚂 Railways capex",     "6.4×",  "₹0.40 → ₹2.55 L cr — biggest infra push ever"),
]

cols = st.columns(3)
for i, (label, change, detail) in enumerate(milestones):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class='stat-card' style='margin-bottom:0.8rem;'>
              <div style='font-size:1.4rem; font-weight:800; color:{ORANGE};
                          letter-spacing:-0.03em; line-height:1;'>{change}</div>
              <div style='color:{BEIGE}; font-size:0.88rem; font-weight:600;
                          margin:0.25rem 0 0.15rem 0;'>{label}</div>
              <div style='color:{BEIGE_MUTED}; font-size:0.75rem;'>{detail}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")
st.markdown(
    f"<div style='text-align:center; color:{BEIGE_MUTED}; font-size:0.85rem; padding:0.5rem 0 1rem;'>"
    f"Use the <b style='color:{ORANGE};'>sidebar navigation</b> to explore Budget Explorer, "
    "Follow the Money, Impact Correlator, and State Finance Tracker."
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(footer_html(), unsafe_allow_html=True)
