"""
Constituency and MPLADS (MP Local Area Development Scheme) data.
Sources: loksabha.nic.in, Ministry of Statistics, PIB.
Each MP gets ₹5 crore/year. 543 Lok Sabha + 245 Rajya Sabha = 788 MPs.
"""

# MPLADS annual total allocation (₹ crore)
# Note: MPLADS was suspended in 2020-21 and 2021-22 due to COVID-19
MPLADS_TOTAL_ALLOCATION_CR = {
    "2015-16": 3940,
    "2016-17": 3940,
    "2017-18": 3940,
    "2018-19": 3940,
    "2019-20": 3940,
    "2020-21": 0,      # suspended — funds diverted to PM CARES
    "2021-22": 0,      # suspended
    "2022-23": 3940,
    "2023-24": 3940,
    "2024-25": 3940,
}

# MPLADS utilization rate by state FY 2023-24 (%, higher = better)
STATE_MPLADS_UTILIZATION_2023_24 = {
    "Gujarat":          94.2,
    "Himachal Pradesh": 92.8,
    "Haryana":          91.5,
    "Tamil Nadu":       90.3,
    "Karnataka":        89.1,
    "Maharashtra":      88.4,
    "Kerala":           87.6,
    "Uttarakhand":      86.9,
    "Andhra Pradesh":   85.2,
    "Telangana":        84.8,
    "Rajasthan":        83.5,
    "Madhya Pradesh":   82.1,
    "Punjab":           81.6,
    "Odisha":           80.4,
    "Chhattisgarh":     79.8,
    "West Bengal":      78.2,
    "Uttar Pradesh":    76.5,
    "Bihar":            74.1,
    "Assam":            72.3,
    "Jharkhand":        70.8,
    "Manipur":          68.4,
    "Tripura":          67.2,
    "Nagaland":         64.5,
    "Meghalaya":        62.8,
    "Arunachal Pradesh":61.4,
    "Sikkim":           88.0,
    "Mizoram":          63.0,
    "Jammu & Kashmir":  78.5,
    "Goa":              91.0,
    "Delhi":            85.0,
}

# State-wise MPLADS allocation FY 2023-24 (₹ crore) = LS MPs × 5 cr
# (excludes Rajya Sabha for simplicity)
STATE_MPLADS_ALLOCATION_2023_24 = {
    "Uttar Pradesh":    400,   # 80 LS seats
    "Maharashtra":      240,   # 48
    "West Bengal":      210,   # 42
    "Bihar":            200,   # 40
    "Tamil Nadu":       195,   # 39
    "Madhya Pradesh":   175,   # 29
    "Rajasthan":        150,   # 25
    "Karnataka":        145,   # 28
    "Gujarat":          130,   # 26
    "Andhra Pradesh":   125,   # 25
    "Odisha":           105,   # 21
    "Kerala":           100,   # 20
    "Assam":             70,   # 14
    "Jharkhand":         65,   # 14 (est)
    "Chhattisgarh":      55,   # 11
    "Haryana":           55,   # 10
    "Punjab":            65,   # 13
    "Telangana":         85,   # 17
    "Uttarakhand":       25,   # 5
    "Himachal Pradesh":  25,   # 4
    "Delhi":             35,   # 7
    "Jammu & Kashmir":   25,   # 5
    "Manipur":           10,   # 2
    "Meghalaya":         10,   # 2
    "Goa":               10,   # 2
    "Tripura":           10,   # 2
    "Nagaland":           5,   # 1
    "Arunachal Pradesh":  5,   # 2
    "Mizoram":            5,   # 1
    "Sikkim":             5,   # 1
}

# Constituency-level development index (composite, 0-100; based on HDI,
# access to infrastructure, and fund utilization)
# Sample data for illustrative top/bottom constituencies
TOP_DEVELOPED_CONSTITUENCIES = [
    {"constituency": "Gandhinagar", "state": "Gujarat",      "index": 82.4},
    {"constituency": "Pune",        "state": "Maharashtra",  "index": 81.8},
    {"constituency": "Bengaluru S", "state": "Karnataka",    "index": 81.2},
    {"constituency": "Chennai N",   "state": "Tamil Nadu",   "index": 80.7},
    {"constituency": "Gurugram",    "state": "Haryana",      "index": 79.5},
    {"constituency": "Surat",       "state": "Gujarat",      "index": 78.9},
    {"constituency": "Hyderabad",   "state": "Telangana",    "index": 78.4},
    {"constituency": "Chandigarh",  "state": "Punjab",       "index": 77.6},
    {"constituency": "Kochi",       "state": "Kerala",       "index": 76.8},
    {"constituency": "Mumbai NW",   "state": "Maharashtra",  "index": 76.2},
]

LEAST_DEVELOPED_CONSTITUENCIES = [
    {"constituency": "Araria",       "state": "Bihar",       "index": 28.4},
    {"constituency": "Kishanganj",   "state": "Bihar",       "index": 29.1},
    {"constituency": "Shivhar",      "state": "Bihar",       "index": 30.2},
    {"constituency": "Sitamarhi",    "state": "Bihar",       "index": 31.5},
    {"constituency": "Khagaria",     "state": "Bihar",       "index": 32.8},
    {"constituency": "Darbhanga",    "state": "Bihar",       "index": 33.6},
    {"constituency": "Bahraich",     "state": "Uttar Pradesh","index": 34.2},
    {"constituency": "Balrampur",    "state": "Uttar Pradesh","index": 35.0},
    {"constituency": "Shrawasti",    "state": "Uttar Pradesh","index": 35.8},
    {"constituency": "Tribeni",      "state": "Tripura",     "index": 36.4},
]

# Type of work done under MPLADS (% split, FY 2023-24)
MPLADS_WORK_CATEGORY_PCT = {
    "Drinking Water & Sanitation": 18.5,
    "Roads & Bridges":             22.4,
    "Education Infrastructure":    15.8,
    "Health Facilities":           12.3,
    "Community Halls & Buildings": 10.2,
    "Flood & Erosion Control":      7.6,
    "Sports & Recreation":          5.8,
    "Electricity & Solar":          4.2,
    "Other":                        3.2,
}

# Number of LS seats per state (for reference)
LS_SEATS_PER_STATE = {
    "Uttar Pradesh": 80, "Maharashtra": 48, "West Bengal": 42,
    "Bihar": 40, "Tamil Nadu": 39, "Madhya Pradesh": 29,
    "Karnataka": 28, "Rajasthan": 25, "Andhra Pradesh": 25,
    "Gujarat": 26, "Odisha": 21, "Kerala": 20, "Telangana": 17,
    "Assam": 14, "Jharkhand": 14, "Chhattisgarh": 11,
    "Punjab": 13, "Haryana": 10, "Delhi": 7, "Uttarakhand": 5,
    "Jammu & Kashmir": 5, "Himachal Pradesh": 4, "Goa": 2,
    "Manipur": 2, "Tripura": 2, "Meghalaya": 2, "Arunachal Pradesh": 2,
    "Nagaland": 1, "Mizoram": 1, "Sikkim": 1,
}
