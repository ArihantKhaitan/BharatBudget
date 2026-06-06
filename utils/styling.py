"""Centralised CSS + Plotly theme for BharatBudget."""

# ── Colour palette ────────────────────────────────────────────────────────────
NAVY        = "#0B1437"
NAVY_CARD   = "#131E3A"
NAVY_LIGHT  = "#1E3A5F"
ORANGE      = "#FF9933"
ORANGE_DARK = "#E07800"
TEAL        = "#00C49A"
RED         = "#E84040"
BLUE_SOFT   = "#4FC3F7"
TEXT_MAIN   = "#E8EDF5"
TEXT_MUTED  = "#8B9CC7"
GRID_COLOR  = "#1E3A5F"

# Plotly paper/plot background colours
PLOTLY_PAPER_BG = "#0B1437"
PLOTLY_PLOT_BG  = "#131E3A"

MINISTRY_COLOR_MAP = {
    "Defence":                   "#E84040",
    "Interest Payments":         "#9E9E9E",
    "Road Transport & Highways": "#FF9933",
    "Railways":                  "#FFB347",
    "Rural Development":         "#00C49A",
    "Home Affairs":              "#E57373",
    "Education":                 "#4FC3F7",
    "Agriculture & Allied":      "#81C784",
    "Health & Family Welfare":   "#BA68C8",
    "Communications & IT":       "#64B5F6",
    "Jal Shakti / Water":        "#29B6F6",
    "Housing & Urban Affairs":   "#FFF176",
    "Food & Public Distribution":"#A5D6A7",
    "Fertiliser Subsidy":        "#C8E6C9",
    "Science & Space":           "#CE93D8",
    "Social Welfare":            "#F48FB1",
    "State Transfers (CSS)":     "#80CBC4",
    "Others":                    "#546E7A",
}


def get_plotly_layout(title: str = "", height: int = 420) -> dict:
    """Return a standard dark-themed Plotly layout dict."""
    return dict(
        title=dict(text=title, font=dict(color=TEXT_MAIN, size=16), x=0.02),
        paper_bgcolor=PLOTLY_PAPER_BG,
        plot_bgcolor=PLOTLY_PLOT_BG,
        font=dict(color=TEXT_MAIN, family="Inter, sans-serif"),
        height=height,
        margin=dict(l=16, r=16, t=48, b=16),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            bordercolor=GRID_COLOR,
            font=dict(color=TEXT_MUTED, size=11),
        ),
        xaxis=dict(
            gridcolor=GRID_COLOR,
            linecolor=GRID_COLOR,
            tickfont=dict(color=TEXT_MUTED),
            title_font=dict(color=TEXT_MUTED),
            zeroline=False,
        ),
        yaxis=dict(
            gridcolor=GRID_COLOR,
            linecolor=GRID_COLOR,
            tickfont=dict(color=TEXT_MUTED),
            title_font=dict(color=TEXT_MUTED),
            zeroline=False,
        ),
    )


