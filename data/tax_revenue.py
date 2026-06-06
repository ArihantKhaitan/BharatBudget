"""
Tax revenue data for India — Union Budget 2015-16 to 2024-25.
Sources: Union Budget statements, CGA, RBI Handbook of Statistics.
All values in ₹ Lakh Crore unless noted.
"""

BUDGET_YEARS = [
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25",
]

# Gross Tax Revenue collected by Centre (actuals; 2024-25 = revised estimate)
GROSS_TAX_REVENUE = {
    "2015-16": 14.55,
    "2016-17": 17.15,
    "2017-18": 19.19,
    "2018-19": 20.80,
    "2019-20": 20.10,
    "2020-21": 20.27,
    "2021-22": 27.07,
    "2022-23": 30.43,
    "2023-24": 34.37,
    "2024-25": 38.40,
}

# Corporation Tax (profit tax on companies)
CORPORATION_TAX = {
    "2015-16": 4.54,
    "2016-17": 4.83,
    "2017-18": 5.71,
    "2018-19": 6.64,
    "2019-20": 5.56,   # corp tax rate cut Sep 2019
    "2020-21": 4.57,
    "2021-22": 7.12,
    "2022-23": 8.25,
    "2023-24": 9.11,
    "2024-25": 10.20,
}

# Personal Income Tax (individuals, HUFs)
INCOME_TAX = {
    "2015-16": 2.87,
    "2016-17": 3.53,
    "2017-18": 4.30,
    "2018-19": 4.72,
    "2019-20": 5.14,
    "2020-21": 4.69,
    "2021-22": 6.96,
    "2022-23": 8.33,
    "2023-24": 10.22,
    "2024-25": 11.87,
}

# GST — Centre's share (CGST + Centre's 50% of IGST). Pre-GST era: None.
# GST launched 1 July 2017; 2017-18 is partial year Centre share.
GST_CENTRE_SHARE = {
    "2015-16": None,
    "2016-17": None,
    "2017-18": 2.63,
    "2018-19": 4.58,
    "2019-20": 4.72,
    "2020-21": 4.34,
    "2021-22": 5.90,
    "2022-23": 7.21,
    "2023-24": 8.11,
    "2024-25": 9.00,
}

# Customs Duty
CUSTOMS_DUTY = {
    "2015-16": 2.10,
    "2016-17": 2.26,
    "2017-18": 2.30,
    "2018-19": 1.30,
    "2019-20": 1.09,
    "2020-21": 1.33,
    "2021-22": 1.99,
    "2022-23": 2.13,
    "2023-24": 2.33,
    "2024-25": 2.41,
}

# Union Excise Duty (petroleum, tobacco — shrinks post-GST but
# petroleum still outside GST)
EXCISE_DUTY = {
    "2015-16": 2.80,
    "2016-17": 3.84,
    "2017-18": 2.58,
    "2018-19": 2.31,
    "2019-20": 2.39,
    "2020-21": 3.91,   # fuel cess raised during COVID
    "2021-22": 3.94,
    "2022-23": 3.31,
    "2023-24": 3.02,
    "2024-25": 2.85,
}

# Tax devolved to states under FC XV (approx 41% of gross)
TAX_DEVOLVED_TO_STATES = {
    "2015-16": 5.09,
    "2016-17": 6.08,
    "2017-18": 6.74,
    "2018-19": 7.64,
    "2019-20": 6.61,
    "2020-21": 5.50,
    "2021-22": 8.17,
    "2022-23": 9.49,
    "2023-24": 12.19,
    "2024-25": 12.47,
}

# State-wise GST contribution FY 2023-24 (₹ Thousand Crore, approx)
STATE_GST_CONTRIBUTION_2023_24 = {
    "Maharashtra":     165.0,
    "Karnataka":        90.0,
    "Gujarat":          80.0,
    "Tamil Nadu":       78.0,
    "Uttar Pradesh":    72.0,
    "Delhi":            60.0,
    "Haryana":          52.0,
    "Rajasthan":        48.0,
    "Andhra Pradesh":   42.0,
    "Telangana":        40.0,
    "West Bengal":      38.0,
    "Madhya Pradesh":   35.0,
    "Odisha":           28.0,
    "Punjab":           24.0,
    "Kerala":           22.0,
    "Bihar":            18.0,
    "Jharkhand":        14.0,
    "Assam":            12.0,
    "Chhattisgarh":     11.0,
    "Uttarakhand":       9.0,
}

# Tax non-filer / compliance gap (% of estimated eligible taxpayers who filed)
FILING_COMPLIANCE_PCT = {
    "2015-16": 51.0,
    "2016-17": 53.0,
    "2017-18": 58.0,
    "2018-19": 63.0,
    "2019-20": 66.0,
    "2020-21": 68.0,
    "2021-22": 72.0,
    "2022-23": 76.0,
    "2023-24": 80.0,
    "2024-25": 82.0,
}

# Number of ITR filers (crore)
ITR_FILERS_CR = {
    "2015-16": 3.7,
    "2016-17": 4.2,
    "2017-18": 5.3,
    "2018-19": 5.9,
    "2019-20": 6.5,
    "2020-21": 6.7,
    "2021-22": 7.3,
    "2022-23": 7.7,
    "2023-24": 8.2,
    "2024-25": 8.9,
}
