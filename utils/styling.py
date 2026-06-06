"""Premium warm parchment theme for BharatBudget — Streamlit 1.49."""

# ── Colour palette ────────────────────────────────────────────────────────────
BG_PRIMARY   = "#F2E8D2"   # golden parchment (main bg)
BG_SURFACE   = "#FAF6EC"   # warm cream (cards — NOT stark white)
BG_ELEVATED  = "#E6D9BD"   # deeper tan (sidebar, raised)
BORDER       = "#C8B898"   # warm golden border
BORDER_GLOW  = "#C84E0040"

ORANGE       = "#C84E00"   # terracotta saffron
ORANGE_LIGHT = "#E06820"   # medium saffron
ORANGE_DIM   = "#C84E0010"

TEAL         = "#2E7D60"   # forest green
RED          = "#A02828"
BLUE_SOFT    = "#2B5299"

TEXT_PRIMARY = "#1A0E06"   # very dark warm brown
TEXT_SEC     = "#4A3520"   # mid warm brown
TEXT_MUTED   = "#7A6250"   # readable muted (all contrast ≥4.5:1 on BG_PRIMARY)

PLOTLY_PAPER = "#F2E8D2"
PLOTLY_PLOT  = "#FAF6EC"   # cream, not white
GRID_COLOR   = "#DDD0B8"

# Legacy aliases
BEIGE        = TEXT_PRIMARY
BEIGE_MUTED  = TEXT_SEC
BEIGE_DIM    = TEXT_MUTED
WHITE        = BG_SURFACE
NAVY         = BG_PRIMARY
NAVY_CARD    = BG_SURFACE
NAVY_LIGHT   = BORDER
TEXT_MAIN    = TEXT_PRIMARY
BG_CARD      = BG_SURFACE
BG_RAISED    = BG_ELEVATED
PLOTLY_PAPER_BG = PLOTLY_PAPER
PLOTLY_PLOT_BG  = PLOTLY_PLOT

MINISTRY_COLOR_MAP = {
    "Defence":                   "#B03030",
    "Interest Payments":         "#7A6250",
    "Road Transport & Highways": "#C84E00",
    "Railways":                  "#D97030",
    "Rural Development":         "#2E7D60",
    "Home Affairs":              "#A03030",
    "Education":                 "#2B5299",
    "Agriculture & Allied":      "#3A7030",
    "Health & Family Welfare":   "#7A3A9A",
    "Communications & IT":       "#1A62A0",
    "Jal Shakti / Water":        "#0A7090",
    "Housing & Urban Affairs":   "#8A6800",
    "Food & Public Distribution":"#3A8040",
    "Fertiliser Subsidy":        "#4A8848",
    "Science & Space":           "#5A2890",
    "Social Welfare":            "#982858",
    "State Transfers (CSS)":     "#1A7A6A",
    "Others":                    "#6A6050",
}

