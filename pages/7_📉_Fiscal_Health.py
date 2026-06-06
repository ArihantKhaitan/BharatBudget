"""Fiscal Health — Deficit, Debt, and India's financial sustainability."""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from utils.styling import (
    footer_html, insight_box, page_header,
    ORANGE, ORANGE_LIGHT, TEAL, RED, BLUE_SOFT, TEXT_PRIMARY, TEXT_SEC, TEXT_MUTED,
    BORDER, GRID_COLOR, PLOTLY_PAPER, PLOTLY_PLOT,
)
from data.fiscal import (
    BUDGET_YEARS, FISCAL_DEFICIT_LCR, FISCAL_DEFICIT_PCT_GDP,
    CENTRAL_GOVT_DEBT_LCR, DEBT_TO_GDP_PCT,
    CAPITAL_EXPENDITURE_LCR,
    REVENUE_EXPENDITURE_LCR,
    INTEREST_AS_PCT_REVENUE,
)

st.markdown(
    page_header(
        "📉",
        "Fiscal Health Dashboard",
        "Is India spending within its means? Track the fiscal deficit, government debt, borrowings, and the shift from consumption spending to capital investment.",
    ),
    unsafe_allow_html=True,
)
st.markdown("---")

# ── Key metrics ───────────────────────────────────────────────────────────────
latest = "2024-25"
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Fiscal Deficit 2024-25", f"₹{FISCAL_DEFICIT_LCR[latest]:.2f} L cr",
              f"{FISCAL_DEFICIT_PCT_GDP[latest]:.1f}% of GDP")
with c2:
    st.metric("Central Govt Debt", f"₹{CENTRAL_GOVT_DEBT_LCR[latest]:.0f} L cr",
              f"{DEBT_TO_GDP_PCT[latest]:.1f}% of GDP")
with c3:
    capex = CAPITAL_EXPENDITURE_LCR[latest]
    total = capex + REVENUE_EXPENDITURE_LCR[latest]
    st.metric("Capital Expenditure 2024-25", f"₹{capex:.2f} L cr",
              f"{capex/total*100:.1f}% of total expenditure")
with c4:
    _interest_val = INTEREST_AS_PCT_REVENUE[latest]
    st.metric("Interest as % of Revenue", f"{_interest_val:.1f}%",
              f"Every ₹{100/_interest_val:.1f} of revenue, ₹1 is interest")

st.markdown("<br>", unsafe_allow_html=True)

# ── Section 1: Fiscal deficit trend ──────────────────────────────────────────
st.markdown(
    f"<div class='section-label'>📊 &nbsp; Fiscal Deficit — Absolute & as % of GDP</div>",
    unsafe_allow_html=True,
)

fig_fd = go.Figure()
colors_fd = [RED if v > 3.5 else TEAL for v in FISCAL_DEFICIT_PCT_GDP.values()]
fig_fd.add_trace(go.Bar(
    x=BUDGET_YEARS, y=list(FISCAL_DEFICIT_PCT_GDP.values()),
    name="Fiscal Deficit % GDP",
    marker=dict(color=colors_fd),
    text=[f"{v:.1f}%" for v in FISCAL_DEFICIT_PCT_GDP.values()],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=9),
    hovertemplate="%{x}: %{y:.1f}% of GDP<extra></extra>",
))
fig_fd.add_hline(y=3.5, line_dash="dash", line_color=ORANGE, opacity=0.8,
                 annotation_text="FRBM target: 3.5%",
                 annotation_font_color=ORANGE, annotation_bgcolor="rgba(245,237,216,0.8)")
fig_fd.add_trace(go.Scatter(
    x=BUDGET_YEARS, y=list(FISCAL_DEFICIT_LCR.values()),
    name="₹ Lakh Crore", yaxis="y2", mode="lines+markers",
    line=dict(color=BLUE_SOFT, width=2, dash="dot"),
    marker=dict(size=6, color=BLUE_SOFT),
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra></extra>",
))
fig_fd.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=340,
    margin=dict(l=8, r=60, t=16, b=8),
    legend=dict(bgcolor="rgba(245,237,216,0.9)", bordercolor=BORDER,
                borderwidth=1, font=dict(color=TEXT_SEC, size=11),
                orientation="h", y=1.12),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="% of GDP", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    yaxis2=dict(title=dict(text="₹ Lakh Crore", font=dict(color=BLUE_SOFT)),
                overlaying="y", side="right",
                tickfont=dict(color=BLUE_SOFT), gridcolor="rgba(0,0,0,0)"),
)
st.plotly_chart(fig_fd, width='stretch')
st.markdown(insight_box(
    "India's FRBM (Fiscal Responsibility) target is <b>3% of GDP by 2025-26</b>. "
    "The <b>COVID-19 year (2020-21)</b> blew out the deficit to <b>9.4% of GDP</b> — the worst since liberalisation. "
    "Since then, fiscal consolidation has been rapid: down to <b>4.9% in 2024-25</b>. "
    "Green bars = within FRBM target; red = above."
), unsafe_allow_html=True)

# ── Section 2: Debt trajectory ────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-label'>🏦 &nbsp; Government Debt — Is It Sustainable?</div>",
    unsafe_allow_html=True,
)

fig_debt = go.Figure()
fig_debt.add_trace(go.Bar(
    x=BUDGET_YEARS, y=list(CENTRAL_GOVT_DEBT_LCR.values()),
    name="Debt (₹ L cr)", marker_color=ORANGE_LIGHT,
    hovertemplate="%{x}: ₹%{y:.0f} L cr<extra></extra>",
))
fig_debt.add_trace(go.Scatter(
    x=BUDGET_YEARS, y=list(DEBT_TO_GDP_PCT.values()),
    name="Debt % GDP", yaxis="y2", mode="lines+markers",
    line=dict(color=RED, width=2.5),
    marker=dict(size=7, color=RED),
    hovertemplate="%{x}: %{y:.1f}% of GDP<extra></extra>",
))
fig_debt.add_hline(y=60, line_dash="dot", line_color=RED, opacity=0.5,
                   annotation_text="IMF 60% warning threshold",
                   annotation_font_color=RED, yref="y2")
