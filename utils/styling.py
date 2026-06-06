"""Premium dark theme for BharatBudget — 21st.dev inspired, orange/black/beige."""

# ── Colour palette ─────────────────────────────────────────────────────────────
BG_PRIMARY   = "#08080B"   # near-black page background
BG_CARD      = "#0F0F13"   # card surface
BG_RAISED    = "#16161B"   # elevated card / hover
BORDER       = "#1E1E26"   # default border
BORDER_GLOW  = "#FF6B0055" # orange border glow

ORANGE       = "#FF6B00"   # primary accent
ORANGE_LIGHT = "#FF9A4D"   # lighter orange for text gradients
ORANGE_DIM   = "#FF6B0022" # orange tint for backgrounds

BEIGE        = "#E8DCC8"   # primary warm text
BEIGE_MUTED  = "#8A7F74"   # secondary / muted text
BEIGE_DIM    = "#4A433C"   # very muted, borders & dividers

WHITE        = "#F5F0EA"   # brightest text (headings)
TEAL         = "#00C49A"   # positive indicator
RED          = "#FF4D4D"   # negative / warning
BLUE_SOFT    = "#7EB8FF"   # soft blue accent

# Plotly backgrounds
PLOTLY_PAPER = "#08080B"
PLOTLY_PLOT  = "#0F0F13"
GRID_COLOR   = "#1A1A22"

# Legacy aliases (used in pages that import these names)
NAVY             = BG_PRIMARY
NAVY_CARD        = BG_CARD
NAVY_LIGHT       = BORDER
TEXT_MAIN        = BEIGE
TEXT_MUTED       = BEIGE_MUTED
PLOTLY_PAPER_BG  = PLOTLY_PAPER
PLOTLY_PLOT_BG   = PLOTLY_PLOT

MINISTRY_COLOR_MAP = {
    "Defence":                   "#FF4D4D",
    "Interest Payments":         "#6B6B7A",
    "Road Transport & Highways": "#FF6B00",
    "Railways":                  "#FF9A4D",
    "Rural Development":         "#00C49A",
    "Home Affairs":              "#E87070",
    "Education":                 "#7EB8FF",
    "Agriculture & Allied":      "#6DBF7E",
    "Health & Family Welfare":   "#C07BDB",
    "Communications & IT":       "#5BA8F5",
    "Jal Shakti / Water":        "#4DC8E8",
    "Housing & Urban Affairs":   "#F5D87A",
    "Food & Public Distribution":"#8FCF8F",
    "Fertiliser Subsidy":        "#B0D9B0",
    "Science & Space":           "#B87BE8",
    "Social Welfare":            "#F5A0BB",
    "State Transfers (CSS)":     "#6FCFC3",
    "Others":                    "#4A4A55",
}

CATEGORY_COLORS = {
    "Security & Governance": "#FF4D4D",
    "Infrastructure":        "#FF6B00",
    "Social":                "#00C49A",
    "Economy & Agriculture": "#7EB8FF",
    "Transfers & Others":    "#6B6B7A",
}


def get_plotly_layout(title: str = "", height: int = 420) -> dict:
    return dict(
        title=dict(text=title, font=dict(color=WHITE, size=14, family="Inter, sans-serif"), x=0.02),
        paper_bgcolor=PLOTLY_PAPER,
        plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=BEIGE, family="Inter, sans-serif"),
        height=height,
        margin=dict(l=16, r=16, t=48, b=16),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            bordercolor=BORDER,
            font=dict(color=BEIGE_MUTED, size=11),
        ),
        xaxis=dict(
            gridcolor=GRID_COLOR,
            linecolor=BORDER,
            tickfont=dict(color=BEIGE_MUTED),
            title_font=dict(color=BEIGE_MUTED),
            zeroline=False,
        ),
        yaxis=dict(
            gridcolor=GRID_COLOR,
            linecolor=BORDER,
            tickfont=dict(color=BEIGE_MUTED),
            title_font=dict(color=BEIGE_MUTED),
            zeroline=False,
        ),
    )


