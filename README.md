# 🇮🇳 BharatBudget — India's Public Finance Tracker

> _Built with public data for public good._

A clean, interactive Streamlit dashboard that makes India's Union Budget data explorable and understandable for every citizen — no economics degree required.

---

## ✨ Features

| Page | What it does |
|------|-------------|
| **🏠 Home** | Overview, 10-year budget growth chart, key milestones |
| **🔍 Budget Explorer** | Ministry-wise treemap + bar chart for any year (2015-16 to 2024-25), allocated vs actual toggle |
| **💸 Follow the Money** | Multi-year trend lines, priority ratios ("Defence vs Education"), YoY % change deep-dives |
| **📊 Impact Correlator** | Spending vs outcomes: infant mortality, literacy, highway km, water coverage, GDP growth |
| **🗺️ State Finance Tracker** | Per-capita transfers, bubble map of India, Finance Commission devolution shares, state table |

---

## 🚀 Quick Start

```bash
# 1. Clone / navigate to the project
cd BharatBudget

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## 📁 File Structure

```
BharatBudget/
├── app.py                          ← Home page (entry point)
├── pages/
│   ├── 1_🔍_Budget_Explorer.py
│   ├── 2_💸_Follow_the_Money.py
│   ├── 3_📊_Impact_Correlator.py
│   └── 4_🗺️_State_Finance_Tracker.py
├── data/
│   ├── budget_data.py              ← Union Budget allocations (2015-16 → 2024-25)
│   ├── indicators.py               ← Health, education, infrastructure indicators
│   └── states.py                   ← State-wise central transfers & metadata
├── components/
│   └── charts.py                   ← Reusable Plotly chart functions
├── utils/
│   └── styling.py                  ← CSS theme, colour palette, layout helpers
├── .streamlit/
│   └── config.toml                 ← Dark navy + orange theme
└── requirements.txt
```

---

## 🔄 How to Update with Real Data

The sample data is structured so real CSVs can replace it with minimal changes.

### Budget allocation data (`data/budget_data.py`)

Replace `MINISTRY_ALLOCATIONS` with data from the Union Budget documents:

1. Download the **Statement of Budget Estimates** (Annex 1) from [indiabudget.gov.in](https://indiabudget.gov.in)
2. For each year, populate:
   ```python
   MINISTRY_ALLOCATIONS["YYYY-YY"] = {
       "Ministry Name": {"allocated": X.XX, "actual": Y.YY},
       ...
   }
   ```
3. Update `TOTAL_BUDGET["YYYY-YY"]` and `NOMINAL_GDP["YYYY-YY"]`

Alternatively, drop a CSV at `data/budget_raw.csv` with columns:
`year, ministry, allocated_lcr, actual_lcr`
and replace the dict reads with `pd.read_csv("data/budget_raw.csv")`.

### Outcome indicators (`data/indicators.py`)

| Indicator | Source | URL |
|-----------|--------|-----|
| Infant / Maternal Mortality | Sample Registration System (SRS) | [censusindia.gov.in](https://censusindia.gov.in) |
| Literacy / Enrolment | AISHE, UDISE+ | [aishe.gov.in](https://aishe.gov.in) |
| GDP Growth | MOSPI National Accounts | [mospi.gov.in](https://mospi.gov.in) |
| Highway km | MoRTH Annual Report | [morth.nic.in](https://morth.nic.in) |
| Tap water coverage | JJM Dashboard | [jaljeevanmission.gov.in](https://jaljeevanmission.gov.in) |

### State transfer data (`data/states.py`)

Download **State-wise Central Transfers** from RBI's State Finances report:
[rbi.org.in → Publications → State Finances: A Study of Budgets](https://rbi.org.in)

Update `PER_CAPITA_TRANSFER_2023_24` and `TOTAL_TRANSFERS_BY_YEAR` directly, or load from CSV.

---

## 📊 Data Sources

| Source | URL | What it covers |
|--------|-----|----------------|
| Union Budget documents | [indiabudget.gov.in](https://indiabudget.gov.in) | Ministry-wise allocations & actuals |
| Open Government Data | [data.gov.in](https://data.gov.in) | Multiple datasets |
| RBI DBIE | [dbie.rbi.org.in](https://dbie.rbi.org.in) | State finances, macro data |
| MOSPI | [mospi.gov.in](https://mospi.gov.in) | GDP, National Accounts |
| Finance Commission XV | [fincom15.gov.in](https://fincom15.gov.in) | Devolution formula & shares |
| Ministry of Health (MoHFW) | [mohfw.gov.in](https://mohfw.gov.in) | Health indicators |
| Ministry of Education | [education.gov.in](https://education.gov.in) | AISHE, UDISE+ |
| MoRTH | [morth.nic.in](https://morth.nic.in) | Highway network data |
| Jal Jeevan Mission | [jaljeevanmission.gov.in](https://jaljeevanmission.gov.in) | Water coverage |

---

## 🎨 Design

- **Colour scheme:** Dark navy (`#0B1437`) + saffron orange (`#FF9933`) — inspired by India's national flag, modernised for a dashboard context
- **Charts:** Plotly (interactive, hover-enabled)
- **Figures:** All monetary values in **Lakh Crore (₹ L cr)** = ₹1,00,000 crore = ₹1 trillion

---

## 📝 Notes on Data Accuracy

All figures are based on publicly available Union Budget documents and official government reports. Small discrepancies from official totals may exist due to rounding or supplementary demand adjustments. For **2024-25**, actual expenditure is not yet finalized — only allocated figures are shown.

---

_Built with public data for public good · BharatBudget 2025_
