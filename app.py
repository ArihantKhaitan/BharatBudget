"""BharatBudget — India's Union Budget Explorer
Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from utils.styling import GLOBAL_CSS, footer_html, ORANGE, TEAL, RED, TEXT_MUTED, NAVY_CARD, NAVY_LIGHT
from data.budget_data import TOTAL_BUDGET, BUDGET_YEARS, MINISTRY_ALLOCATIONS, NOMINAL_GDP
from components.charts import fmt_lcr, gauge_chart

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
        <div style='text-align:center; padding:1rem 0 0.5rem 0;'>
          <span style='font-size:2rem;'>🇮🇳</span>
          <h2 style='margin:0; color:#FF9933; font-size:1.4rem; letter-spacing:1px;'>
            BharatBudget
          </h2>
          <p style='font-size:0.75rem; color:{TEXT_MUTED}; margin:0.2rem 0 1rem 0;'>
            India's Public Finance Tracker
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        f"<p style='font-size:0.78rem;color:{TEXT_MUTED};padding:0 0.5rem;'>"
        "Navigate using the <b style='color:#FF9933;'>pages</b> listed below or "
        "in Streamlit's sidebar page list above."
        "</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div style='padding:0.5rem;'>
          <a href='/Budget_Explorer' style='color:{ORANGE}; text-decoration:none;'>
            🔍 Budget Explorer</a><br>
          <a href='/Follow_the_Money' style='color:{ORANGE}; text-decoration:none;'>
            💸 Follow the Money</a><br>
          <a href='/Impact_Correlator' style='color:{ORANGE}; text-decoration:none;'>
            📊 Impact Correlator</a><br>
          <a href='/State_Finance_Tracker' style='color:{ORANGE}; text-decoration:none;'>
            🗺️ State Finance Tracker</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        f"<p style='font-size:0.72rem;color:{TEXT_MUTED};padding:0 0.5rem;'>"
        "Data: <a href='https://indiabudget.gov.in' style='color:{ORANGE};'>indiabudget.gov.in</a>, "
        "<a href='https://data.gov.in' style='color:{ORANGE};'>data.gov.in</a>, RBI DBIE, MOSPI"
        "</p>".replace("{ORANGE}", ORANGE),
        unsafe_allow_html=True,
    )

# ── Hero section ──────────────────────────────────────────────────────────────
col_logo, col_tagline = st.columns([1, 4])
with col_logo:
    st.markdown(
        "<div style='font-size:4rem; text-align:center; padding-top:0.4rem;'>🇮🇳</div>",
        unsafe_allow_html=True,
    )
with col_tagline:
    st.markdown(
        f"""
        <h1 style='color:#FF9933; margin:0; font-size:2.4rem; letter-spacing:1px;'>
          BharatBudget
        </h1>
        <p style='color:{TEXT_MUTED}; margin:0.2rem 0 0 0; font-size:1rem;'>
          India's Union Budget — made simple, visual, and useful for every citizen.
        </p>
        <span class='badge'>2015-16 to 2024-25</span>
        &nbsp;
        <span class='badge' style='background:{TEAL}22; color:{TEAL}; border-color:{TEAL}55;'>
          ₹ in Lakh Crore
        </span>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# ── Why this matters ──────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div style='background:{NAVY_CARD}; border:1px solid {NAVY_LIGHT};
                border-radius:12px; padding:1.2rem 1.5rem; margin-bottom:1.5rem;'>
      <h3 style='color:#FF9933; margin:0 0 0.6rem 0; font-size:1.1rem;'>
        🤔 Why does the Union Budget matter to you?
      </h3>
      <p style='color:{TEXT_MUTED}; margin:0; font-size:0.92rem; line-height:1.7;'>
        Every rupee the Indian government spends — on roads, schools, hospitals, defence, or
        subsidies — comes from your taxes. The <b style='color:#E8EDF5;'>Union Budget</b> is
        the single document that decides these priorities for 1.4 billion people.
        <br><br>
        Yet most budget coverage is full of jargon. <b style='color:#FF9933;'>BharatBudget</b>
        cuts through that — letting you explore where the money actually goes, how
        priorities have shifted over the years, and whether government spending is
        actually improving lives.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Key stats: current year ───────────────────────────────────────────────────
CURRENT_YEAR = "2024-25"
PREV_YEAR    = "2023-24"

cur_total  = TOTAL_BUDGET[CURRENT_YEAR]
prev_total = TOTAL_BUDGET[PREV_YEAR]
cur_gdp    = NOMINAL_GDP[CURRENT_YEAR]

cur_data = MINISTRY_ALLOCATIONS[CURRENT_YEAR]
biggest_ministry = max(cur_data, key=lambda m: cur_data[m]["allocated"])
biggest_val      = cur_data[biggest_ministry]["allocated"]

budget_gdp_pct   = cur_total / cur_gdp * 100
yoy_change_pct   = (cur_total - prev_total) / prev_total * 100