CATEGORY_COLORS = {
    "Security & Governance": "#B03030",
    "Infrastructure":        "#C84E00",
    "Social":                "#2E7D60",
    "Economy & Agriculture": "#2B5299",
    "Transfers & Others":    "#6A6050",
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
            bgcolor="rgba(242,232,210,0.9)",
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
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Keyframes ── */
@keyframes fadeUp {{
  from {{ opacity: 0; transform: translateY(16px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes pulseGlow {{
  0%, 100% {{ box-shadow: 0 1px 4px rgba(200,78,0,0.07), 0 2px 8px rgba(0,0,0,0.04); }}
  50%       {{ box-shadow: 0 2px 18px rgba(200,78,0,0.18), 0 4px 16px rgba(0,0,0,0.07); }}
}}

/* ── App base ── */
*, *::before, *::after {{ box-sizing: border-box; }}

/* ── Branded top header bar ──
   Keep Streamlit's default position (fixed) so its JS correctly offsets stMain.
   The ::before pseudo-element works on fixed elements just as well as relative. */
header[data-testid="stHeader"] {{
  background: {BG_ELEVATED} !important;
  border-bottom: 1px solid {BORDER} !important;
  box-shadow: 0 1px 8px rgba(200,78,0,0.06) !important;
  overflow: visible !important;
}}
header[data-testid="stHeader"]::before {{
  content: "BharatBudget";
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: {ORANGE};
  pointer-events: none;
  white-space: nowrap;
}}

/* ── Style the hamburger toggle buttons ── */
[data-testid="stSidebarCollapsedControl"] {{
  top: 0.6rem !important;
  left: 0.5rem !important;
}}
[data-testid="stSidebarCollapsedControl"] button,
[data-testid="stSidebarCollapseButton"] button {{
  background: {BG_ELEVATED} !important;
  border: 1px solid {BORDER} !important;
  border-radius: 8px !important;
  color: {TEXT_SEC} !important;
  transition: background 0.14s ease, color 0.14s ease !important;
}}
[data-testid="stSidebarCollapsedControl"] button:hover,
[data-testid="stSidebarCollapseButton"] button:hover {{
  background: rgba(200,78,0,0.08) !important;
  color: {ORANGE} !important;
  border-color: {ORANGE}55 !important;
}}

/* ── Hide Streamlit anchor-link icons on every heading ── */
a[data-testid="stHeadingAnchorLink"] {{
  display: none !important;
}}

.stApp {{
  background-color: {BG_PRIMARY} !important;
  font-family: 'DM Sans', system-ui, sans-serif !important;
}}
.main {{
  background-color: {BG_PRIMARY} !important;
  color: {TEXT_PRIMARY} !important;
}}
.main .block-container {{
  padding: 0.5rem 2rem 4rem !important;
  max-width: 1280px !important;
  background-color: {BG_PRIMARY} !important;
}}

/* ── Scrollbar ── */
::-webkit-scrollbar              {{ width: 5px; height: 5px; }}
::-webkit-scrollbar-track        {{ background: {BG_PRIMARY}; }}
::-webkit-scrollbar-thumb        {{ background: {ORANGE}55; border-radius: 99px; }}
::-webkit-scrollbar-thumb:hover  {{ background: {ORANGE}; }}

/* ── Sidebar ── */
[data-testid="stSidebar"] {{
  background-color: {BG_ELEVATED} !important;
  border-right: 1px solid {BORDER} !important;
}}
[data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"] {{
  background-color: {BG_ELEVATED} !important;
  padding: 0 !important;
}}
[data-testid="stSidebarNavSeparator"] {{
  border-color: {BORDER} !important;
  opacity: 0.5 !important;
  margin: 6px 12px !important;
}}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span:not([data-testid]),
[data-testid="stSidebar"] div.stMarkdown {{
  color: {TEXT_PRIMARY} !important;
  font-family: 'DM Sans', sans-serif !important;
}}

/* ── Nav link base styles ── */
[data-testid="stSidebarNavLink"] {{
  border-radius: 7px !important;
  margin: 1px 8px !important;
  padding: 8px 10px !important;
  font-size: 0.82rem !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 500 !important;
  color: {TEXT_SEC} !important;
  letter-spacing: 0.01em !important;
  transition: background 0.14s ease, color 0.14s ease !important;
  border-left: 2px solid transparent !important;
  white-space: nowrap !important;
  overflow: hidden !important;
}}
[data-testid="stSidebarNavLink"]:hover {{
  background: rgba(200,78,0,0.08) !important;
  color: {ORANGE} !important;
  border-left-color: {ORANGE}55 !important;
}}
[data-testid="stSidebarNavLink"][aria-current="page"] {{
  background: rgba(200,78,0,0.11) !important;
  border-left: 2px solid {ORANGE} !important;
  color: {ORANGE} !important;
  font-weight: 600 !important;
}}
/* Text label is a <span> (StyledSidebarLinkText) */
[data-testid="stSidebarNavLink"] > span:last-child {{
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.82rem !important;
  white-space: nowrap !important;
  overflow: hidden !important;
}}
[data-testid="stSidebarNavLink"][aria-current="page"] > span:last-child {{
  font-weight: 600 !important;
  color: {ORANGE} !important;
}}
[data-testid="stSidebarNavItems"] {{
  padding: 4px 0 !important;
}}


[data-testid="stStatusWidget"] {{ display: none !important; }}
[data-testid="stDecoration"]   {{ display: none !important; }}
#MainMenu {{ visibility: hidden !important; }}
footer    {{ visibility: hidden !important; }}

/* ── Hide Plotly modebar (zoom / pan / download) ── */
.modebar, .modebar-container, .modebar-group {{ display: none !important; }}

/* ── Metric cards ── */
[data-testid="stMetric"] {{
  background: {BG_SURFACE} !important;
  border: 1px solid {BORDER} !important;
  border-top: 2px solid {ORANGE}55 !important;
  border-radius: 12px !important;
  padding: 1rem 1.2rem !important;
  box-shadow: 0 1px 6px rgba(0,0,0,0.05), 0 2px 16px rgba(200,78,0,0.04) !important;
  animation: pulseGlow 3.5s ease-in-out infinite !important;
  transition: border-color 0.2s !important;
}}
[data-testid="stMetric"]:hover {{
  border-color: {ORANGE}77 !important;
  box-shadow: 0 3px 14px rgba(200,78,0,0.12) !important;
}}
[data-testid="stMetricLabel"] p {{
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.62rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: {TEXT_MUTED} !important;
}}
[data-testid="stMetricValue"] {{
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 1.5rem !important;
  font-weight: 500 !important;
  color: {TEXT_PRIMARY} !important;
  letter-spacing: -0.01em !important;
}}
[data-testid="stMetricDelta"] > div {{
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.72rem !important;
  font-weight: 500 !important;
}}

/* ── Inputs ── */
.stSelectbox > div > div,
.stMultiSelect > div > div {{
  background: {BG_SURFACE} !important;
  border: 1px solid {BORDER} !important;
  border-radius: 10px !important;
  color: {TEXT_PRIMARY} !important;
  font-family: 'DM Sans', sans-serif !important;
}}
.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within {{
  border-color: {ORANGE} !important;
  box-shadow: 0 0 0 2px {ORANGE_DIM} !important;
}}
[data-testid="stRadio"] label,
[data-testid="stCheckbox"] label {{
  color: {TEXT_PRIMARY} !important;
  font-family: 'DM Sans', sans-serif !important;
}}

/* ── Buttons ── */
.stButton > button {{
  background: linear-gradient(135deg, {ORANGE} 0%, {ORANGE_LIGHT} 100%) !important;
  color: #FFF8F0 !important;
  border: none !important;
  border-radius: 10px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 600 !important;
  box-shadow: 0 2px 10px rgba(200,78,0,0.22) !important;
  transition: opacity 0.18s, transform 0.15s !important;
}}
.stButton > button:hover {{
  opacity: 0.88 !important;
  transform: translateY(-1px) !important;
}}

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
  padding: 6px 14px !important;
}}
.stTabs [aria-selected="true"] {{
  background: {BG_SURFACE} !important;
  color: {ORANGE} !important;
  border-bottom: 2px solid {ORANGE} !important;
  box-shadow: 0 1px 4px rgba(0,0,0,0.07) !important;
  font-weight: 600 !important;
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
  padding: 8px 12px !important;
}}
[data-testid="stDataFrame"] td {{
  background: {BG_SURFACE} !important;
  color: {TEXT_PRIMARY} !important;
  font-size: 0.84rem !important;
  padding: 7px 12px !important;
}}
[data-testid="stDataFrame"] tr:hover td {{
  background: {BG_ELEVATED} !important;
}}

/* ── Alert ── */
[data-testid="stAlert"] {{
  background: rgba(200,78,0,0.05) !important;
  border: 1px solid {ORANGE}30 !important;
  border-radius: 10px !important;
  color: {TEXT_PRIMARY} !important;
}}

button[data-testid="baseButton-headerNoPadding"],
button[data-testid="baseButton-header"] {{
  color: {TEXT_MUTED} !important;
  border-radius: 8px !important;
}}
button[data-testid="baseButton-headerNoPadding"]:hover,
button[data-testid="baseButton-header"]:hover {{
  background: rgba(200,78,0,0.08) !important;
  color: {ORANGE} !important;
}}

/* ── Controls row (inline page controls) ── */
.controls-row {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-radius: 12px;
  padding: 0.85rem 1.2rem;
  margin-bottom: 1.2rem;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: flex-end;
}}

/* ── Section header ── */
.section-header {{
  font-family: 'DM Sans', sans-serif;
  font-size: 0.82rem;
  font-weight: 600;
  color: {TEXT_PRIMARY};
  margin-bottom: 0.6rem;
  margin-top: 0.2rem;
}}

/* ── Divider ── */
hr {{
  border: none !important;
  border-top: 1px solid {BORDER} !important;
  margin: 1.5rem 0 !important;
}}

/* ── Expander ── */
[data-testid="stExpander"] {{
  background: {BG_SURFACE} !important;
  border: 1px solid {BORDER} !important;
  border-radius: 10px !important;
}}

/* ─────────────────────────────
   CUSTOM COMPONENTS
   ───────────────────────────── */

/* Insight box — warm tint, not white */
.insight-box {{
  background: rgba(200,78,0,0.05);
  border: 1px solid {BORDER};
  border-left: 3px solid {ORANGE};
  border-radius: 0 10px 10px 0;
  padding: 0.8rem 1.1rem;
  margin: 0.3rem 0 1.2rem 0;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.87rem;
  color: {TEXT_SEC};
  line-height: 1.75;
}}
.insight-box b {{ color: {ORANGE}; font-weight: 600; }}

/* Section label */
.section-label {{
  font-family: 'DM Sans', sans-serif;
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.11em;
  text-transform: uppercase;
  color: {ORANGE};
  margin-bottom: 0.35rem;
  display: flex;
  align-items: center;
  gap: 0.35rem;
}}

/* Stat card */
.stat-card {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-top: 2px solid {ORANGE}44;
  border-radius: 12px;
  padding: 1rem 1.2rem;
  box-shadow: 0 1px 5px rgba(0,0,0,0.05);
  transition: all 0.22s ease;
  animation: fadeUp 0.45s ease forwards;
}}
.stat-card:hover {{
  border-color: {ORANGE}66;
  box-shadow: 0 4px 18px rgba(200,78,0,0.1);
  transform: translateY(-2px);
}}

/* Milestone card */
.milestone-card {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-radius: 12px;
  padding: 1rem 1.2rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  transition: all 0.22s ease;
}}
.milestone-card:hover {{
  border-color: {ORANGE}55;
  box-shadow: 0 4px 16px rgba(200,78,0,0.1);
  transform: translateY(-2px);
}}

