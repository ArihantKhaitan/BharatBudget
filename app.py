"""BharatBudget — India's Union Budget Explorer
Run with: streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go

from utils.styling import (
    GLOBAL_CSS, footer_html, insight_box,
    ORANGE, ORANGE_LIGHT, TEAL, TEXT_PRIMARY, TEXT_SEC, TEXT_MUTED,
    BG_SURFACE, BG_ELEVATED, BORDER, GRID_COLOR, PLOTLY_PAPER, PLOTLY_PLOT,
    ORANGE_DIM,
    # Legacy aliases still used below
    BEIGE, BEIGE_MUTED, BEIGE_DIM, NAVY_CARD, NAVY_LIGHT,
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
        <div style='padding:1.4rem 0.6rem 0.6rem 0.6rem;'>
          <div style='display:flex; align-items:center; gap:0.7rem; margin-bottom:0.5rem;'>
            <span style='font-size:1.8rem; line-height:1;'>🇮🇳</span>
            <div>
              <div style='font-family:"Playfair Display",Georgia,serif;
                          font-size:1.2rem; font-weight:700; color:{ORANGE};
                          letter-spacing:-0.01em; line-height:1.1;'>BharatBudget</div>
              <div style='font-family:"DM Sans",sans-serif; font-size:0.62rem;
                          color:{TEXT_MUTED}; letter-spacing:0.08em;
                          text-transform:uppercase; margin-top:1px;'>Public Finance Tracker</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        f"<p style='font-family:\"DM Sans\",sans-serif; font-size:0.76rem; color:{TEXT_SEC}; "
        "padding:0 0.3rem 0.5rem;'>"
        "Navigate using the pages in the sidebar to explore India's Union Budget."
        "</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        f"<p style='font-family:\"DM Sans\",sans-serif; font-size:0.68rem; color:{TEXT_MUTED}; padding:0 0.3rem;'>"
        f"Data: <a href='https://indiabudget.gov.in' style='color:{ORANGE};text-decoration:none;'>indiabudget.gov.in</a> · "
        f"<a href='https://data.gov.in' style='color:{ORANGE};text-decoration:none;'>data.gov.in</a> · RBI DBIE · MOSPI"
        "</p>",
        unsafe_allow_html=True,
    )

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div style='padding:0.4rem 0 2rem 0; animation:fadeUp 0.5s ease forwards;'>
      <div style='font-family:"DM Sans",sans-serif; font-size:0.62rem; font-weight:600;
                  letter-spacing:0.1em; text-transform:uppercase; color:{ORANGE};
                  margin-bottom:0.6rem;'>
        🇮🇳 &nbsp; India's Union Budget
      </div>
      <h1 style='font-family:"Playfair Display",Georgia,serif;
                 font-size:clamp(2.2rem,5vw,3.2rem); font-weight:700;
                 letter-spacing:-0.02em; line-height:1.1; margin:0 0 0.6rem 0;
                 background:linear-gradient(90deg,{ORANGE} 0%,{ORANGE_LIGHT} 45%,{TEXT_PRIMARY} 100%);
                 -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                 background-clip:text;'>
        BharatBudget
      </h1>
      <p style='font-family:"DM Sans",sans-serif; color:{TEXT_SEC}; font-size:1.05rem;
                margin:0 0 1.2rem 0; max-width:600px; line-height:1.65;'>
        India's public finance — made simple, visual, and useful for every citizen.
        Follow the money across ministries, years, and states.
      </p>
      <span class='badge'>2015-16 → 2024-25</span>
      &nbsp;
      <span class='badge badge-teal'>₹ in Lakh Crore</span>
      &nbsp;
      <span class='badge' style='background:rgba(126,184,255,0.1);color:#7EB8FF;border-color:#7EB8FF33;'>18 Ministries</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Why this matters (glassmorphism card) ─────────────────────────────────────
st.markdown(
    f"""
    <div class='why-box' style='animation-delay:0.15s;'>
      <div style='font-family:"DM Sans",sans-serif; font-size:0.62rem; font-weight:600;
                  letter-spacing:0.08em; text-transform:uppercase; color:{ORANGE};
                  margin-bottom:0.7rem;'>Why this matters</div>
      <p style='font-family:"DM Sans",sans-serif; color:{TEXT_SEC}; margin:0;
                font-size:0.92rem; line-height:1.8;'>
        Every rupee the Indian government spends — on roads, schools, hospitals, defence, or
        subsidies — comes from your taxes. The Union Budget decides these priorities for
        <b style='color:{TEXT_PRIMARY};'>1.4 billion people</b>.
        <br/><br/>
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
    f"""
    <div style='font-family:"DM Sans",sans-serif; font-size:0.62rem; font-weight:600;
                letter-spacing:0.09em; text-transform:uppercase; color:{ORANGE};
                margin-bottom:0.8rem; margin-top:0.4rem;'>
      📌 &nbsp; Union Budget {CURRENT_YEAR} — At a Glance
    </div>
    """,
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
    f"""
    <div style='font-family:"DM Sans",sans-serif; font-size:0.62rem; font-weight:600;
                letter-spacing:0.09em; text-transform:uppercase; color:{ORANGE};
                margin-bottom:0.8rem;'>
      📈 &nbsp; Budget Growth: 2015-16 to 2024-25
    </div>
    """,
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
    f"""
    <div style='font-family:"DM Sans",sans-serif; font-size:0.62rem; font-weight:600;
                letter-spacing:0.09em; text-transform:uppercase; color:{ORANGE};
                margin-bottom:0.8rem;'>
      🔑 &nbsp; 10-Year Budget Milestones
    </div>
    """,
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
            <div class='milestone-card' style='margin-bottom:0.9rem; animation-delay:{i*0.07}s;'>
              <div style='display:flex; align-items:flex-start; gap:0.7rem;'>
                <span style='font-size:1.5rem; line-height:1; flex-shrink:0;'>{icon}</span>
                <div>
                  <div style='font-family:"JetBrains Mono",monospace; font-size:1.5rem;
                              font-weight:500; color:{ORANGE}; letter-spacing:-0.03em;
                              line-height:1;'>{change}</div>
                  <div style='font-family:"DM Sans",sans-serif; color:{TEXT_PRIMARY};
                              font-size:0.88rem; font-weight:600; margin:0.2rem 0 0.1rem 0;'>
                    {label}
                  </div>
                  <div style='font-family:"DM Sans",sans-serif; color:{TEXT_SEC};
                              font-size:0.74rem; line-height:1.5;'>{detail}</div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div style='background:rgba(255,107,53,0.05); border:1px solid {ORANGE}22;
                border-radius:12px; padding:1rem 1.4rem; text-align:center;'>
      <span style='font-family:"DM Sans",sans-serif; color:{TEXT_SEC}; font-size:0.88rem;'>
        Use the <b style='color:{ORANGE};'>sidebar navigation</b> to explore
        Budget Explorer, Follow the Money, Impact Correlator, and State Finance Tracker.
      </span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(footer_html(), unsafe_allow_html=True)
