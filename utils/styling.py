"""Premium warm-beige theme for BharatBudget."""

# ── Colour palette (warm beige / Indian parchment) ────────────────────────────
BG_PRIMARY   = "#F5EDD8"   # warm parchment
BG_SURFACE   = "#FFFFFF"   # white cards
BG_ELEVATED  = "#EDE3CA"   # deeper parchment
BORDER       = "#D4C9B0"   # warm tan border
BORDER_GLOW  = "#C4520040"

ORANGE       = "#C45000"   # deep saffron
ORANGE_LIGHT = "#E06820"   # medium saffron
ORANGE_DIM   = "#C450000C"

TEAL         = "#006652"
RED          = "#A42E2E"
BLUE_SOFT    = "#2B5FA0"

TEXT_PRIMARY = "#1A0E06"
TEXT_SEC     = "#5A4530"
TEXT_MUTED   = "#8A7360"

PLOTLY_PAPER = "#F5EDD8"
PLOTLY_PLOT  = "#FFFFFF"
GRID_COLOR   = "#DDD5BE"

# Legacy aliases (keep old imports working)
BEIGE        = TEXT_PRIMARY
BEIGE_MUTED  = TEXT_SEC
BEIGE_DIM    = TEXT_MUTED
WHITE        = "#FFFFFF"
NAVY         = BG_PRIMARY
NAVY_CARD    = BG_SURFACE
NAVY_LIGHT   = BORDER
TEXT_MAIN    = TEXT_PRIMARY
BG_CARD      = BG_SURFACE
BG_RAISED    = BG_ELEVATED
PLOTLY_PAPER_BG = PLOTLY_PAPER
PLOTLY_PLOT_BG  = PLOTLY_PLOT

MINISTRY_COLOR_MAP = {
    "Defence":                   "#C0392B",
    "Interest Payments":         "#8A7360",
    "Road Transport & Highways": "#C45000",
    "Railways":                  "#E07030",
    "Rural Development":         "#006652",
    "Home Affairs":              "#B03030",
    "Education":                 "#2B5FA0",
    "Agriculture & Allied":      "#3A7D3A",
    "Health & Family Welfare":   "#7B3A9E",
    "Communications & IT":       "#1A6EA8",
    "Jal Shakti / Water":        "#0A7A9A",
    "Housing & Urban Affairs":   "#9A7000",
    "Food & Public Distribution":"#4A8C4A",
    "Fertiliser Subsidy":        "#5A9050",
    "Science & Space":           "#6A2E9A",
    "Social Welfare":            "#A83060",
    "State Transfers (CSS)":     "#1A8A7A",
    "Others":                    "#7A7060",
}

CATEGORY_COLORS = {
    "Security & Governance": "#C0392B",
    "Infrastructure":        "#C45000",
    "Social":                "#006652",
    "Economy & Agriculture": "#2B5FA0",
    "Transfers & Others":    "#7A7060",
}


def get_plotly_layout(title: str = "", height: int = 420) -> dict:
    return dict(
        title=dict(
            text=title,
            font=dict(color=TEXT_PRIMARY, size=13, family="DM Sans, sans-serif"),
            x=0.02,
        ),
        paper_bgcolor=PLOTLY_PAPER,
        plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
        height=height,
        margin=dict(l=16, r=16, t=44, b=16),
        legend=dict(
            bgcolor="rgba(245,237,216,0.9)",
            bordercolor=BORDER,
            borderwidth=1,
            font=dict(color=TEXT_SEC, size=11),
        ),
        xaxis=dict(
            gridcolor=GRID_COLOR,
            linecolor=BORDER,
            tickfont=dict(color=TEXT_SEC),
            title_font=dict(color=TEXT_SEC),
            zeroline=False,
        ),
        yaxis=dict(
            gridcolor=GRID_COLOR,
            linecolor=BORDER,
            tickfont=dict(color=TEXT_SEC),
            title_font=dict(color=TEXT_SEC),
            zeroline=False,
        ),
    )