/* Why box */
.why-box {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-radius: 14px;
  padding: 1.3rem 1.6rem;
  margin-bottom: 1.8rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.04);
}}

/* Badge */
.badge {{
  display: inline-block;
  padding: 3px 11px;
  border-radius: 999px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.63rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  background: {ORANGE_DIM};
  color: {ORANGE};
  border: 1px solid {ORANGE}40;
}}
.badge-teal {{
  background: rgba(46,125,96,0.08);
  color: {TEAL};
  border-color: {TEAL}40;
}}
.badge-blue {{
  background: rgba(43,82,153,0.08);
  color: {BLUE_SOFT};
  border-color: {BLUE_SOFT}40;
}}

/* Statistics card (aghasisahakyan1 style) */
.stat-bar-card {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-radius: 14px;
  padding: 1.2rem 1.4rem 1rem;
  box-shadow: 0 1px 6px rgba(0,0,0,0.05);
}}
.stat-bar-card .bars-row {{
  display: flex;
  align-items: flex-end;
  gap: 10px;
  height: 80px;
  margin: 0.8rem 0 0.5rem;
}}
.stat-bar-card .bar-col {{
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  height: 100%;
  justify-content: flex-end;
}}
.stat-bar-card .bar-fill {{
  width: 100%;
  border-radius: 4px 4px 0 0;
  background: repeating-linear-gradient(
    45deg, rgba(255,255,255,0.07), rgba(255,255,255,0.07) 2px,
    transparent 2px, transparent 6px
  ), {ORANGE};
  transition: height 0.4s cubic-bezier(.34,1.56,.64,1);
  position: relative;
}}
.stat-bar-card .bar-fill.highlight {{
  background: repeating-linear-gradient(
    45deg, rgba(255,255,255,0.1), rgba(255,255,255,0.1) 2px,
    transparent 2px, transparent 6px
  ), #38BDF8;
}}
.stat-bar-card .bar-badge {{
  width: 26px; height: 26px;
  border-radius: 50%;
  background: {BG_ELEVATED};
  border: 1.5px solid {BORDER};
  display: flex; align-items: center; justify-content: center;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.52rem;
  font-weight: 700;
  color: {TEXT_PRIMARY};
  flex-shrink: 0;
}}
.stat-bar-card .bar-label {{
  font-family: 'DM Sans', sans-serif;
  font-size: 0.6rem;
  color: {TEXT_MUTED};
  text-align: center;
  max-width: 60px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}

/* Scorecard row */
.scorecard {{
  background: {BG_SURFACE};
  border: 1px solid {BORDER};
  border-radius: 10px;
  padding: 0.8rem 1.1rem;
  margin-bottom: 0.45rem;
  transition: all 0.18s;
}}
.scorecard:hover {{
  border-color: {TEAL}55;
  background: {BG_ELEVATED};
}}

/* Footer */
.footer {{
  margin-top: 3.5rem;
  padding-top: 1.2rem;
  border-top: 1px solid {BORDER};
  font-family: 'DM Sans', sans-serif;
  font-size: 0.73rem;
  color: {TEXT_MUTED};
  text-align: center;
  line-height: 1.9;
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
  <br/>
  Built with public data for public good &nbsp;·&nbsp; BharatBudget 2025
</div>
"""


def insight_box(text: str) -> str:
    return f'<div class="insight-box">💡 {text}</div>'


def page_header(icon: str, title: str, subtitle: str) -> str:
    icon_html = f'<span style="margin-right:0.4rem;">{icon}</span>' if icon else ""
    return f"""
<div style="padding:0 0 1.2rem 0; animation:fadeUp 0.4s ease forwards;">
  <h1 style="font-family:'Playfair Display',Georgia,serif;
             font-size:clamp(2rem,5vw,2.8rem); font-weight:700;
             letter-spacing:-0.03em; line-height:1.1;
             color:{TEXT_PRIMARY}; margin:0 0 0.55rem 0;">{icon_html}{title}</h1>
  <p style="font-family:'DM Sans',sans-serif; color:{TEXT_SEC}; font-size:0.95rem;
            margin:0; max-width:680px; line-height:1.75;">{subtitle}</p>
</div>
"""
