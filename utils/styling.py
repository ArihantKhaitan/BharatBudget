"""
Premium dark theme for BharatBudget.
Design references:
  - Layout & palette: github.com/ArihantKhaitan/Rajneeti
  - UI features & glassmorphism: github.com/ArihantKhaitan/FAKENEWSDETECTOR
"""

# ── Colour palette (Rajneeti-inspired) ───────────────────────────────────────
BG_PRIMARY   = "#0A0A0F"   # very dark base
BG_SURFACE   = "#14141F"   # elevated surface (cards)
BG_ELEVATED  = "#1C1C2E"   # raised card / hover state
BORDER       = "#2A2A3F"   # subtle border (Rajneeti)
BORDER_GLOW  = "#FF6B3544" # saffron border glow

ORANGE       = "#FF6B35"   # saffron accent (Rajneeti)
ORANGE_LIGHT = "#FF9A6C"   # lighter saffron
ORANGE_DIM   = "#FF6B3518" # dim saffron bg tint

TEAL         = "#00C9A7"   # Rajneeti teal
RED          = "#FF4D4D"   # negative
BLUE_SOFT    = "#7EB8FF"   # soft blue

TEXT_PRIMARY = "#E8E6E3"   # Rajneeti primary text
TEXT_SEC     = "#9896A0"   # Rajneeti secondary
TEXT_MUTED   = "#5C5B66"   # Rajneeti muted

# Legacy aliases (keep old imports working)
BEIGE        = TEXT_PRIMARY
BEIGE_MUTED  = TEXT_SEC
BEIGE_DIM    = TEXT_MUTED
WHITE        = TEXT_PRIMARY
NAVY         = BG_PRIMARY
NAVY_CARD    = BG_SURFACE
NAVY_LIGHT   = BORDER
TEXT_MAIN    = TEXT_PRIMARY
BG_CARD      = BG_SURFACE
BG_RAISED    = BG_ELEVATED

PLOTLY_PAPER    = BG_PRIMARY
PLOTLY_PLOT     = BG_SURFACE
PLOTLY_PAPER_BG = BG_PRIMARY
PLOTLY_PLOT_BG  = BG_SURFACE
GRID_COLOR      = "#1E1E2E"

MINISTRY_COLOR_MAP = {
    "Defence":                   "#FF4D4D",
    "Interest Payments":         "#5C5B66",
    "Road Transport & Highways": "#FF6B35",
    "Railways":                  "#FF9A6C",
    "Rural Development":         "#00C9A7",
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
    "Others":                    "#3A3A4A",
}

CATEGORY_COLORS = {
    "Security & Governance": "#FF4D4D",
    "Infrastructure":        "#FF6B35",
    "Social":                "#00C9A7",
    "Economy & Agriculture": "#7EB8FF",
    "Transfers & Others":    "#5C5B66",
}