# ── Global Streamlit CSS ───────────────────────────────────────────────────────
GLOBAL_CSS = f"""
<style>
  /* ── Google font ── */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

  /* ── Reset & base ── */
  *, *::before, *::after {{ box-sizing: border-box; }}

  .stApp, .main {{
    background-color: {BG_PRIMARY} !important;
    color: {BEIGE} !important;
    font-family: 'Inter', sans-serif !important;
  }}
  .main .block-container {{
    padding-top: 1.6rem;
    padding-bottom: 3rem;
    max-width: 1200px;
  }}

  /* ── Scrollbar ── */
  ::-webkit-scrollbar {{ width: 5px; height: 5px; }}
  ::-webkit-scrollbar-track {{ background: {BG_PRIMARY}; }}
  ::-webkit-scrollbar-thumb {{ background: {ORANGE}55; border-radius: 99px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: {ORANGE}; }}

  /* ── Sidebar ── */
  [data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #0A0A0E 0%, #0D0D12 100%) !important;
    border-right: 1px solid {BORDER} !important;
  }}
  [data-testid="stSidebar"] .block-container {{
    padding-top: 1rem;
  }}
  [data-testid="stSidebar"] * {{
    color: {BEIGE} !important;
  }}
  [data-testid="stSidebarNavLink"] {{
    border-radius: 8px !important;
    transition: background 0.2s;
  }}
  [data-testid="stSidebarNavLink"]:hover {{
    background: {ORANGE_DIM} !important;
  }}
  [data-testid="stSidebarNavLink"][aria-current="page"] {{
    background: {ORANGE_DIM} !important;
    border-left: 2px solid {ORANGE} !important;
  }}

  /* ── Metric cards ── */
  [data-testid="stMetric"] {{
    background: {BG_CARD} !important;
    border: 1px solid {BORDER} !important;
    border-top: 1px solid {ORANGE}44 !important;
    border-radius: 12px !important;
    padding: 1rem 1.25rem !important;
    transition: border-color 0.2s, box-shadow 0.2s;
  }}
  [data-testid="stMetric"]:hover {{
    border-color: {ORANGE}88 !important;
    box-shadow: 0 0 18px {ORANGE}15 !important;
  }}
  [data-testid="stMetricLabel"] p {{
    color: {BEIGE_MUTED} !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.04em !important;
    text-transform: uppercase;
  }}
  [data-testid="stMetricValue"] {{
    color: {WHITE} !important;
    font-size: 1.45rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
  }}
  [data-testid="stMetricDelta"] {{
    font-size: 0.75rem !important;
  }}

  /* ── Select / Multiselect ── */
  .stSelectbox > div > div,
  .stMultiSelect > div > div {{
    background: {BG_CARD} !important;
    border: 1px solid {BORDER} !important;
    color: {BEIGE} !important;
    border-radius: 8px !important;
  }}
  .stSelectbox > div > div:focus-within,
  .stMultiSelect > div > div:focus-within {{
    border-color: {ORANGE} !important;
    box-shadow: 0 0 0 2px {ORANGE_DIM} !important;
  }}

  /* ── Radio ── */
  [data-testid="stRadio"] label {{
    color: {BEIGE} !important;
  }}
  [data-testid="stRadio"] div[data-baseweb="radio"] div {{
    background: {ORANGE} !important;
  }}

  /* ── Checkbox ── */
  [data-testid="stCheckbox"] label {{
    color: {BEIGE} !important;
  }}

  /* ── Buttons ── */
  .stButton > button {{
    background: linear-gradient(135deg, {ORANGE} 0%, {ORANGE_LIGHT} 100%) !important;
    color: {BG_PRIMARY} !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
    transition: opacity 0.2s, transform 0.15s !important;
  }}
  .stButton > button:hover {{
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
  }}

  /* ── Tabs ── */
  .stTabs [data-baseweb="tab-list"] {{
    background: {BG_CARD} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 10px !important;
    padding: 3px !important;
    gap: 2px !important;
  }}
  .stTabs [data-baseweb="tab"] {{
    background: transparent !important;
    color: {BEIGE_MUTED} !important;
    border-radius: 7px !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    transition: all 0.2s !important;
  }}
  .stTabs [aria-selected="true"] {{
    background: {ORANGE_DIM} !important;
    color: {ORANGE_LIGHT} !important;
    border-bottom: 2px solid {ORANGE} !important;
  }}
  .stTabs [data-baseweb="tab-panel"] {{
    padding-top: 1rem !important;
  }}

  /* ── Dataframe / Table ── */
  [data-testid="stDataFrame"] {{
    border: 1px solid {BORDER} !important;
    border-radius: 10px !important;
    overflow: hidden !important;
  }}
  [data-testid="stDataFrame"] th {{
    background: {BG_RAISED} !important;
    color: {BEIGE_MUTED} !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-bottom: 1px solid {BORDER} !important;
  }}
  [data-testid="stDataFrame"] td {{
    background: {BG_CARD} !important;
    color: {BEIGE} !important;
    border-bottom: 1px solid {BORDER}88 !important;
    font-size: 0.85rem !important;
  }}
  [data-testid="stDataFrame"] tr:hover td {{
    background: {BG_RAISED} !important;
  }}

  /* ── Expander ── */
  [data-testid="stExpander"] {{
    background: {BG_CARD} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 10px !important;
  }}
  [data-testid="stExpander"] summary {{
    color: {BEIGE} !important;
  }}

  /* ── Alerts / Info ── */
  [data-testid="stAlert"] {{
    background: {BG_CARD} !important;
    border: 1px solid {ORANGE}44 !important;
    border-radius: 8px !important;
    color: {BEIGE} !important;
  }}

  /* ── Divider ── */
  hr {{
    border: none !important;
    border-top: 1px solid {BORDER} !important;
    margin: 1.4rem 0 !important;
  }}

  /* ── Insight box ── */
  .insight-box {{
    background: {BG_CARD};
    border: 1px solid {BORDER};
    border-left: 2px solid {ORANGE};
    border-radius: 0 10px 10px 0;
    padding: 0.7rem 1.1rem;
    margin: 0.3rem 0 1.1rem 0;
    font-size: 0.85rem;
    color: {BEIGE_MUTED};
    line-height: 1.65;
  }}
  .insight-box b {{ color: {ORANGE_LIGHT}; }}

  /* ── Section header ── */
  .section-header {{
    font-size: 1.1rem;
    font-weight: 600;
    color: {WHITE};
    margin: 0.2rem 0 1rem 0;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }}

  /* ── Stat card (custom) ── */
  .stat-card {{
    background: {BG_CARD};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 1.1rem 1.3rem;
    transition: border-color 0.2s, box-shadow 0.2s;
  }}
  .stat-card:hover {{
    border-color: {ORANGE}55;
    box-shadow: 0 0 20px {ORANGE}0D;
  }}
  .stat-card .label {{
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: {BEIGE_MUTED};
    margin-bottom: 0.35rem;
  }}
  .stat-card .value {{
    font-size: 1.5rem;
    font-weight: 700;
    color: {WHITE};
    letter-spacing: -0.025em;
  }}
  .stat-card .delta {{
    font-size: 0.72rem;
    color: {TEAL};
    margin-top: 0.2rem;
  }}

  /* ── Badge ── */
  .badge {{
    display: inline-block;
    padding: 2px 10px;
    border-radius: 999px;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    background: {ORANGE_DIM};
    color: {ORANGE_LIGHT};
    border: 1px solid {ORANGE}33;
  }}
  .badge-teal {{
    background: #00C49A18;
    color: {TEAL};
    border-color: {TEAL}33;
  }}

  /* ── Page title gradient ── */
  .page-title {{
    background: linear-gradient(90deg, {ORANGE} 0%, {ORANGE_LIGHT} 60%, {BEIGE} 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    margin-bottom: 0.15rem;
    line-height: 1.15;
  }}

  /* ── Footer ── */
  .footer {{
    margin-top: 3.5rem;
    padding-top: 1.2rem;
    border-top: 1px solid {BORDER};
    font-size: 0.75rem;
    color: {BEIGE_DIM};
    text-align: center;
    letter-spacing: 0.01em;
  }}
  .footer a {{ color: {ORANGE}; text-decoration: none; }}
  .footer a:hover {{ color: {ORANGE_LIGHT}; }}

  /* ── Hide Streamlit chrome ── */
  #MainMenu, footer, header {{ visibility: hidden; }}
  [data-testid="stDecoration"] {{ display: none; }}
</style>
"""


def footer_html() -> str:
    return f"""
<div class="footer">
  Data sources: &nbsp;
  <a href="https://indiabudget.gov.in" target="_blank">indiabudget.gov.in</a> &nbsp;·&nbsp;
  <a href="https://data.gov.in" target="_blank">data.gov.in</a> &nbsp;·&nbsp;
  <a href="https://rbi.org.in" target="_blank">RBI DBIE</a> &nbsp;·&nbsp;
  <a href="https://mospi.gov.in" target="_blank">MOSPI</a> &nbsp;·&nbsp;
  <a href="https://fincom15.gov.in" target="_blank">Finance Commission XV</a>
  <br/><br/>
  <span style="color:{BEIGE_DIM};">Built with public data for public good &nbsp;·&nbsp; BharatBudget 2025</span>
</div>
"""


def insight_box(text: str) -> str:
    return f'<div class="insight-box">💡 {text}</div>'
