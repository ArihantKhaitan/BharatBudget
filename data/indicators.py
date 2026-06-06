# Socio-economic outcome indicators for India
# Sources: NFHS, MOSPI, World Bank, MoHFW, ASER Reports, MoRD
# Used in Impact Correlator page

# ── Health Indicators ─────────────────────────────────────────────────────────

# Infant Mortality Rate: deaths per 1,000 live births (SRS, MoHFW)
INFANT_MORTALITY_RATE = {
    "2015-16": 37,
    "2016-17": 34,
    "2017-18": 32,
    "2018-19": 30,
    "2019-20": 28,
    "2020-21": 28,   # COVID; minimal change
    "2021-22": 25,
    "2022-23": 23,
    "2023-24": 21,
    "2024-25": 20,   # projected
}

# Maternal Mortality Rate: deaths per 1,00,000 live births (SRS)
MATERNAL_MORTALITY_RATE = {
    "2015-16": 130,
    "2016-17": 122,
    "2017-18": 113,
    "2018-19": 103,
    "2019-20": 97,
    "2020-21": 97,
    "2021-22": 93,
    "2022-23": 86,
    "2023-24": 80,
    "2024-25": 75,
}

# Life Expectancy at birth (years, MOSPI)
LIFE_EXPECTANCY = {
    "2015-16": 68.3,
    "2016-17": 68.7,
    "2017-18": 69.2,
    "2018-19": 69.7,
    "2019-20": 70.0,
    "2020-21": 69.0,   # slight dip, COVID excess mortality
    "2021-22": 69.8,
    "2022-23": 70.5,
    "2023-24": 71.0,
    "2024-25": 71.4,
}

# Out-of-Pocket health expenditure as % of total health expenditure (NHA, MoHFW)
OUT_OF_POCKET_HEALTH_PCT = {
    "2015-16": 64.2,
    "2016-17": 62.6,
    "2017-18": 60.6,
    "2018-19": 58.7,
    "2019-20": 54.3,
    "2020-21": 52.1,
    "2021-22": 50.0,
    "2022-23": 48.3,
    "2023-24": 46.5,
    "2024-25": 44.8,
}

# ── Education Indicators ──────────────────────────────────────────────────────

# Adult Literacy Rate (%, ASER / Census projection)
LITERACY_RATE = {
    "2015-16": 73.5,
    "2016-17": 74.1,
    "2017-18": 74.8,
    "2018-19": 75.5,
    "2019-20": 76.2,
    "2020-21": 76.9,
    "2021-22": 77.7,
    "2022-23": 78.5,
    "2023-24": 79.2,
    "2024-25": 80.0,
}

# Gross Enrolment Ratio – Higher Education (%, AISHE, MoE)
GROSS_ENROLMENT_RATIO_HE = {
    "2015-16": 24.5,
    "2016-17": 25.2,
    "2017-18": 25.8,
    "2018-19": 26.3,
    "2019-20": 27.1,
    "2020-21": 27.3,
    "2021-22": 28.4,
    "2022-23": 29.4,
    "2023-24": 30.1,
    "2024-25": 30.8,
}

# School dropout rate – secondary level (%, UDISE+, MoE)
SCHOOL_DROPOUT_RATE = {
    "2015-16": 17.1,
    "2016-17": 16.5,
    "2017-18": 15.9,
    "2018-19": 15.0,
    "2019-20": 14.4,
    "2020-21": 13.8,
    "2021-22": 12.6,
    "2022-23": 11.4,
    "2023-24": 10.6,
    "2024-25": 10.0,
}

# ── Economic / Infrastructure Indicators ─────────────────────────────────────

# Real GDP growth rate (%, MOSPI)
GDP_GROWTH_RATE = {
    "2015-16": 8.0,
    "2016-17": 8.3,
    "2017-18": 6.8,
    "2018-19": 6.5,
    "2019-20": 4.0,
    "2020-21": -6.6,  # COVID contraction
    "2021-22": 8.7,
    "2022-23": 7.2,
    "2023-24": 8.2,
    "2024-25": 6.8,
}

# National Highway length (thousand km, MoRTH)
HIGHWAY_LENGTH_KM = {
    "2015-16": 97.83,
    "2016-17": 114.16,
    "2017-18": 132.50,
    "2018-19": 145.24,
    "2019-20": 132.50,   # revised classification
    "2020-21": 137.20,
    "2021-22": 145.16,
    "2022-23": 154.79,
    "2023-24": 163.29,
    "2024-25": 175.00,
}

# Electrified railway route km (thousand km, IR)
RAILWAY_ELECTRIFICATION = {
    "2015-16": 22.2,
    "2016-17": 24.8,
    "2017-18": 28.8,
    "2018-19": 33.4,
    "2019-20": 38.6,
    "2020-21": 46.1,
    "2021-22": 50.4,
    "2022-23": 57.0,
    "2023-24": 61.8,
    "2024-25": 65.0,
}

# ── Agriculture Indicators ────────────────────────────────────────────────────

# Agricultural GDP growth (%, MOSPI)
AGRI_GDP_GROWTH = {
    "2015-16": 0.6,
    "2016-17": 6.3,
    "2017-18": 6.3,
    "2018-19": 2.1,
    "2019-20": 4.0,
    "2020-21": 3.6,
    "2021-22": 3.3,
    "2022-23": 4.0,
    "2023-24": 1.4,
    "2024-25": 3.8,
}

# Farmers registered on PM-KISAN (crore, DBT portal) – 0 before launch in 2019
PM_KISAN_BENEFICIARIES = {
    "2015-16": 0.0,
    "2016-17": 0.0,
    "2017-18": 0.0,
    "2018-19": 0.0,
    "2019-20": 8.45,
    "2020-21": 10.23,
    "2021-22": 11.18,
    "2022-23": 11.40,
    "2023-24": 11.00,
    "2024-25": 11.00,
}

# ── Water & Sanitation ────────────────────────────────────────────────────────

# Households with tap water connection, % (Jal Jeevan Mission, MoJS)
TAP_WATER_COVERAGE = {
    "2015-16": 16.8,
    "2016-17": 18.4,
    "2017-18": 19.2,
    "2018-19": 23.5,
    "2019-20": 31.5,
    "2020-21": 43.8,
    "2021-22": 58.1,
    "2022-23": 72.4,
    "2023-24": 85.7,
    "2024-25": 91.3,
}

# Open Defecation Free (ODF) villages, % (SBM, MoJS)
ODF_COVERAGE = {
    "2015-16": 42.0,
    "2016-17": 57.0,
    "2017-18": 75.0,
    "2018-19": 95.0,
    "2019-20": 100.0,
    "2020-21": 100.0,
    "2021-22": 100.0,
    "2022-23": 100.0,
    "2023-24": 100.0,
    "2024-25": 100.0,
}
