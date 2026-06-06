"""BharatBudget — entry point.

Run with: streamlit run app.py
"""

import streamlit as st
from utils.styling import GLOBAL_CSS

st.set_page_config(
    page_title="BharatBudget — India's Public Finance Tracker",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject global CSS once — applies to every page
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

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
