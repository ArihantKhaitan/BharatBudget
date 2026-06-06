"""BharatBudget — entry point.

Run with: streamlit run app.py
"""

import streamlit as st
from utils.styling import (
    GLOBAL_CSS, ORANGE, TEXT_MUTED, TEXT_SEC, BORDER, BG_ELEVATED,
)

st.set_page_config(
    page_title="BharatBudget — India's Public Finance Tracker",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Inject global CSS once — applies to every page
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Sidebar header (andrewlu0 style) — appears above nav links ────────────────
with st.sidebar:
    st.markdown(
        f"""
        <div class="bb-sidebar-header" style="
          padding: 1.4rem 1.2rem 1.1rem;
          border-bottom: 1px solid {BORDER};
          margin-bottom: 0.2rem;
        ">
          <div style="
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 1.18rem;
            font-weight: 700;
            color: {ORANGE};
            letter-spacing: -0.03em;
            line-height: 1;
            margin-bottom: 0.28rem;
          ">BharatBudget</div>
          <div style="
            font-family: 'DM Sans', sans-serif;
            font-size: 0.6rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: {TEXT_MUTED};
          ">Public Finance Tracker</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

pg = st.navigation([
    st.Page("home_page.py",                              title="BharatBudget",         icon="🏠", default=True),
    st.Page("pages/1_🔍_Budget_Explorer.py",             title="Budget Explorer",       icon="🔍"),
    st.Page("pages/2_💸_Follow_the_Money.py",            title="Follow the Money",      icon="💸"),
    st.Page("pages/3_📊_Impact_Correlator.py",           title="Impact Correlator",     icon="📊"),
    st.Page("pages/4_🗺️_State_Finance_Tracker.py",      title="State Finance Tracker", icon="🗺️"),
    st.Page("pages/5_💰_Tax_Revenue.py",                 title="Tax Revenue",           icon="💰"),
    st.Page("pages/6_🏗️_Scheme_Tracker.py",             title="Scheme Tracker",        icon="🏗️"),
    st.Page("pages/7_📉_Fiscal_Health.py",               title="Fiscal Health",         icon="📉"),
    st.Page("pages/8_🏛️_Procurement.py",                title="Procurement",           icon="🏛️"),
    st.Page("pages/9_🗳️_Constituency_Funds.py",         title="Constituency Funds",    icon="🗳️"),
])
pg.run()
