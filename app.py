"""BharatBudget — entry point.

Run with: streamlit run app.py
"""

import streamlit as st
from utils.styling import GLOBAL_CSS, ORANGE, TEXT_MUTED, BG_SURFACE, BORDER

st.set_page_config(
    page_title="BharatBudget — India's Public Finance Tracker",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject global CSS once — applies to every page
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# Fixed top-right brand badge (visible on every page)
st.markdown(
    f"""
    <div id="bb-brand">
      <span style="font-size:1.05rem; line-height:1;">🇮🇳</span>
      <div style="line-height:1.15;">
        <div style="font-family:'Playfair Display',Georgia,serif;
                    font-size:0.82rem; font-weight:700; color:{ORANGE};">BharatBudget</div>
        <div style="font-family:'DM Sans',sans-serif; font-size:0.47rem; font-weight:700;
                    letter-spacing:0.1em; text-transform:uppercase; color:{TEXT_MUTED};">Public Finance Tracker</div>
      </div>
    </div>
    <style>
    #bb-brand {{
      position: fixed;
      top: 0.55rem;
      right: 1.1rem;
      z-index: 9998;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(250,246,236,0.96);
      border: 1px solid {BORDER};
      border-radius: 999px;
      padding: 0.3rem 0.9rem 0.3rem 0.55rem;
      box-shadow: 0 2px 14px rgba(0,0,0,0.08);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      pointer-events: none;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

pg = st.navigation([
    st.Page("home_page.py",                              title="BharatBudget",         icon="🇮🇳", default=True),
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