def get_plotly_layout(title: str = "", height: int = 420) -> dict:
    return dict(
        title=dict(
            text=title,
            font=dict(color=TEXT_PRIMARY, size=14, family="DM Sans, sans-serif"),
            x=0.02,
        ),
        paper_bgcolor=PLOTLY_PAPER,
        plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
        height=height,
        margin=dict(l=16, r=16, t=48, b=16),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            bordercolor=BORDER,
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


# ── Global CSS ────────────────────────────────────────────────────────────────
GLOBAL_CSS = f"""
<style>
/* ── Fonts: Playfair Display + DM Sans + JetBrains Mono ── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Keyframes ── */
@keyframes fadeUp {{
  from {{ opacity: 0; transform: translateY(22px); }}
  to   {{ opacity: 1; transform: translateY(0);    }}
}}
@keyframes fadeIn {{
  from {{ opacity: 0; }} to {{ opacity: 1; }}
}}
@keyframes pulseGlow {{
  0%, 100% {{ box-shadow: 0 0 12px {ORANGE_DIM}, 0 1px 3px rgba(0,0,0,0.4); }}
  50%       {{ box-shadow: 0 0 32px {BORDER_GLOW}, 0 4px 20px rgba(255,107,53,0.15); }}
}}
@keyframes shimmer {{
  0%   {{ background-position: -200% 0; }}
  100% {{ background-position:  200% 0; }}
}}
@keyframes countUp {{
  from {{ opacity: 0; transform: translateY(10px); }}
  to   {{ opacity: 1; transform: translateY(0);    }}
}}
@keyframes borderPulse {{
  0%, 100% {{ border-color: {BORDER}; }}
  50%       {{ border-color: {BORDER_GLOW}; }}
}}

/* ── Reset ── */
*, *::before, *::after {{ box-sizing: border-box; }}

/* ── App base ── */
.stApp, .main {{
  background-color: {BG_PRIMARY} !important;
  color: {TEXT_PRIMARY} !important;
  font-family: 'DM Sans', system-ui, sans-serif !important;
}}
.main .block-container {{
  padding: 1.8rem 2rem 4rem !important;
  max-width: 1280px !important;
}}

/* ── Custom scrollbar ── */
::-webkit-scrollbar              {{ width: 4px; height: 4px; }}
::-webkit-scrollbar-track        {{ background: {BG_PRIMARY}; }}
::-webkit-scrollbar-thumb        {{ background: {ORANGE}55; border-radius: 99px; }}
::-webkit-scrollbar-thumb:hover  {{ background: {ORANGE}; }}

/* ── Sidebar ── */
[data-testid="stSidebar"] {{
  background: linear-gradient(180deg, #0C0C14 0%, #111120 100%) !important;
  border-right: 1px solid {BORDER} !important;
}}
[data-testid="stSidebar"] * {{ color: {TEXT_PRIMARY} !important; }}
[data-testid="stSidebarNavLink"] {{
  border-radius: 8px !important;
  margin: 1px 6px !important;
  transition: all 0.2s !important;
  font-size: 0.88rem !important;
}}
[data-testid="stSidebarNavLink"]:hover {{
  background: {ORANGE_DIM} !important;
  color: {ORANGE_LIGHT} !important;
}}
[data-testid="stSidebarNavLink"][aria-current="page"] {{
  background: {ORANGE_DIM} !important;
  border-left: 2px solid {ORANGE} !important;
  color: {ORANGE} !important;
}}

/* ── Metric cards (glassmorphism + pulse glow) ── */
[data-testid="stMetric"] {{
  background: rgba(20,20,31,0.72) !important;
  backdrop-filter: blur(20px) saturate(180%) !important;
  border: 1px solid {BORDER} !important;
  border-top: 1px solid {ORANGE}33 !important;
  border-radius: 16px !important;
  padding: 1.1rem 1.3rem !important;
  animation: pulseGlow 3s ease-in-out infinite !important;
  transition: border-color 0.25s !important;
}}
[data-testid="stMetric"]:hover {{
  border-color: {ORANGE}66 !important;
  background: rgba(28,28,46,0.85) !important;
}}
[data-testid="stMetricLabel"] p {{
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.68rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.09em !important;
  text-transform: uppercase !important;
  color: {TEXT_SEC} !important;
}}
[data-testid="stMetricValue"] {{
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 1.55rem !important;
  font-weight: 500 !important;
  letter-spacing: -0.01em !important;
  color: {TEXT_PRIMARY} !important;
}}
[data-testid="stMetricDelta"] {{
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.72rem !important;
}}

/* ── Select / Multiselect ── */
.stSelectbox > div > div,
.stMultiSelect > div > div {{
  background: {BG_SURFACE} !important;
  border: 1px solid {BORDER} !important;
  color: {TEXT_PRIMARY} !important;
  border-radius: 10px !important;
  font-family: 'DM Sans', sans-serif !important;
}}
.stSelectbox > div > div:focus-within,
.stMultiSelect > div > div:focus-within {{
  border-color: {ORANGE} !important;
  box-shadow: 0 0 0 3px {ORANGE_DIM} !important;
}}

/* ── Checkbox & Radio ── */
[data-testid="stRadio"] label,
[data-testid="stCheckbox"] label {{
  color: {TEXT_PRIMARY} !important;
  font-family: 'DM Sans', sans-serif !important;
}}
[data-testid="stRadio"] div[data-baseweb="radio"] div,
[data-testid="stCheckbox"] div[data-baseweb="checkbox"] div {{
  background: {ORANGE} !important;
  border-color: {ORANGE} !important;
}}

/* ── Buttons ── */
.stButton > button {{
  background: linear-gradient(135deg, {ORANGE} 0%, {ORANGE_LIGHT} 100%) !important;
  color: {BG_PRIMARY} !important;
  border: none !important;
  border-radius: 10px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 600 !important;
  letter-spacing: 0.02em !important;
  transition: opacity 0.2s, transform 0.15s !important;
  box-shadow: 0 4px 20px {ORANGE_DIM} !important;
}}
.stButton > button:hover {{
  opacity: 0.85 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 28px {BORDER_GLOW} !important;
}}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {{
  background: {BG_SURFACE} !important;
  border: 1px solid {BORDER} !important;
  border-radius: 12px !important;
  padding: 4px !important;
  gap: 2px !important;
}}
.stTabs [data-baseweb="tab"] {{
  background: transparent !important;
  color: {TEXT_SEC} !important;
  border-radius: 9px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.82rem !important;
  font-weight: 500 !important;
  transition: all 0.2s !important;
  border-bottom: none !important;
}}
.stTabs [aria-selected="true"] {{
  background: {BG_ELEVATED} !important;
  color: {ORANGE} !important;
  border-bottom: 2px solid {ORANGE} !important;
}}
.stTabs [data-baseweb="tab-panel"] {{
  padding-top: 1.2rem !important;
}}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {{
  border: 1px solid {BORDER} !important;
  border-radius: 12px !important;
  overflow: hidden !important;
}}
[data-testid="stDataFrame"] th {{
  background: {BG_ELEVATED} !important;
  color: {TEXT_SEC} !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.7rem !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.07em !important;
  border-bottom: 1px solid {BORDER} !important;
}}
[data-testid="stDataFrame"] td {{
  background: {BG_SURFACE} !important;
  color: {TEXT_PRIMARY} !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.84rem !important;
  border-bottom: 1px solid {BORDER}66 !important;
}}
[data-testid="stDataFrame"] tr:hover td {{
  background: {BG_ELEVATED} !important;
}}

/* ── Alerts ── */
[data-testid="stAlert"] {{
  background: rgba(20,20,31,0.6) !important;
  backdrop-filter: blur(12px) !important;
  border: 1px solid {ORANGE}33 !important;
  border-radius: 10px !important;
  color: {TEXT_PRIMARY} !important;
  font-family: 'DM Sans', sans-serif !important;
}}

/* ── Expander ── */
[data-testid="stExpander"] {{
  background: {BG_SURFACE} !important;
  border: 1px solid {BORDER} !important;
  border-radius: 12px !important;
}}

/* ── Divider ── */
hr {{
  border: none !important;
  border-top: 1px solid {BORDER} !important;
  margin: 1.8rem 0 !important;
}}

/* ── Insight box (glassmorphism style) ── */
.insight-box {{
  background: rgba(20,20,31,0.6);
  backdrop-filter: blur(12px) saturate(160%);
  border: 1px solid {BORDER};
  border-left: 2px solid {ORANGE};
  border-radius: 0 12px 12px 0;
  padding: 0.75rem 1.15rem;
  margin: 0.3rem 0 1.2rem 0;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.86rem;
  color: {TEXT_SEC};
  line-height: 1.7;
  animation: fadeUp 0.5s ease forwards;
}}
.insight-box b {{ color: {ORANGE_LIGHT}; font-weight: 600; }}

/* ── Section header ── */
.section-header {{
  font-family: 'DM Sans', sans-serif;
  font-size: 1.05rem;
  font-weight: 600;
  color: {TEXT_PRIMARY};
  margin: 0.2rem 0 1rem 0;
  letter-spacing: -0.01em;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  animation: fadeUp 0.4s ease forwards;
}}

/* ── Page title (Playfair Display gradient — like Rajneeti) ── */
.page-title {{
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(1.8rem, 4vw, 2.4rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.15;
  background: linear-gradient(90deg, {ORANGE} 0%, {ORANGE_LIGHT} 50%, {TEXT_PRIMARY} 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0;
  animation: fadeUp 0.5s ease forwards;
}}

/* ── Section label (uppercase small caps) ── */
.section-label {{
  font-family: 'DM Sans', sans-serif;
  font-size: 0.62rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: {ORANGE};
  margin-bottom: 0.4rem;
}}

/* ── Stat card (glassmorphism + pulse glow — FAKENEWSDETECTOR inspired) ── */
.stat-card {{
  background: rgba(20,20,31,0.72);
  backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid {BORDER};
  border-top: 1px solid {ORANGE}33;
  border-radius: 16px;
  padding: 1.1rem 1.3rem;
  transition: border-color 0.25s, box-shadow 0.25s;
  animation: fadeUp 0.5s ease forwards;
  box-shadow: 0 2px 20px rgba(0,0,0,0.3), 0 1px 4px rgba(0,0,0,0.2);
}}
.stat-card:hover {{
  border-color: {ORANGE}55;
  box-shadow: 0 8px 40px rgba(255,107,53,0.12), 0 2px 8px rgba(0,0,0,0.4);
}}
.stat-card .label {{
  font-family: 'DM Sans', sans-serif;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: {TEXT_SEC};
  margin-bottom: 0.3rem;
}}
.stat-card .value {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.65rem;
  font-weight: 500;
  color: {TEXT_PRIMARY};
  letter-spacing: -0.02em;
  line-height: 1.1;
}}
.stat-card .delta {{
  font-family: 'DM Sans', sans-serif;
  font-size: 0.72rem;
  color: {TEAL};
  margin-top: 0.25rem;
  font-weight: 500;
}}
.stat-card .delta.neg {{ color: {RED}; }}

/* ── Milestone card ── */
.milestone-card {{
  background: rgba(20,20,31,0.55);
  backdrop-filter: blur(16px) saturate(160%);
  border: 1px solid {BORDER};
  border-radius: 14px;
  padding: 1rem 1.2rem;
  transition: all 0.25s;
  animation: fadeUp 0.5s ease forwards;
}}
.milestone-card:hover {{
  border-color: {ORANGE}44;
  background: rgba(28,28,46,0.8);
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(255,107,53,0.1);
}}

/* ── Badge ── */
.badge {{
  display: inline-block;
  padding: 2px 10px;
  border-radius: 999px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  background: {ORANGE_DIM};
  color: {ORANGE_LIGHT};
  border: 1px solid {ORANGE}33;
}}
.badge-teal {{
  background: rgba(0,201,167,0.1);
  color: {TEAL};
  border-color: {TEAL}33;
}}

/* ── Why-box (glassmorphism info card) ── */
.why-box {{
  background: rgba(20,20,31,0.6);
  backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid {BORDER};
  border-radius: 16px;
  padding: 1.4rem 1.7rem;
  margin-bottom: 2rem;
  animation: fadeUp 0.6s ease forwards;
  box-shadow: 0 4px 32px rgba(0,0,0,0.25), inset 0 1px 0 rgba(255,255,255,0.04);
}}

/* ── Shimmer text (like FAKENEWSDETECTOR TextShimmer) ── */
.shimmer-text {{
  background: linear-gradient(
    90deg,
    {TEXT_PRIMARY} 0%,
    {ORANGE} 30%,
    {ORANGE_LIGHT} 50%,
    {TEXT_PRIMARY} 70%,
    {TEXT_PRIMARY} 100%
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 3s linear infinite;
}}

/* ── Scorecard row ── */
.scorecard {{
  background: rgba(20,20,31,0.55);
  backdrop-filter: blur(12px);
  border: 1px solid {BORDER};
  border-radius: 12px;
  padding: 0.9rem 1.1rem;
  margin-bottom: 0.6rem;
  transition: all 0.2s;
}}
.scorecard:hover {{
  border-color: {TEAL}44;
  background: rgba(28,28,46,0.8);
}}

/* ── Footer ── */
.footer {{
  margin-top: 4rem;
  padding-top: 1.4rem;
  border-top: 1px solid {BORDER};
  font-family: 'DM Sans', sans-serif;
  font-size: 0.73rem;
  color: {TEXT_MUTED};
  text-align: center;
  letter-spacing: 0.01em;
}}
.footer a {{ color: {ORANGE}; text-decoration: none; transition: color 0.2s; }}
.footer a:hover {{ color: {ORANGE_LIGHT}; }}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header {{ visibility: hidden; }}
[data-testid="stDecoration"] {{ display: none; }}

/* ── Stagger delay helpers ── */
.delay-100 {{ animation-delay: 0.1s; opacity: 0; }}
.delay-200 {{ animation-delay: 0.2s; opacity: 0; }}
.delay-300 {{ animation-delay: 0.3s; opacity: 0; }}
.delay-400 {{ animation-delay: 0.4s; opacity: 0; }}
.delay-500 {{ animation-delay: 0.5s; opacity: 0; }}
</style>
"""


def footer_html() -> str:
    return f"""
<div class="footer">
  Data sources: &nbsp;
  <a href="https://indiabudget.gov.in" target="_blank">indiabudget.gov.in</a>
  &nbsp;·&nbsp;
  <a href="https://data.gov.in" target="_blank">data.gov.in</a>
  &nbsp;·&nbsp;
  <a href="https://rbi.org.in" target="_blank">RBI DBIE</a>
  &nbsp;·&nbsp;
  <a href="https://mospi.gov.in" target="_blank">MOSPI</a>
  &nbsp;·&nbsp;
  <a href="https://fincom15.gov.in" target="_blank">Finance Commission XV</a>
  <br/><br/>
  <span style="color:{TEXT_MUTED}; letter-spacing:0.04em;">
    Built with public data for public good &nbsp;·&nbsp; BharatBudget 2025
  </span>
</div>
"""


def insight_box(text: str) -> str:
    return f'<div class="insight-box">💡 {text}</div>'


def page_header(icon: str, title: str, subtitle: str) -> str:
    """Premium page header with Playfair Display title."""
    return f"""
<div style="padding: 0.2rem 0 1.4rem 0; animation: fadeUp 0.5s ease forwards;">
  <div class="section-label">{icon} BharatBudget</div>
  <div class="page-title">{title}</div>
  <p style="font-family:'DM Sans',sans-serif; color:{TEXT_SEC};
            font-size:0.92rem; margin:0.4rem 0 0 0; max-width:640px;">
    {subtitle}
  </p>
</div>
"""