st.markdown(
    f"<h2 style='color:#E8EDF5; font-size:1.2rem; margin-bottom:0.8rem;'>"
    f"📌 Union Budget {CURRENT_YEAR} — At a Glance</h2>",
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Total Budget 2024-25", f"₹{cur_total:.2f} L cr",
              f"+{yoy_change_pct:.1f}% vs {PREV_YEAR}")
with c2:
    st.metric("Budget as % of GDP", f"{budget_gdp_pct:.1f}%",
              "of ₹324 L cr nominal GDP")
with c3:
    st.metric("Biggest Allocation", biggest_ministry,
              f"₹{biggest_val:.2f} L cr")
with c4:
    per_citizen = cur_total * 1e5 / 140  # in ₹ (1 L cr = 1e12 paise → 1e10 ₹; pop ~140 cr)
    st.metric("Per Citizen (approx)", f"₹{per_citizen:,.0f}",
              "₹ per Indian in 2024-25")

st.markdown("<br>", unsafe_allow_html=True)

# ── Budget growth timeline ────────────────────────────────────────────────────
st.markdown(
    f"<h2 style='color:#E8EDF5; font-size:1.2rem; margin-bottom:0.8rem;'>"
    f"📈 Budget Growth: 2015-16 to 2024-25</h2>",
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
        colorscale=[[0, "#1E3A5F"], [1, "#FF9933"]],
        showscale=False,
    ),
    text=[f"₹{t:.1f}" for t in totals],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=10),
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra></extra>",
))
fig_overview.add_trace(go.Scatter(
    x=years, y=pcts,
    name="% of GDP",
    yaxis="y2",
    mode="lines+markers",
    line=dict(color=TEAL, width=2, dash="dot"),
    marker=dict(size=6),
    hovertemplate="%{x}: %{y:.1f}% of GDP<extra></extra>",
))
fig_overview.update_layout(
    paper_bgcolor="#0B1437",
    plot_bgcolor="#131E3A",
    font=dict(color="#E8EDF5"),
    height=340,
    margin=dict(l=16, r=16, t=24, b=16),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=TEXT_MUTED)),
    xaxis=dict(gridcolor=NAVY_LIGHT, linecolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
    yaxis=dict(title="₹ Lakh Crore", gridcolor=NAVY_LIGHT,
               linecolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
    yaxis2=dict(title="% of GDP", overlaying="y", side="right",
                tickfont=dict(color=TEAL), titlefont=dict(color=TEAL),
                gridcolor="rgba(0,0,0,0)"),
    barmode="group",
)
st.plotly_chart(fig_overview, use_container_width=True)
st.markdown(
    f"<div class='insight-box'>"
    f"India's Union Budget has grown <b>2.68×</b> in 10 years — from ₹17.78 L cr (2015-16) to "
    f"₹47.65 L cr (2024-25). Budget as a share of GDP stayed between <b>13–16%</b>, "
    f"with a spike in 2020-21 due to COVID-19 relief spending."
    f"</div>",
    unsafe_allow_html=True,
)

# ── Quick-win stats row ───────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    f"<h2 style='color:#E8EDF5; font-size:1.2rem; margin-bottom:0.8rem;'>"
    f"🔑 10-Year Budget Milestones</h2>",
    unsafe_allow_html=True,
)

milestones = [
    ("🛣️ Roads capex", "6.6×", "₹0.42 → ₹2.78 L cr since 2015-16"),
    ("🏥 Health spending", "2.7×", "₹0.33 → ₹0.90 L cr in a decade"),
    ("🎓 Education", "1.8×", "₹0.69 → ₹1.25 L cr allocated in 2024-25"),
    ("🛡️ Defence", "1.95×", "₹3.18 → ₹6.21 L cr; always the #1 ministry"),
    ("💧 Jal Jeevan Mission", "3.85×", "Water budget grew from ₹0.20 → ₹0.77 L cr"),
    ("🚂 Railways capex", "6.4×", "₹0.40 → ₹2.55 L cr — biggest infra push in decades"),
]

cols = st.columns(3)
for i, (icon_label, change, detail) in enumerate(milestones):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style='background:{NAVY_CARD}; border:1px solid {NAVY_LIGHT};
                        border-radius:10px; padding:1rem; margin-bottom:0.8rem;'>
              <div style='font-size:1.1rem; color:#FF9933; font-weight:700;'>{change}</div>
              <div style='color:#E8EDF5; font-size:0.9rem; font-weight:600;'>{icon_label}</div>
              <div style='color:{TEXT_MUTED}; font-size:0.78rem; margin-top:0.3rem;'>{detail}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")
st.markdown(
    f"""
    <div style='text-align:center; color:{TEXT_MUTED}; font-size:0.88rem; margin-bottom:1rem;'>
      Use the <b style='color:#FF9933;'>sidebar navigation</b> to explore Budget Explorer,
      Follow the Money, Impact Correlator, and State Finance Tracker.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(footer_html(), unsafe_allow_html=True)
