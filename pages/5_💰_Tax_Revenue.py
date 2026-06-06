"""Tax Revenue Tracker — Where does India's tax money come FROM?"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from utils.styling import (
    footer_html, insight_box, page_header,
    ORANGE, ORANGE_LIGHT, TEAL, RED, BLUE_SOFT, TEXT_PRIMARY, TEXT_SEC, TEXT_MUTED,
    BORDER, GRID_COLOR, PLOTLY_PAPER, PLOTLY_PLOT, BG_SURFACE, BG_ELEVATED,
)
from data.tax_revenue import (
    BUDGET_YEARS, GROSS_TAX_REVENUE, CORPORATION_TAX, INCOME_TAX,
    GST_CENTRE_SHARE, CUSTOMS_DUTY, EXCISE_DUTY,
    TAX_DEVOLVED_TO_STATES, STATE_GST_CONTRIBUTION_2023_24,
    ITR_FILERS_CR,
)

st.markdown(
    page_header(
        "💰",
        "Tax Revenue Tracker",
        "Where does India's money come from? Explore the composition of Central tax revenue — Corporate Tax, Income Tax, GST, Customs, and more.",
    ),
    unsafe_allow_html=True,
)
st.markdown("---")

# ── Page controls (inline) ────────────────────────────────────────────────────
c_yr, _ = st.columns([1, 3])
with c_yr:
    year_filter = st.selectbox("Focus Year", BUDGET_YEARS[::-1], index=0)

# ── Top metrics ───────────────────────────────────────────────────────────────
gross   = GROSS_TAX_REVENUE[year_filter]
corp    = CORPORATION_TAX[year_filter]
income  = INCOME_TAX[year_filter]
gst     = GST_CENTRE_SHARE.get(year_filter) or 0
devolved = TAX_DEVOLVED_TO_STATES[year_filter]
net_centre = gross - devolved

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Gross Tax Revenue", f"₹{gross:.2f} L cr", year_filter)
with c2:
    st.metric("Net to Centre", f"₹{net_centre:.2f} L cr",
              f"After {devolved:.2f} L cr devolved to states")
with c3:
    st.metric("Corp Tax + Income Tax",
              f"₹{corp + income:.2f} L cr",
              f"{(corp + income)/gross*100:.1f}% of total")
with c4:
    gst_lbl = f"₹{gst:.2f} L cr" if gst else "Pre-GST era"
    st.metric("GST (Centre's share)", gst_lbl,
              "GST started 1 Jul 2017" if not gst else f"{gst/gross*100:.1f}% of total")

st.markdown("<br>", unsafe_allow_html=True)

# ── Section 1: Composition stacked bar ───────────────────────────────────────
st.markdown(
    f"<div class='section-label'>📊 &nbsp; Tax Collection by Source</div>",
    unsafe_allow_html=True,
)

fig_stack = go.Figure()
fig_stack.add_trace(go.Bar(
    name="Corporation Tax", x=BUDGET_YEARS,
    y=[CORPORATION_TAX[y] for y in BUDGET_YEARS],
    marker_color="#C0392B",
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra>Corp Tax</extra>",
))
fig_stack.add_trace(go.Bar(
    name="Income Tax (Personal)", x=BUDGET_YEARS,
    y=[INCOME_TAX[y] for y in BUDGET_YEARS],
    marker_color=ORANGE,
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra>Income Tax</extra>",
))
fig_stack.add_trace(go.Bar(
    name="GST (Centre share)", x=BUDGET_YEARS,
    y=[GST_CENTRE_SHARE.get(y) or 0 for y in BUDGET_YEARS],
    marker_color=TEAL,
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra>GST Centre</extra>",
))
fig_stack.add_trace(go.Bar(
    name="Customs Duty", x=BUDGET_YEARS,
    y=[CUSTOMS_DUTY[y] for y in BUDGET_YEARS],
    marker_color=BLUE_SOFT,
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra>Customs</extra>",
))
fig_stack.add_trace(go.Bar(
    name="Union Excise", x=BUDGET_YEARS,
    y=[EXCISE_DUTY[y] for y in BUDGET_YEARS],
    marker_color="#9A7000",
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra>Excise</extra>",
))
fig_stack.update_layout(
    barmode="stack",
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=380,
    margin=dict(l=8, r=8, t=12, b=8),
    legend=dict(bgcolor="rgba(245,237,216,0.9)", bordercolor=BORDER,
                borderwidth=1, font=dict(color=TEXT_SEC, size=11),
                orientation="h", y=-0.18),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="₹ Lakh Crore", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
)
st.plotly_chart(fig_stack, width='stretch')
st.markdown(
    insight_box(
        "India's tax mix has shifted dramatically. Before GST (2017), customs and excise dominated. "
        "Now <b>Personal Income Tax overtook Corporation Tax in 2022-23</b> for the first time — "
        "reflecting rising salaried employment and better TDS compliance. GST collections now "
        "form the single largest tax head."
    ),
    unsafe_allow_html=True,
)

# ── Section 2: Direct vs Indirect ────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-label'>⚖️ &nbsp; Direct Tax vs Indirect Tax</div>",
    unsafe_allow_html=True,
)

direct   = [CORPORATION_TAX[y] + INCOME_TAX[y] for y in BUDGET_YEARS]
indirect = [
    (GST_CENTRE_SHARE.get(y) or 0) + CUSTOMS_DUTY[y] + EXCISE_DUTY[y]
    for y in BUDGET_YEARS
]
direct_pct   = [d / (d + i) * 100 for d, i in zip(direct, indirect)]
indirect_pct = [100 - p for p in direct_pct]

fig_di = go.Figure()
fig_di.add_trace(go.Scatter(
    x=BUDGET_YEARS, y=direct_pct, name="Direct Tax %",
    fill="tozeroy", mode="lines+markers",
    line=dict(color=ORANGE, width=2.5),
    marker=dict(size=6, color=ORANGE),
    fillcolor=f"rgba(196,80,0,0.12)",
    hovertemplate="%{x}: %{y:.1f}% direct<extra></extra>",
))
fig_di.add_trace(go.Scatter(
    x=BUDGET_YEARS, y=indirect_pct, name="Indirect Tax %",
    mode="lines+markers",
    line=dict(color=TEAL, width=2.5, dash="dot"),
    marker=dict(size=6, color=TEAL),
    hovertemplate="%{x}: %{y:.1f}% indirect<extra></extra>",
))
fig_di.add_hline(y=50, line_dash="dash", line_color=BORDER,
                 annotation_text="50:50 line", annotation_font_color=TEXT_MUTED)
fig_di.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=300,
    margin=dict(l=8, r=8, t=12, b=8),
    legend=dict(bgcolor="rgba(245,237,216,0.9)", bordercolor=BORDER,
                borderwidth=1, font=dict(color=TEXT_SEC, size=11)),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="% share", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC),
               range=[30, 70]),
)
st.plotly_chart(fig_di, width='stretch')
_dt_latest = direct_pct[-1]
_dt_earliest = direct_pct[0]
st.markdown(
    insight_box(
        f"Direct taxes (paid by corporates and individuals directly) rose from <b>{_dt_earliest:.0f}%</b> (2015-16) "
        f"to <b>~{_dt_latest:.0f}%</b> (2024-25) of the tax mix. "
        "A higher direct-tax share is considered more equitable — "
        "indirect taxes like GST are regressive as they fall equally on rich and poor."
    ),
    unsafe_allow_html=True,
)

# ── Section 3: State GST contribution ────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-label'>🗺️ &nbsp; Which States Pay the Most GST? (FY 2023-24)</div>",
    unsafe_allow_html=True,
)

gst_states = sorted(STATE_GST_CONTRIBUTION_2023_24.items(), key=lambda x: x[1], reverse=True)
gst_df = pd.DataFrame(gst_states, columns=["State", "GST Collection (₹ Th cr)"])
total_gst = sum(v for v in STATE_GST_CONTRIBUTION_2023_24.values())
gst_df["Share %"] = (gst_df["GST Collection (₹ Th cr)"] / total_gst * 100).round(1)

fig_gst = go.Figure(go.Bar(
    x=gst_df["GST Collection (₹ Th cr)"],
    y=gst_df["State"],
    orientation="h",
    marker=dict(
        color=gst_df["GST Collection (₹ Th cr)"],
        colorscale=[[0, BG_ELEVATED], [0.4, ORANGE_LIGHT], [1, ORANGE]],
        showscale=False,
    ),
    text=[f"₹{v:.0f} ({s:.1f}%)" for v, s in
          zip(gst_df["GST Collection (₹ Th cr)"], gst_df["Share %"])],
    textposition="outside",
    textfont=dict(color=TEXT_SEC, size=10),
    hovertemplate="%{y}: ₹%{x:.1f} Th cr<extra></extra>",
))
fig_gst.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=520,
    margin=dict(l=8, r=160, t=12, b=8),
    xaxis=dict(title=dict(text="₹ Thousand Crore", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
)
st.plotly_chart(fig_gst, width='stretch')

col_a, col_b = st.columns(2)
with col_a:
    st.markdown(
        insight_box(
            f"<b>Maharashtra, Karnataka, Gujarat, and Tamil Nadu</b> together contribute "
            f"~{sum(STATE_GST_CONTRIBUTION_2023_24[s] for s in ['Maharashtra','Karnataka','Gujarat','Tamil Nadu'])/total_gst*100:.0f}% "
            f"of all state GST — though they have only ~25% of India's population. "
            f"Industrial and commercial states pay disproportionately more."
        ),
        unsafe_allow_html=True,
    )
with col_b:
    st.markdown(
        insight_box(
            f"<b>Bihar, UP, and MP</b> — which have large populations — collect far less GST "
            f"because their economies are more agricultural and informal. "
            f"This is why fiscal federalism and FC devolution exist: to redistribute back."
        ),
        unsafe_allow_html=True,
    )

# ── Section 4: ITR filers ─────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-label'>📋 &nbsp; Tax Compliance — How Many Indians File Returns?</div>",
    unsafe_allow_html=True,
)

_itr_vals = [ITR_FILERS_CR[y] for y in BUDGET_YEARS]
fig_itr = go.Figure(go.Bar(
    x=BUDGET_YEARS, y=_itr_vals,
    marker=dict(
        color=_itr_vals,
        colorscale=[[0, "#1A1A22"], [0.5, ORANGE_LIGHT], [1, ORANGE]],
        showscale=False,
    ),
    text=[f"{v:.1f} cr" for v in _itr_vals],
    textposition="outside",
    textfont=dict(color=TEXT_SEC, size=10),
    hovertemplate="%{x}: %{y:.1f} crore filers<extra></extra>",
))
fig_itr.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=300,
    margin=dict(l=8, r=16, t=12, b=8),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="Crore Filers", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
)
st.plotly_chart(fig_itr, width='stretch')
st.markdown(
    insight_box(
        "ITR filers have more than <b>doubled</b> from 3.7 crore (2015-16) to 8.9 crore (2024-25), "
        "driven by demonetisation nudge, GST data matching, and AIS (Annual Information Statement). "
        "Yet only ~6% of India's 140 crore people file taxes — most income falls below the ₹5 lakh threshold."
    ),
    unsafe_allow_html=True,
)

st.markdown(footer_html(), unsafe_allow_html=True)
