# BharatBudget

India's public finance tracker — Union Budget data from 2015-16 to 2024-25, built with Streamlit.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Requires Python 3.9+. Opens at `http://localhost:8501`.

---

## Pages

| Page | File | What it shows |
|------|------|---------------|
| Home | `home_page.py` | Budget overview, top ministry allocations, 10-year milestones |
| Budget Explorer | `pages/1_🔍_Budget_Explorer.py` | Ministry-wise allocation and YoY changes, 2015–2025 |
| Follow the Money | `pages/2_💸_Follow_the_Money.py` | Expenditure breakdown — capital vs revenue, ministry deep-dive |
| Impact Correlator | `pages/3_📊_Impact_Correlator.py` | Spending vs outcomes — HDI, literacy, infant mortality |
| State Finance Tracker | `pages/4_🗺️_State_Finance_Tracker.py` | State-level fiscal data and central transfers |
| Tax Revenue | `pages/5_💰_Tax_Revenue.py` | GST, income tax, corporate tax, customs — trends and state breakdown |
| Scheme Tracker | `pages/6_🏗️_Scheme_Tracker.py` | PM-KISAN, MGNREGA, Jal Jeevan, PMAY — beneficiaries and spend |
| Fiscal Health | `pages/7_📉_Fiscal_Health.py` | Fiscal deficit, revenue deficit, interest burden, debt trajectory |
| Procurement | `pages/8_🏛️_Procurement.py` | GeM marketplace — orders, top categories, state-wise contracts |
| Constituency Funds | `pages/9_🗳️_Constituency_Funds.py` | MPLADS — MP fund allocation and utilisation by state |

---

## Project structure

```
BharatBudget/
├── app.py                  # Entry point — page config + st.navigation
├── home_page.py            # Home page
├── pages/                  # One file per page
├── data/
│   ├── budget_data.py      # Ministry allocations, total budget, nominal GDP (₹ L cr)
│   ├── tax_revenue.py      # GST, income tax, corporate tax, ITR filers
│   ├── fiscal.py           # Fiscal deficit, revenue deficit, debt, interest payments
│   ├── schemes.py          # PM-KISAN, MGNREGA, PMAY, Jal Jeevan beneficiary data
│   ├── procurement.py      # GeM orders (₹ Th cr), sellers, MSME share, state contracts
│   ├── constituencies.py   # MPLADS fund data by state
│   ├── states.py           # State-level fiscal and transfer data
│   └── indicators.py       # HDI, literacy, health outcome indicators
├── utils/
│   └── styling.py          # Global CSS string, colour tokens, page_header/insight_box helpers
└── components/
    └── charts.py           # Shared Plotly chart helpers
```

All monetary values are in **₹ Lakh Crore** unless noted otherwise.  
GeM (Procurement) data is in **₹ Thousand Crore**. MPLADS data is in **₹ Crore**.

---

## Data sources

| Source | What it covers |
|--------|---------------|
| [Union Budget documents](https://www.indiabudget.gov.in/) | Ministry-wise expenditure statements |
| [RBI Handbook of Statistics](https://rbi.org.in/) | Fiscal deficit, debt, GDP |
| [GSTN / GST Council](https://www.gst.gov.in/) | GST collections by state |
| [GeM Portal](https://gem.gov.in/) | Government procurement order data |
| [MOSPI](https://mospi.gov.in/) | National accounts, economic indicators |
| [MPLADS Ministry](https://mplads.gov.in/) | Constituency fund releases and utilisation |

---

## Tech stack

- **Streamlit 1.49** — multipage app via `st.navigation()`
- **Plotly** — all charts
- **Pandas** — data wrangling
- Custom CSS theme via `st.markdown(GLOBAL_CSS, unsafe_allow_html=True)` in `utils/styling.py`
