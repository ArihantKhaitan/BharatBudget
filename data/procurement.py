"""
Government procurement data — GeM (Govt e-Marketplace) and major tenders.
Sources: gem.gov.in annual reports, Finance Ministry data, PIB.
"""

BUDGET_YEARS = [
    "2016-17", "2017-18", "2018-19", "2019-20", "2020-21",
    "2021-22", "2022-23", "2023-24", "2024-25",
]

# GeM total orders value (₹ Thousand Crore)
GEM_ORDERS_TCR = {
    "2016-17": 0.02,
    "2017-18": 0.18,
    "2018-19": 0.52,
    "2019-20": 0.98,
    "2020-21": 2.05,
    "2021-22": 5.01,
    "2022-23": 8.32,
    "2023-24": 13.16,
    "2024-25": 17.42,
}

# GeM registered sellers (lakh)
GEM_SELLERS_LAKH = {
    "2016-17": 0.02,
    "2017-18": 0.08,
    "2018-19": 0.20,
    "2019-20": 0.55,
    "2020-21": 1.24,
    "2021-22": 3.80,
    "2022-23": 6.20,
    "2023-24": 9.50,
    "2024-25": 11.80,
}

# GeM registered buyers (government organisations, thousand)
GEM_BUYERS_K = {
    "2016-17": 0.5,
    "2017-18": 2.1,
    "2018-19": 5.4,
    "2019-20": 10.2,
    "2020-21": 21.0,
    "2021-22": 45.0,
    "2022-23": 62.0,
    "2023-24": 75.0,
    "2024-25": 82.0,
}

# Top procurement categories FY 2023-24 (₹ Thousand Crore)
GEM_CATEGORIES_2023_24 = {
    "IT Hardware & Software": 2.80,
    "Office Supplies & Furniture": 2.20,
    "Healthcare Equipment": 1.80,
    "Vehicles & Transport": 1.40,
    "Electrical Equipment": 1.20,
    "Uniforms & PPE": 0.80,
    "Construction Material": 0.72,
    "Scientific Equipment": 0.54,
    "Agricultural Inputs": 0.48,
    "Printing & Stationery": 0.42,
    "Food & Canteen Supplies": 0.38,
    "Safety & Security Equipment": 0.30,
}

# State-wise GeM procurement value FY 2023-24 (₹ Thousand Crore)
STATE_GEM_PROCUREMENT_2023_24 = {
    "Uttar Pradesh": 1.85,
    "Maharashtra": 1.62,
    "Madhya Pradesh": 1.24,
    "Rajasthan": 1.18,
    "Karnataka": 1.05,
    "West Bengal": 0.92,
    "Tamil Nadu": 0.88,
    "Gujarat": 0.82,
    "Bihar": 0.76,
    "Andhra Pradesh": 0.65,
    "Odisha": 0.58,
    "Haryana": 0.54,
    "Jharkhand": 0.46,
    "Kerala": 0.42,
    "Telangana": 0.40,
    "Chhattisgarh": 0.38,
    "Assam": 0.35,
    "Punjab": 0.30,
    "Uttarakhand": 0.18,
    "Himachal Pradesh": 0.14,
}

# Major infrastructure contracts announced (indicative, ₹ Thousand Crore)
# Source: NITI Aayog, Ministry annual reports, PIB
MAJOR_CONTRACTS_BY_SECTOR = {
    "National Highways (NHAI)": 6.50,
    "Railways (new lines+electrification)": 5.20,
    "Urban Metro Projects": 2.80,
    "Defence Procurement (domestic)": 2.40,
    "Ports & Shipping": 1.80,
    "Airport Development (AAI+PPP)": 1.60,
    "Rural Roads (PMGSY)": 1.40,
    "Power Transmission (PGCIL)": 1.20,
    "Smart City Projects": 0.90,
    "Irrigation (PMKSY)": 0.80,
}

# % of GeM orders going to MSMEs
GEM_MSME_PCT = {
    "2019-20": 55, "2020-21": 58, "2021-22": 60,
    "2022-23": 61, "2023-24": 62, "2024-25": 63,
}

# % of GeM orders going to women-owned enterprises
GEM_WOMEN_ENTERPRISES_PCT = {
    "2019-20": 7, "2020-21": 10, "2021-22": 13,
    "2022-23": 16, "2023-24": 20, "2024-25": 22,
}