# ── Global Streamlit CSS ──────────────────────────────────────────────────────
GLOBAL_CSS = f"""
<style>
  /* ---------- App background ---------- */
  .stApp, .main {{
    background-color: {NAVY} !important;
    color: {TEXT_MAIN} !important;
  }}
  .main .block-container {{
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
  }}

  /* ---------- Sidebar ---------- */
  [data-testid="stSidebar"] {{
    background-color: #071029 !important;
    border-right: 1px solid {NAVY_LIGHT};
  }}
  [data-testid="stSidebar"] * {{
    color: {TEXT_MAIN} !important;
  }}

  /* ---------- Metric cards ---------- */
  [data-testid="stMetric"] {{
    background: linear-gradient(135deg, {NAVY_CARD}, {NAVY_LIGHT}33);
    border: 1px solid {NAVY_LIGHT};
    border-left: 3px solid {ORANGE};
    border-radius: 10px;
    padding: 1rem 1.2rem;
  }}
  [data-testid="stMetricLabel"] {{
    color: {TEXT_MUTED} !important;
    font-size: 0.8rem !important;
  }}
  [data-testid="stMetricValue"] {{
    color: {TEXT_MAIN} !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
  }}
  [data-testid="stMetricDelta"] {{
    font-size: 0.8rem !important;
  }}

  /* ---------- Selectbox / inputs ---------- */
  .stSelectbox > div > div,
  .stMultiSelect > div > div {{
    background-color: {NAVY_CARD} !important;
    border: 1px solid {NAVY_LIGHT} !important;
    color: {TEXT_MAIN} !important;
    border-radius: 8px;
  }}

  /* ---------- Buttons ---------- */
  .stButton > button {{
    background: linear-gradient(90deg, {ORANGE}, {ORANGE_DARK});
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
  }}
  .stButton > button:hover {{
    opacity: 0.88;
  }}

  /* ---------- Radio pills ---------- */
  [data-testid="stRadio"] label {{
    color: {TEXT_MAIN} !important;
  }}

  /* ---------- Plotly charts ---------- */
  .js-plotly-plot .plotly {{
    border-radius: 12px;
    overflow: hidden;
  }}

  /* ---------- Divider ---------- */
  hr {{
    border-color: {NAVY_LIGHT} !important;
    margin: 1.2rem 0;
  }}

  /* ---------- Expander ---------- */
  [data-testid="stExpander"] {{
    background-color: {NAVY_CARD} !important;
    border: 1px solid {NAVY_LIGHT} !important;
    border-radius: 8px !important;
  }}

  /* ---------- Insight boxes ---------- */
  .insight-box {{
    background: {NAVY_CARD};
    border-left: 3px solid {ORANGE};
    border-radius: 0 8px 8px 0;
    padding: 0.65rem 1rem;
    margin: 0.4rem 0 1rem 0;
    font-size: 0.88rem;
    color: {TEXT_MUTED};
    line-height: 1.6;
  }}
  .insight-box b {{ color: {ORANGE}; }}

  /* ---------- Section headers ---------- */
  .section-header {{
    font-size: 1.3rem;
    font-weight: 700;
    color: {TEXT_MAIN};
    margin-bottom: 0.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }}

  /* ---------- Footer ---------- */
  .footer {{
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 1px solid {NAVY_LIGHT};
    font-size: 0.78rem;
    color: {TEXT_MUTED};
    text-align: center;
  }}
  .footer a {{ color: {ORANGE}; text-decoration: none; }}
  .footer a:hover {{ text-decoration: underline; }}

  /* ---------- Tag badges ---------- */
  .badge {{
    display: inline-block;
    padding: 2px 10px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 600;
    background: {ORANGE}22;
    color: {ORANGE};
    border: 1px solid {ORANGE}55;
  }}

  /* ---------- Hide default Streamlit decoration ---------- */
  #MainMenu, footer, header {{ visibility: hidden; }}
</style>
"""


def footer_html() -> str:
    return """
<div class="footer">
  📊 Data sources:&nbsp;
  <a href="https://indiabudget.gov.in" target="_blank">indiabudget.gov.in</a> &nbsp;|&nbsp;
  <a href="https://data.gov.in" target="_blank">data.gov.in</a> &nbsp;|&nbsp;
  <a href="https://rbi.org.in/scripts/DBIE.aspx" target="_blank">RBI DBIE</a> &nbsp;|&nbsp;
  <a href="https://mospi.gov.in" target="_blank">MOSPI</a> &nbsp;|&nbsp;
  <a href="https://fincom15.gov.in" target="_blank">Finance Commission XV</a>
  <br/>
  <span style="opacity:0.6;">Built with public data for public good · BharatBudget 2025</span>
</div>
"""


def insight_box(text: str) -> str:
    return f'<div class="insight-box">💡 {text}</div>'
