"""Impact Correlator — Does more spending actually improve outcomes?"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from utils.styling import (
    footer_html, insight_box, page_header,
    ORANGE, TEAL, RED, TEXT_MUTED, TEXT_SEC, TEXT_PRIMARY, NAVY_LIGHT, NAVY_CARD, TEXT_MAIN,
    PLOTLY_PAPER, PLOTLY_PLOT,
)
from data.budget_data import BUDGET_YEARS, MINISTRY_ALLOCATIONS, TOTAL_BUDGET
from data.indicators import (
    INFANT_MORTALITY_RATE, LITERACY_RATE, GDP_GROWTH_RATE,
    HIGHWAY_LENGTH_KM, RAILWAY_ELECTRIFICATION, GROSS_ENROLMENT_RATIO_HE,
    OUT_OF_POCKET_HEALTH_PCT, AGRI_GDP_GROWTH, TAP_WATER_COVERAGE,
    SCHOOL_DROPOUT_RATE, MATERNAL_MORTALITY_RATE, LIFE_EXPECTANCY,
    PM_KISAN_BENEFICIARIES,
)
from components.charts import scatter_correlation

# ── Helpers ───────────────────────────────────────────────────────────────────
def ministry_series(ministry: str, value_key: str = "allocated") -> dict:
    return {
        y: MINISTRY_ALLOCATIONS[y].get(ministry, {}).get(value_key)
        for y in BUDGET_YEARS
    }

def pct_of_total(ministry: str) -> dict:
    return {
        y: (MINISTRY_ALLOCATIONS[y].get(ministry, {}).get("allocated") or 0) / TOTAL_BUDGET[y] * 100
        for y in BUDGET_YEARS
    }

def dual_axis_chart(years, spend_vals, outcome_vals,
                    spend_label, outcome_label, title,
                    invert_outcome=False) -> go.Figure:
    """Line chart with spending on left axis, outcome on right."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years, y=spend_vals, name=spend_label, mode="lines+markers",
        line=dict(color=ORANGE, width=2.5),
        marker=dict(size=7),
        hovertemplate=f"<b>{spend_label}</b><br>%{{x}}: %{{y:.2f}}<extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=years, y=outcome_vals, name=outcome_label, mode="lines+markers",
        yaxis="y2",
        line=dict(color=TEAL, width=2.5, dash="dot"),
        marker=dict(size=7),
        hovertemplate=f"<b>{outcome_label}</b><br>%{{x}}: %{{y:.1f}}<extra></extra>",
    ))
    fig.update_layout(
        title=dict(text=title, font=dict(color=TEXT_MAIN, size=14), x=0.01),
        paper_bgcolor=PLOTLY_PAPER,
        plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_MAIN),
        height=360,
        margin=dict(l=16, r=60, t=48, b=16),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=TEXT_MUTED),
                    orientation="h", y=-0.18),
        xaxis=dict(gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
        yaxis=dict(title=dict(text=spend_label, font=dict(color=ORANGE)),
                   gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
        yaxis2=dict(
            title=dict(text=outcome_label, font=dict(color=TEAL)),
            overlaying="y", side="right",
            tickfont=dict(color=TEAL),
            autorange="reversed" if invert_outcome else True,
            gridcolor="rgba(0,0,0,0)",
        ),
    )
    return fig

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    page_header(
        "📊",
        "Impact Correlator",
        "Does spending more actually help? Track health, education, infrastructure, and agricultural outcomes against budget allocations.",
    ),
    unsafe_allow_html=True,
)
st.markdown(
    insight_box(
        "⚠️ <b>Important:</b> These charts show <b>correlation</b>, not causation. "
        "India's social outcomes are shaped by many factors beyond just budget allocation — "
        "state-level spending, private sector, global trends, and time lags all matter."
    ),
    unsafe_allow_html=True,
)
st.markdown("---")

YEARS_COMMON = BUDGET_YEARS  # 2015-16 to 2024-25

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: Health
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown(
    "<div class='section-header'>🏥 Health Spending vs Outcomes</div>",
    unsafe_allow_html=True,
)

