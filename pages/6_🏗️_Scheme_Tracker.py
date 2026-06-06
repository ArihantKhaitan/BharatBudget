"""Flagship Scheme Tracker — Are government schemes reaching people?"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from utils.styling import (
    footer_html, insight_box, page_header,
    ORANGE, ORANGE_LIGHT, TEAL, RED, BLUE_SOFT, TEXT_PRIMARY, TEXT_SEC, TEXT_MUTED,
    BORDER, GRID_COLOR, PLOTLY_PAPER, PLOTLY_PLOT, BG_SURFACE, BG_ELEVATED,
)
from data.schemes import (
    BUDGET_YEARS,
    MGNREGA_EXPENDITURE_LCR, MGNREGA_HOUSEHOLDS_CR,
    PM_KISAN_EXPENDITURE_LCR, PM_KISAN_BENEFICIARIES_CR,
    PMJAY_EXPENDITURE_LCR, PMJAY_CLAIMS_CR,
    PMAYG_HOUSES_COMPLETED_LAKH, PMAYG_EXPENDITURE_LCR,
    JJM_TAP_CONNECTIONS_CR_CUMULATIVE, JJM_EXPENDITURE_LCR,
    UJJWALA_CONNECTIONS_CR, UJJWALA_EXPENDITURE_LCR,
    STATE_PMAYG_2023_24, STATE_MGNREGA_PERSONDAYS_2023_24,
)

st.markdown(
    page_header(
        "🏗️",
        "Flagship Scheme Tracker",
        "Are government schemes reaching people? Track expenditure and beneficiaries for MGNREGA, PM-KISAN, Ayushman Bharat, PM Awas, Jal Jeevan Mission, and more.",
    ),
    unsafe_allow_html=True,
)
st.markdown("---")

# ── Overview cards ────────────────────────────────────────────────────────────
schemes_overview = [
    ("🔨 MGNREGA",          "7.5 cr households",  "COVID peak 2020-21", "₹1.11 L cr peak spend"),
    ("🌾 PM-KISAN",         "11 cr farmers",      "₹6,000/yr each",    "₹0.66 L cr/yr"),
    ("🏥 Ayushman Bharat",  "1.8 cr claims/yr",   "₹5L cover/family",  "₹0.90 L cr 2024-25"),
    ("🏠 PMAY-Gramin",      "55 L houses/yr",     "₹1.2-1.4 L/house",  "₹0.31 L cr 2023-24"),
    ("💧 Jal Jeevan Mission","15.2 cr connections","Rural tap water",   "₹0.77 L cr 2024-25"),
    ("🔥 PM Ujjwala",       "10.2 cr LPG conns",  "Free to BPL women", "₹0.18 L cr/yr"),
]
cols = st.columns(3)
for i, (name, stat1, stat2, spend) in enumerate(schemes_overview):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class='stat-card' style='margin-bottom:0.8rem;'>
              <div style='font-family:"DM Sans",sans-serif; font-size:0.87rem; font-weight:600;
                          color:{TEXT_PRIMARY}; margin-bottom:0.4rem;'>{name}</div>
              <div style='font-family:"JetBrains Mono",monospace; font-size:1.1rem;
                          font-weight:500; color:{ORANGE}; line-height:1;'>{stat1}</div>
              <div style='font-family:"DM Sans",sans-serif; font-size:0.73rem;
                          color:{TEXT_SEC}; margin-top:0.2rem;'>{stat2} &nbsp;·&nbsp; {spend}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")

# ── Page controls (inline) ────────────────────────────────────────────────────
scheme_choice = st.selectbox("Select Scheme to Deep Dive", [
    "MGNREGA", "PM-KISAN", "Ayushman Bharat PM-JAY",
    "PM Awas Yojana Gramin", "Jal Jeevan Mission", "PM Ujjwala Yojana",
])

# ── Deep-dive on selected scheme ─────────────────────────────────────────────
st.markdown(
    f"<div class='section-label'>🔍 &nbsp; Deep Dive: {scheme_choice}</div>",
    unsafe_allow_html=True,
)

def line_bar_chart(years, bar_vals, line_vals, bar_name, line_name,
                   bar_color, line_color, bar_suffix="", line_suffix="") -> go.Figure:
    valid = [(y, b, l) for y, b, l in zip(years, bar_vals, line_vals)
             if b is not None and l is not None]
    if not valid:
        return go.Figure()
    yv, bv, lv = zip(*valid)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=yv, y=bv, name=bar_name, marker_color=bar_color,
        hovertemplate=f"%{{x}}: %{{y:.2f}}{bar_suffix}<extra>{bar_name}</extra>",
        text=[f"{v:.2f}" for v in bv], textposition="outside",
        textfont=dict(color=TEXT_MUTED, size=9),
    ))
    fig.add_trace(go.Scatter(
        x=yv, y=lv, name=line_name, yaxis="y2",
        mode="lines+markers", line=dict(color=line_color, width=2.5, dash="dot"),
        marker=dict(size=7, color=line_color),
        hovertemplate=f"%{{x}}: %{{y:.2f}}{line_suffix}<extra>{line_name}</extra>",
    ))
    fig.update_layout(
        paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
        height=320,
        margin=dict(l=8, r=60, t=12, b=8),
        legend=dict(bgcolor="rgba(245,237,216,0.9)", bordercolor=BORDER,
                    borderwidth=1, font=dict(color=TEXT_SEC, size=11),
                    orientation="h", y=1.12),
        xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
        yaxis=dict(title=dict(text=bar_name, font=dict(color=TEXT_SEC)),
                   gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
        yaxis2=dict(title=dict(text=line_name, font=dict(color=line_color)),
                    overlaying="y", side="right",
                    tickfont=dict(color=line_color), gridcolor="rgba(0,0,0,0)"),
    )
    return fig

if scheme_choice == "MGNREGA":
    yrs = BUDGET_YEARS
    fig = line_bar_chart(
        yrs, [MGNREGA_EXPENDITURE_LCR[y] for y in yrs],
        [MGNREGA_HOUSEHOLDS_CR[y] for y in yrs],
        "Expenditure (₹ L cr)", "Households Employed (cr)",
        ORANGE, TEAL, " L cr", " cr",
    )
    st.plotly_chart(fig, width='stretch')
    st.markdown(insight_box(
        "MGNREGA — India's largest rural employment guarantee — peaked at <b>₹1.11 L cr</b> in 2020-21 "
        "when <b>7.5 crore households</b> relied on it during COVID lockdowns. "
        "It acts as an automatic stabiliser: spending spikes in distress years."
    ), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='section-label'>🗺️ &nbsp; State-wise MGNREGA Activity (FY 2023-24)</div>",
        unsafe_allow_html=True,
    )
    sorted_mgnrega = sorted(STATE_MGNREGA_PERSONDAYS_2023_24.items(), key=lambda x: x[1], reverse=True)
    df_m = pd.DataFrame(sorted_mgnrega, columns=["State", "Person-days (cr)"])
    fig2 = go.Figure(go.Bar(
        x=df_m["Person-days (cr)"], y=df_m["State"], orientation="h",
        marker=dict(color=df_m["Person-days (cr)"],
                    colorscale=[[0, BG_ELEVATED], [0.5, ORANGE_LIGHT], [1, ORANGE]]),
        hovertemplate="%{y}: %{x:.1f} cr person-days<extra></extra>",
    ))
    fig2.update_layout(
        paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_PRIMARY), height=520,
        margin=dict(l=8, r=20, t=12, b=8),
        xaxis=dict(title=dict(text="Crore Person-days", font=dict(color=TEXT_SEC)),
                   gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
        yaxis=dict(gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    )
    st.plotly_chart(fig2, width='stretch')

elif scheme_choice == "PM-KISAN":
    yrs = [y for y in BUDGET_YEARS if PM_KISAN_EXPENDITURE_LCR.get(y) is not None]
    fig = line_bar_chart(
        yrs, [PM_KISAN_EXPENDITURE_LCR[y] for y in yrs],
        [PM_KISAN_BENEFICIARIES_CR[y] for y in yrs],
        "Expenditure (₹ L cr)", "Farmer Beneficiaries (cr)",
        "#3A7D3A", ORANGE, " L cr", " cr",
    )
    st.plotly_chart(fig, width='stretch')
    st.markdown(insight_box(
        "PM-KISAN provides <b>₹6,000 per year (₹500/month)</b> to ~11 crore farmers. "
        "Annual expenditure is capped near <b>₹0.66 L cr</b> — stable since 2022. "
        "Despite scale, ₹6,000/yr amounts to just <b>₹16.4/day per farmer</b>."
    ), unsafe_allow_html=True)

elif scheme_choice == "Ayushman Bharat PM-JAY":
    yrs = [y for y in BUDGET_YEARS if PMJAY_EXPENDITURE_LCR.get(y) is not None]
    fig = line_bar_chart(
        yrs, [PMJAY_EXPENDITURE_LCR[y] for y in yrs],
        [PMJAY_CLAIMS_CR[y] for y in yrs],
        "Expenditure (₹ L cr)", "Hospitalisation Claims (cr)",
        "#7B3A9E", ORANGE, " L cr", " cr",
    )
    st.plotly_chart(fig, width='stretch')
    st.markdown(insight_box(
        "Ayushman Bharat PM-JAY — the world's largest government-funded health insurance — covers "
        "<b>₹5 lakh per family per year</b> for secondary and tertiary hospitalisation. "
        "Claims have surged from 0.07 cr (2018-19) to <b>1.8 cr</b> (2024-25). "
        "But out-of-pocket health costs are still ~45% of total health spend."
    ), unsafe_allow_html=True)

elif scheme_choice == "PM Awas Yojana Gramin":
    yrs = BUDGET_YEARS
    fig = line_bar_chart(
        yrs, [PMAYG_EXPENDITURE_LCR[y] for y in yrs],
        [PMAYG_HOUSES_COMPLETED_LAKH[y] for y in yrs],
        "Expenditure (₹ L cr)", "Houses Completed (lakh)",
        "#9A7000", ORANGE, " L cr", " lakh",
    )
    st.plotly_chart(fig, width='stretch')
    st.markdown(insight_box(
        "PMAY-G targets <b>pucca (permanent) housing</b> for rural poor. "
        "Peak completion was 85 lakh houses in 2018-19. COVID disrupted construction in 2020-21. "
        "Each house subsidy is ₹1.2 lakh (plains) or ₹1.4 lakh (hilly areas)."
    ), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='section-label'>🗺️ &nbsp; State-wise PMAY-G Houses (FY 2023-24)</div>",
        unsafe_allow_html=True,
    )
    sorted_pmay = sorted(STATE_PMAYG_2023_24.items(), key=lambda x: x[1], reverse=True)
    df_p = pd.DataFrame(sorted_pmay, columns=["State", "Houses Completed (lakh)"])
    fig2 = go.Figure(go.Bar(
        x=df_p["Houses Completed (lakh)"], y=df_p["State"], orientation="h",
        marker=dict(color=df_p["Houses Completed (lakh)"],
                    colorscale=[[0, BG_ELEVATED], [0.5, "#D4B020"], [1, "#9A7000"]]),
        hovertemplate="%{y}: %{x:.1f} lakh houses<extra></extra>",
    ))
    fig2.update_layout(
        paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_PRIMARY), height=480,
        margin=dict(l=8, r=20, t=12, b=8),
        xaxis=dict(title=dict(text="Lakh Houses", font=dict(color=TEXT_SEC)),
                   gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
        yaxis=dict(gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    )
    st.plotly_chart(fig2, width='stretch')

elif scheme_choice == "Jal Jeevan Mission":
    yrs = BUDGET_YEARS
    fig = line_bar_chart(
        yrs, [JJM_EXPENDITURE_LCR[y] for y in yrs],
        [JJM_TAP_CONNECTIONS_CR_CUMULATIVE[y] for y in yrs],
        "Expenditure (₹ L cr)", "Cumulative Tap Connections (cr)",
        "#0A7A9A", ORANGE, " L cr", " cr",
    )
    st.plotly_chart(fig, width='stretch')
    st.markdown(insight_box(
        "Launched in 2019, Jal Jeevan Mission aims for <b>'Har Ghar Jal' — tap water to every rural home</b>. "
        "Coverage surged from 3.2 cr connections (2019-20) to <b>15.2 cr</b> (2024-25). "
        "In 5 years, more tap connections were added than in the previous 70 years combined."
    ), unsafe_allow_html=True)

elif scheme_choice == "PM Ujjwala Yojana":
    yrs = BUDGET_YEARS
    fig = line_bar_chart(
        yrs, [UJJWALA_EXPENDITURE_LCR[y] for y in yrs],
        [UJJWALA_CONNECTIONS_CR[y] for y in yrs],
        "Expenditure (₹ L cr)", "LPG Connections (cr)",
        "#E06820", TEAL, " L cr", " cr",
    )
    st.plotly_chart(fig, width='stretch')
    st.markdown(insight_box(
        "PM Ujjwala Yojana gave <b>free LPG connections to BPL (Below Poverty Line) households</b>, "
        "primarily targeting women in rural areas. Over <b>10 crore connections</b> provided. "
        "Challenge: many beneficiaries can't afford refills — actual usage rates vary."
    ), unsafe_allow_html=True)

st.markdown(footer_html(), unsafe_allow_html=True)