GLOBAL_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600&family=JetBrains+Mono:wght@400;500&display=swap');

@keyframes fadeUp {{
  from {{ opacity: 0; transform: translateY(18px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes pulseGlow {{
  0%, 100% {{ box-shadow: 0 1px 4px rgba(196,80,0,0.07), 0 2px 8px rgba(0,0,0,0.04); }}
  50%       {{ box-shadow: 0 2px 20px rgba(196,80,0,0.16), 0 4px 16px rgba(0,0,0,0.07); }}
}}
@keyframes shimmer {{
  0%   {{ background-position: -200% 0; }}
  100% {{ background-position:  200% 0; }}
}}

*, *::before, *::after {{ box-sizing: border-box; }}

.stApp, .main {{
  background-color: {BG_PRIMARY} !important;
  color: {TEXT_PRIMARY} !important;
  font-family: 'DM Sans', system-ui, sans-serif !important;
}}
.main .block-container {{
  padding: 1.6rem 2rem 4rem !important;
  max-width: 1280px !important;
}}

::-webkit-scrollbar              {{ width: 4px; height: 4px; }}
::-webkit-scrollbar-track        {{ background: {BG_PRIMARY}; }}
::-webkit-scrollbar-thumb        {{ background: {ORANGE}66; border-radius: 99px; }}
::-webkit-scrollbar-thumb:hover  {{ background: {ORANGE}; }}

/* ── Sidebar — forced visible ── */
section[data-testid="stSidebar"] {{
  display: flex !important;
  visibility: visible !important;
  background: {BG_ELEVATED} !important;
  border-right: 1px solid {BORDER} !important;
  min-width: 240px !important;
}}
section[data-testid="stSidebar"] > div {{
  background: {BG_ELEVATED} !important;
  visibility: visible !important;
}}
[data-testid="stSidebarContent"] {{
  visibility: visible !important;
  background: {BG_ELEVATED} !important;
}}
section[data-testid="stSidebar"] * {{ color: {TEXT_PRIMARY} !important; }}
[data-testid="stSidebarNavLink"] {{
  border-radius: 8px !important;
  margin: 1px 6px !important;
  font-size: 0.86rem !important;
  font-family: 'DM Sans', sans-serif !important;
  color: {TEXT_SEC} !important;
  transition: all 0.2s !important;
}}
[data-testid="stSidebarNavLink"]:hover {{
  background: rgba(196,80,0,0.08) !important;
  color: {ORANGE} !important;
}}
[data-testid="stSidebarNavLink"][aria-current="page"] {{
  background: rgba(196,80,0,0.1) !important;
  border-left: 2px solid {ORANGE} !important;
  color: {ORANGE} !important;
}}

/* ── Hide top bar but NOT sidebar toggle ── */
[data-testid="stToolbar"] {{ display: none !important; }}
[data-testid="stDecoration"] {{ display: none !important; }}
#MainMenu {{ visibility: hidden !important; }}
footer {{ visibility: hidden !important; }}

/* ── Hide Plotly chart modebar (zoom/pan/download controls) ── */
.modebar, .modebar-container, .modebar-group {{ display: none !important; }}

/* ── Metric cards ── */
[data-testid="stMetric"] {{
  background: {BG_SURFACE} !important;
  border: 1px solid {BORDER} !important;
  border-top: 2px solid {ORANGE}55 !important;
  border-radius: 12px !important;
  padding: 1rem 1.2rem !important;
  box-shadow: 0 1px 8px rgba(0,0,0,0.05) !important;
  animation: pulseGlow 3s ease-in-out infinite !important;
  transition: border-color 0.25s !important;
}}
[data-testid="stMetric"]:hover {{
  border-color: {ORANGE}77 !important;
  box-shadow: 0 3px 16px rgba(196,80,0,0.1) !important;
}}
[data-testid="stMetricLabel"] p {{
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.63rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.09em !important;
  text-transform: uppercase !important;
  color: {TEXT_MUTED} !important;
}}
[data-testid="stMetricValue"] {{
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 1.5rem !important;
  font-weight: 500 !important;
  color: {TEXT_PRIMARY} !important;
}}
[data-testid="stMetricDelta"] > div {{
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.72rem !important;
}}

/* ── Inputs ── */
.stSelectbox > div > div,
.stMultiSelect > div > div {{
  background: {BG_SURFACE} !important;
  border: 1px solid {BORDER} !important;
  border-radius: 10px !important;
  color: {TEXT_PRIMARY} !important;
}}
.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within {{
  border-color: {ORANGE} !important;
  box-shadow: 0 0 0 2px {ORANGE_DIM} !important;
}}
[data-testid="stRadio"] label, [data-testid="stCheckbox"] label {{
  color: {TEXT_PRIMARY} !important;
  font-family: 'DM Sans', sans-serif !important;
}}

/* ── Buttons ── */
.stButton > button {{
  background: linear-gradient(135deg, {ORANGE} 0%, {ORANGE_LIGHT} 100%) !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 10px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 600 !important;
  box-shadow: 0 2px 12px rgba(196,80,0,0.2) !important;
  transition: opacity 0.2s, transform 0.15s !important;
}}
.stButton > button:hover {{ opacity: 0.88 !important; transform: translateY(-1px) !important; }}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {{
  background: {BG_ELEVATED} !important;
  border: 1px solid {BORDER} !important;
  border-radius: 10px !important;
  padding: 3px !important;
  gap: 2px !important;
}}
.stTabs [data-baseweb="tab"] {{
  background: transparent !important;
  color: {TEXT_SEC} !important;
  border-radius: 8px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.82rem !important;
  font-weight: 500 !important;
  border-bottom: none !important;
}}
.stTabs [aria-selected="true"] {{
  background: {BG_SURFACE} !important;
  color: {ORANGE} !important;
  border-bottom: 2px solid {ORANGE} !important;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
}}
.stTabs [data-baseweb="tab-panel"] {{
  padding-top: 1rem !important;
  background: transparent !important;
}}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {{
  border: 1px solid {BORDER} !important;
  border-radius: 10px !important;
  overflow: hidden !important;
}}
[data-testid="stDataFrame"] th {{
  background: {BG_ELEVATED} !important;
  color: {TEXT_SEC} !important;
  font-size: 0.67rem !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.06em !important;
}}
[data-testid="stDataFrame"] td {{
  background: {BG_SURFACE} !important;
  color: {TEXT_PRIMARY} !important;
  font-size: 0.84rem !important;
}}
[data-testid="stDataFrame"] tr:hover td {{ background: {BG_ELEVATED} !important; }}

/* ── Alert ── */
[data-testid="stAlert"] {{
  background: rgba(196,80,0,0.05) !important;
  border: 1px solid {ORANGE}33 !important;
  border-radius: 10px !important;
  color: {TEXT_PRIMARY} !important;
}}

/* ── Divider ── */
hr {{ border: none !important; border-top: 1px solid {BORDER} !important; margin: 1.6rem 0 !important; }}

/* ── Insight box ── */
.insight-box {{
  background: rgba(255,255,255,0.75);
  border: 1px solid {BORDER};
  border-left: 3px solid {ORANGE};
  border-radius: 0 10px 10px 0;
  padding: 0.75rem 1.1rem;
  margin: 0.3rem 0 1.2rem 0;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.86rem;
  color: {TEXT_SEC};
  line-height: 1.7;
}}
.insight-box b {{ color: {ORANGE}; font-weight: 600; }}

.section-label {{
  font-family: 'DM Sans', sans-serif;
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: {ORANGE};
  margin-bottom: 0.35rem;
}}

.page-title {{
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(1.8rem, 4vw, 2.4rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.15;
  color: {TEXT_PRIMARY};
  margin: 0;
}}

.stat-card {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-top: 2px solid {ORANGE}44;
  border-radius: 12px;
  padding: 1rem 1.2rem;
  box-shadow: 0 1px 6px rgba(0,0,0,0.05);
  transition: all 0.22s;
  animation: fadeUp 0.4s ease forwards;
}}
.stat-card:hover {{
  border-color: {ORANGE}55;
  box-shadow: 0 4px 20px rgba(196,80,0,0.1);
  transform: translateY(-2px);
}}

.milestone-card {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-radius: 12px;
  padding: 1rem 1.2rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  transition: all 0.22s;
}}
.milestone-card:hover {{
  border-color: {ORANGE}55;
  box-shadow: 0 4px 20px rgba(196,80,0,0.1);
  transform: translateY(-2px);
}}

.why-box {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-radius: 14px;
  padding: 1.3rem 1.6rem;
  margin-bottom: 1.8rem;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}}

.badge {{
  display: inline-block;
  padding: 2px 10px;
  border-radius: 999px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.63rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  background: {ORANGE_DIM};
  color: {ORANGE};
  border: 1px solid {ORANGE}33;
}}
.badge-teal {{
  background: rgba(0,102,82,0.07);
  color: {TEAL};
  border-color: {TEAL}33;
}}

.scorecard {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-radius: 10px;
  padding: 0.85rem 1.1rem;
  margin-bottom: 0.5rem;
  transition: all 0.2s;
}}
.scorecard:hover {{ border-color: {TEAL}44; box-shadow: 0 2px 10px rgba(0,102,82,0.07); }}

.footer {{
  margin-top: 3.5rem;
  padding-top: 1.2rem;
  border-top: 1px solid {BORDER};
  font-family: 'DM Sans', sans-serif;
  font-size: 0.73rem;
  color: {TEXT_MUTED};
  text-align: center;
}}
.footer a {{ color: {ORANGE}; text-decoration: none; }}
.footer a:hover {{ color: {ORANGE_LIGHT}; }}
</style>
"""


def footer_html() -> str:
    return f"""
<div class="footer">
  Data: &nbsp;
  <a href="https://indiabudget.gov.in" target="_blank">indiabudget.gov.in</a> &nbsp;·&nbsp;
  <a href="https://data.gov.in" target="_blank">data.gov.in</a> &nbsp;·&nbsp;
  <a href="https://rbi.org.in" target="_blank">RBI DBIE</a> &nbsp;·&nbsp;
  <a href="https://mospi.gov.in" target="_blank">MOSPI</a> &nbsp;·&nbsp;
  <a href="https://gem.gov.in" target="_blank">GeM Portal</a> &nbsp;·&nbsp;
  <a href="https://fincom15.gov.in" target="_blank">Finance Commission XV</a>
  <br/><br/>
  <span>Built with public data for public good &nbsp;·&nbsp; BharatBudget 2025</span>
</div>
"""


def insight_box(text: str) -> str:
    return f'<div class="insight-box">💡 {text}</div>'


def page_header(icon: str, title: str, subtitle: str) -> str:
    return f"""
<div style="padding:0.2rem 0 1.3rem 0; animation:fadeUp 0.4s ease forwards;">
  <div class="section-label">{icon} BharatBudget</div>
  <h1 style="font-family:'Playfair Display',Georgia,serif;
             font-size:clamp(1.7rem,4vw,2.3rem); font-weight:700;
             letter-spacing:-0.02em; line-height:1.15;
             color:{TEXT_PRIMARY}; margin:0 0 0.5rem 0;">{title}</h1>
  <p style="font-family:'DM Sans',sans-serif; color:{TEXT_SEC}; font-size:0.92rem;
            margin:0; max-width:640px; line-height:1.65;">{subtitle}</p>
</div>
"""