health_spend = [MINISTRY_ALLOCATIONS[y]["Health & Family Welfare"]["allocated"] for y in YEARS_COMMON]
imr_vals     = [INFANT_MORTALITY_RATE[y] for y in YEARS_COMMON]
mmr_vals     = [MATERNAL_MORTALITY_RATE[y] for y in YEARS_COMMON]
oop_vals     = [OUT_OF_POCKET_HEALTH_PCT[y] for y in YEARS_COMMON]
le_vals      = [LIFE_EXPECTANCY[y] for y in YEARS_COMMON]

tab1a, tab1b, tab1c = st.tabs([
    "Health Budget vs Infant Mortality",
    "Health Budget vs Out-of-Pocket Cost",
    "Scatter: Budget vs Life Expectancy",
])

with tab1a:
    fig = dual_axis_chart(
        YEARS_COMMON, health_spend, imr_vals,
        "Health Budget (₹ L cr)", "Infant Mortality Rate (per 1,000 births)",
        "Health Budget ↑ vs Infant Mortality ↓", invert_outcome=False,
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        insight_box(
            f"India's health budget grew from <b>₹0.33 L cr (2015-16)</b> to "
            f"<b>₹0.90 L cr (2024-25)</b> — a <b>2.7× increase</b>. "
            f"In the same period, the Infant Mortality Rate fell from <b>37 to ~20</b> "
            f"deaths per 1,000 live births. The trend is encouraging, though India still "
            f"lags behind the WHO benchmark of under 12."
        ),
        unsafe_allow_html=True,
    )

with tab1b:
    fig = dual_axis_chart(
        YEARS_COMMON, health_spend, oop_vals,
        "Health Budget (₹ L cr)", "Out-of-Pocket Cost (% of total health spend)",
        "Public Health Spending vs Out-of-Pocket Burden", invert_outcome=False,
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        insight_box(
            f"As public health spending increased, out-of-pocket costs fell from "
            f"<b>64.2%</b> (2015-16) to around <b>44.8%</b> (2024-25). "
            f"Schemes like <b>Ayushman Bharat (PM-JAY)</b>, launched in 2018, played a major role. "
            f"But 44.8% is still very high — the global average is around 20%."
        ),
        unsafe_allow_html=True,
    )