fig_debt.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=320,
    margin=dict(l=8, r=60, t=12, b=8),
    legend=dict(bgcolor="rgba(245,237,216,0.9)", bordercolor=BORDER,
                borderwidth=1, font=dict(color=TEXT_SEC, size=11),
                orientation="h", y=1.12),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="₹ Lakh Crore", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    yaxis2=dict(title=dict(text="% of GDP", font=dict(color=RED)),
                overlaying="y", side="right",
                tickfont=dict(color=RED), gridcolor="rgba(0,0,0,0)",
                range=[40, 70]),
)
st.plotly_chart(fig_debt, width='stretch')
st.markdown(insight_box(
    "India's central government debt crossed the <b>IMF's 60% GDP warning threshold in 2020-21</b> "
    "due to COVID borrowings. It's now declining — projected at <b>53.8% in 2024-25</b>. "
    "India's debt is mostly <b>domestic (rupee-denominated)</b>, reducing currency risk, "
    "but rising interest payments eat into productive spending."
), unsafe_allow_html=True)

# ── Section 3: Capex vs Revex ─────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-label'>🏗️ &nbsp; Capital vs Revenue Expenditure</div>",
    unsafe_allow_html=True,
)

capex_vals = list(CAPITAL_EXPENDITURE_LCR.values())
revex_vals = list(REVENUE_EXPENDITURE_LCR.values())
capex_pct  = [c / (c + r) * 100 for c, r in zip(capex_vals, revex_vals)]

fig_cr = go.Figure()
fig_cr.add_trace(go.Bar(
    x=BUDGET_YEARS, y=capex_vals, name="Capital Expenditure (₹ L cr)",
    marker_color=TEAL,
    hovertemplate="%{x}: ₹%{y:.2f} L cr capex<extra></extra>",
))
fig_cr.add_trace(go.Bar(
    x=BUDGET_YEARS, y=revex_vals, name="Revenue Expenditure (₹ L cr)",
    marker_color="#D4C9B0",
    hovertemplate="%{x}: ₹%{y:.2f} L cr revex<extra></extra>",
))
fig_cr.add_trace(go.Scatter(
    x=BUDGET_YEARS, y=capex_pct, name="Capex as % total", yaxis="y2",
    mode="lines+markers", line=dict(color=ORANGE, width=2.5),
    marker=dict(size=7, color=ORANGE),
    hovertemplate="%{x}: %{y:.1f}% capex share<extra></extra>",
))
fig_cr.update_layout(
    barmode="stack",
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=350,
    margin=dict(l=8, r=60, t=12, b=8),
    legend=dict(bgcolor="rgba(245,237,216,0.9)", bordercolor=BORDER,
                borderwidth=1, font=dict(color=TEXT_SEC, size=11),
                orientation="h", y=-0.18),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="₹ Lakh Crore", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    yaxis2=dict(title=dict(text="Capex %", font=dict(color=ORANGE)),
                overlaying="y", side="right",
                tickfont=dict(color=ORANGE), gridcolor="rgba(0,0,0,0)"),
)
st.plotly_chart(fig_cr, width='stretch')
st.markdown(insight_box(
    "<b>Capital expenditure creates assets</b> (roads, bridges, schools); "
    "<b>revenue expenditure pays salaries, pensions, interest</b>. "
    "India's capex share has dramatically risen from <b>11% (2015-16) to ~23% (2024-25)</b> — "
    "a core Modi-era policy push. Capex has a higher economic multiplier (~2.5x vs 1x for revex)."
), unsafe_allow_html=True)

# ── Section 4: Interest burden ────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-label'>💳 &nbsp; Interest Burden — The Hidden Cost of Debt</div>",
    unsafe_allow_html=True,
)

interest_pct = list(INTEREST_AS_PCT_REVENUE.values())
fig_int = go.Figure(go.Scatter(
    x=BUDGET_YEARS, y=interest_pct,
    mode="lines+markers+text",
    line=dict(color=RED, width=2.5),
    marker=dict(size=8, color=[RED if v > 40 else ORANGE for v in interest_pct],
                line=dict(width=1.5, color="white")),
    text=[f"{v:.1f}%" for v in interest_pct],
    textposition="top center",
    textfont=dict(color=TEXT_MUTED, size=9),
    fill="tozeroy",
    fillcolor="rgba(164,46,46,0.07)",
    hovertemplate="%{x}: %{y:.1f}% of revenue receipts<extra></extra>",
))
fig_int.add_hline(y=33.3, line_dash="dash", line_color=ORANGE,
                  annotation_text="1-in-3 threshold (33%)",
                  annotation_font_color=ORANGE)
fig_int.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=280,
    margin=dict(l=8, r=8, t=12, b=8),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="% of Revenue Receipts", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC), range=[28, 52]),
)
st.plotly_chart(fig_int, width='stretch')
st.markdown(insight_box(
    "India spends roughly <b>₹1 in every ₹3 of revenue on just paying interest</b> on past debt. "
    "This 'interest burden' peaked at <b>47.2%</b> in 2020-21. "
    "High interest burden means less money for hospitals, schools, and roads. "
    "Reducing debt is crucial for India's long-term development capacity."
), unsafe_allow_html=True)

st.markdown(footer_html(), unsafe_allow_html=True)