with tab1c:
    fig_sc = scatter_correlation(
        x_vals=health_spend, y_vals=le_vals, labels=YEARS_COMMON,
        x_label="Health Budget (₹ L cr)", y_label="Life Expectancy (years)",
        title="Health Spending vs Life Expectancy", trendline=True,
    )
    st.plotly_chart(fig_sc, use_container_width=True)
    st.markdown(
        insight_box(
            f"Life expectancy has risen from <b>68.3 years (2015-16)</b> to <b>~71.4 years</b> "
            f"as health spending increased. The trendline shows a positive correlation. "
            f"The 2020-21 outlier reflects the <b>COVID-19 impact on life expectancy</b>."
        ),
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: Education
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown(
    "<div class='section-header'>🎓 Education Spending vs Outcomes</div>",
    unsafe_allow_html=True,
)

edu_spend  = [MINISTRY_ALLOCATIONS[y]["Education"]["allocated"] for y in YEARS_COMMON]
lit_vals   = [LITERACY_RATE[y] for y in YEARS_COMMON]
ger_vals   = [GROSS_ENROLMENT_RATIO_HE[y] for y in YEARS_COMMON]
drop_vals  = [SCHOOL_DROPOUT_RATE[y] for y in YEARS_COMMON]

tab2a, tab2b, tab2c = st.tabs([
    "Budget vs Literacy Rate",
    "Budget vs Higher Education Enrolment",
    "Budget vs School Dropout Rate",
])

with tab2a:
    fig = dual_axis_chart(
        YEARS_COMMON, edu_spend, lit_vals,
        "Education Budget (₹ L cr)", "Literacy Rate (%)",
        "Education Spending vs Adult Literacy Rate",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        insight_box(
            f"India's literacy rate improved from <b>73.5%</b> to <b>~80%</b> over the decade "
            f"alongside higher education spending. However, the budget was ₹1.25 L cr in 2024-25 — "
            f"just <b>2.6% of the total budget</b>. The NEP 2020 target is 6% of GDP on education; "
            f"current public education spend (Centre + States) is about <b>4.3% of GDP</b>."
        ),
        unsafe_allow_html=True,
    )

with tab2b:
    fig = dual_axis_chart(
        YEARS_COMMON, edu_spend, ger_vals,
        "Education Budget (₹ L cr)", "Higher Education GER (%)",
        "Education Spending vs Gross Enrolment Ratio (Higher Ed)",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        insight_box(
            f"Gross Enrolment Ratio in Higher Education rose from <b>24.5%</b> (2015-16) "
            f"to <b>~30.8%</b> (2024-25). The NEP 2020 target is <b>50% by 2035</b>. "
            f"At the current pace, India needs to significantly accelerate spending and capacity."
        ),
        unsafe_allow_html=True,
    )

with tab2c:
    fig = dual_axis_chart(
        YEARS_COMMON, edu_spend, drop_vals,
        "Education Budget (₹ L cr)", "Secondary School Dropout Rate (%)",
        "Education Spending vs Dropout Rate",
        invert_outcome=False,
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        insight_box(
            f"School dropout rates at secondary level fell from <b>17.1%</b> to <b>~10%</b> "
            f"as education spending increased. But 10% still means millions of children "
            f"leaving school early — a challenge that money alone cannot solve (gender norms, "
            f"child labour, and infrastructure also matter)."
        ),
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: Infrastructure & Growth
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown(
    "<div class='section-header'>🛣️ Infrastructure Spending vs Economic Growth</div>",
    unsafe_allow_html=True,
)

roads_spend  = [MINISTRY_ALLOCATIONS[y]["Road Transport & Highways"]["allocated"] for y in YEARS_COMMON]
rail_spend   = [MINISTRY_ALLOCATIONS[y]["Railways"]["allocated"] for y in YEARS_COMMON]
gdp_growth   = [GDP_GROWTH_RATE[y] for y in YEARS_COMMON]
hw_km        = [HIGHWAY_LENGTH_KM[y] for y in YEARS_COMMON]
rail_elec    = [RAILWAY_ELECTRIFICATION[y] for y in YEARS_COMMON]

tab3a, tab3b, tab3c = st.tabs([
    "Roads Budget vs Highway Network",
    "Railways Budget vs Electrification",
    "Infrastructure vs GDP Growth",
])

with tab3a:
    fig = dual_axis_chart(
        YEARS_COMMON, roads_spend, hw_km,
        "Roads Budget (₹ L cr)", "National Highways (thousand km)",
        "Road Investment vs Highway Network Growth",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        insight_box(
            f"India's roads budget grew <b>6.6×</b> from ₹0.42 L cr to ₹2.78 L cr. "
            f"The national highway network expanded from <b>97,830 km → ~175,000 km</b>. "
            f"This is one of India's biggest infrastructure success stories — the <b>Bharatmala</b> "
            f"programme accelerated highway construction to <b>30+ km/day</b> from 2017 onwards."
        ),
        unsafe_allow_html=True,
    )

with tab3b:
    fig = dual_axis_chart(
        YEARS_COMMON, rail_spend, rail_elec,
        "Railways Budget (₹ L cr)", "Electrified Route (thousand km)",
        "Railway Investment vs Network Electrification",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        insight_box(
            f"Railways capital budget jumped <b>6.4×</b> from ₹0.40 L cr to ₹2.55 L cr. "
            f"Electrified route length more than doubled — from <b>22,200 km to 65,000+ km</b>. "
            f"India's <b>100% railway electrification</b> mission is near completion, cutting "
            f"diesel costs and carbon emissions significantly."
        ),
        unsafe_allow_html=True,
    )

with tab3c:
    # Combined infra spend
    combined_infra = [r + ra for r, ra in zip(roads_spend, rail_spend)]
    fig_sc = scatter_correlation(
        x_vals=combined_infra, y_vals=gdp_growth, labels=YEARS_COMMON,
        x_label="Roads + Railways Budget (₹ L cr)",
        y_label="Real GDP Growth (%)",
        title="Infrastructure Spending vs GDP Growth Rate",
    )
    st.plotly_chart(fig_sc, use_container_width=True)
    st.markdown(
        insight_box(
            f"The 2020-21 outlier (GDP: <b>-6.6%</b>) was caused by COVID-19, not infra spending. "
            f"Outside that anomaly, higher infrastructure spending broadly correlates with "
            f"stronger growth. Economists estimate every ₹1 of infra spending generates "
            f"<b>₹2.5–3 in economic output</b> over time via the multiplier effect."
        ),
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: Agriculture & Water
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown(
    "<div class='section-header'>🌾 Agriculture & Water Spending vs Outcomes</div>",
    unsafe_allow_html=True,
)

agri_spend   = [MINISTRY_ALLOCATIONS[y]["Agriculture & Allied"]["allocated"] for y in YEARS_COMMON]
water_spend  = [MINISTRY_ALLOCATIONS[y]["Jal Shakti / Water"]["allocated"] for y in YEARS_COMMON]
agri_growth  = [AGRI_GDP_GROWTH[y] for y in YEARS_COMMON]
tap_cov      = [TAP_WATER_COVERAGE[y] for y in YEARS_COMMON]
pmk_ben      = [PM_KISAN_BENEFICIARIES[y] for y in YEARS_COMMON]

tab4a, tab4b = st.tabs([
    "Water Budget vs Tap Water Coverage",
    "Agri Budget vs Agricultural Growth",
])

with tab4a:
    fig = dual_axis_chart(
        YEARS_COMMON, water_spend, tap_cov,
        "Jal Shakti Budget (₹ L cr)", "Households with Tap Water (%)",
        "Water Spending vs Tap Water Coverage (Jal Jeevan Mission)",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        insight_box(
            f"<b>Jal Jeevan Mission</b> (launched 2019) is arguably India's most impactful "
            f"recent welfare programme. Tap water coverage jumped from <b>31.5%</b> (2019-20) "
            f"to <b>91.3%</b> (2024-25) — connecting ~150 million homes in just 5 years. "
            f"The water budget grew 3.85× to fund this."
        ),
        unsafe_allow_html=True,
    )

with tab4b:
    fig = dual_axis_chart(
        YEARS_COMMON, agri_spend, agri_growth,
        "Agriculture Budget (₹ L cr)", "Agricultural GDP Growth (%)",
        "Agriculture Spending vs Farm Sector Growth",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        insight_box(
            f"Agricultural growth is highly <b>volatile</b> — driven more by monsoons than spending. "
            f"The 2016-17 spike (6.3% growth) followed a good monsoon after 2015-16's drought. "
            f"PM-KISAN (direct cash transfer) was launched in 2019 and now covers "
            f"<b>11 crore farmer families</b>, providing ₹6,000/year each."
        ),
        unsafe_allow_html=True,
    )

# ── Summary scorecard ─────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<div class='section-header'>📋 Impact Scorecard: 2015-16 → 2024-25</div>",
    unsafe_allow_html=True,
)

scorecard = [
    ("🏥 Infant Mortality Rate", "37", "~20", "↓ 46% improvement", TEAL),
    ("📚 Literacy Rate", "73.5%", "~80%", "↑ 6.5 ppt increase", TEAL),
    ("🛣️ Highway Network", "97,830 km", "175,000 km", "↑ 79% expansion", TEAL),
    ("💧 Tap Water Coverage", "16.8%", "91.3%", "↑ 74 ppt in 10 years", TEAL),
    ("🚂 Railway Electrification", "22,200 km", "65,000 km", "↑ 193% growth", TEAL),
    ("👶 Maternal Mortality", "130/lakh", "~75/lakh", "↓ 42% improvement", TEAL),
    ("🎓 Higher Ed GER", "24.5%", "~30.8%", "↑ 6.3 ppt increase", TEAL),
    ("💊 Out-of-Pocket Health", "64.2%", "~44.8%", "↓ 19.4 ppt reduction", TEAL),
]

cols_sc = st.columns(4)
for i, (indicator, before, after, change, color) in enumerate(scorecard):
    with cols_sc[i % 4]:
        st.markdown(
            f"""
            <div style='background:{NAVY_CARD}; border:1px solid {NAVY_LIGHT};
                        border-left:3px solid {color}; border-radius:10px;
                        padding:0.8rem; margin-bottom:0.6rem;'>
              <div style='font-size:0.75rem; color:{TEXT_MUTED};'>{indicator}</div>
              <div style='display:flex; justify-content:space-between; margin-top:0.3rem;'>
                <span style='color:#8B9CC7; font-size:0.82rem;'>{before}</span>
                <span style='color:{TEXT_MUTED};'>→</span>
                <span style='color:{BEIGE}; font-size:0.9rem; font-weight:600;'>{after}</span>
              </div>
              <div style='color:{color}; font-size:0.75rem; margin-top:0.3rem;
                          font-weight:600;'>{change}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(footer_html(), unsafe_allow_html=True)
