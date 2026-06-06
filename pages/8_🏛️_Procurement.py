"""Government Procurement — How much does India buy, and from whom?"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from utils.styling import (
    footer_html, insight_box, page_header,
    ORANGE, ORANGE_LIGHT, TEAL, RED, BLUE_SOFT, TEXT_PRIMARY, TEXT_SEC, TEXT_MUTED,
    BORDER, GRID_COLOR, PLOTLY_PAPER, PLOTLY_PLOT, BG_ELEVATED,
)
from data.procurement import (
    BUDGET_YEARS, GEM_ORDERS_TCR, GEM_SELLERS_LAKH, GEM_BUYERS_K,
    GEM_CATEGORIES_2023_24, STATE_GEM_PROCUREMENT_2023_24,
    MAJOR_CONTRACTS_BY_SECTOR, GEM_MSME_PCT, GEM_WOMEN_ENTERPRISES_PCT,
)

st.markdown(
    page_header(
        "🏛️",
        "Government Procurement",
        "How does budget money reach businesses and people? Track India's ₹17L cr Government e-Marketplace, state-wise contracts, and major infrastructure tenders.",
    ),
    unsafe_allow_html=True,
)
st.markdown("---")

# ── Top metrics ───────────────────────────────────────────────────────────────
latest_gem = GEM_ORDERS_TCR["2024-25"]
prev_gem   = GEM_ORDERS_TCR["2023-24"]
gem_growth = (latest_gem - prev_gem) / prev_gem * 100

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("GeM Orders 2024-25", f"₹{latest_gem:.1f}k cr",
              f"+{gem_growth:.0f}% vs 2023-24")
with c2:
    st.metric("Registered Sellers", f"{GEM_SELLERS_LAKH['2024-25']:.1f} lakh",
              "MSMEs, startups & manufacturers")
with c3:
    st.metric("MSME Share of GeM", f"{GEM_MSME_PCT['2024-25']}%",
              "Orders going to small businesses")
with c4:
    st.metric("Women Enterprise Share", f"{GEM_WOMEN_ENTERPRISES_PCT['2024-25']}%",
              "Women-owned businesses on GeM")

st.markdown("<br>", unsafe_allow_html=True)

# ── Section 1: GeM growth ─────────────────────────────────────────────────────
st.markdown(
    f"<div class='section-label'>📈 &nbsp; GeM Marketplace Growth</div>",
    unsafe_allow_html=True,
)

yrs = list(GEM_ORDERS_TCR.keys())
fig_gem = go.Figure()
fig_gem.add_trace(go.Bar(
    x=yrs, y=list(GEM_ORDERS_TCR.values()),
    name="Order Value (₹ Th cr)",
    marker=dict(
        color=list(GEM_ORDERS_TCR.values()),
        colorscale=[[0, BG_ELEVATED], [0.4, ORANGE_LIGHT], [1, ORANGE]],
        showscale=False,
    ),
    text=[f"₹{v:.1f}k" for v in GEM_ORDERS_TCR.values()],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=9),
    hovertemplate="%{x}: ₹%{y:.2f}k cr<extra></extra>",
))
fig_gem.add_trace(go.Scatter(
    x=yrs, y=list(GEM_SELLERS_LAKH.values()),
    name="Sellers (lakh)", yaxis="y2",
    mode="lines+markers",
    line=dict(color=TEAL, width=2.5, dash="dot"),
    marker=dict(size=7, color=TEAL),
    hovertemplate="%{x}: %{y:.1f} lakh sellers<extra></extra>",
))
fig_gem.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=340,
    margin=dict(l=8, r=60, t=12, b=8),
    legend=dict(bgcolor="rgba(245,237,216,0.9)", bordercolor=BORDER,
                borderwidth=1, font=dict(color=TEXT_SEC, size=11),
                orientation="h", y=1.12),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="₹ Thousand Crore", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    yaxis2=dict(title=dict(text="Sellers (lakh)", font=dict(color=TEAL)),
                overlaying="y", side="right",
                tickfont=dict(color=TEAL), gridcolor="rgba(0,0,0,0)"),
)
st.plotly_chart(fig_gem, use_container_width=True)
st.markdown(insight_box(
    "GeM has grown from virtually zero to <b>₹17.4 lakh crore</b> in orders by 2024-25 — a <b>870x growth in 8 years</b>. "
    "It has eliminated middlemen in government procurement, giving direct access to <b>11.8 lakh sellers</b> "
    "including MSMEs, startups, and artisans (SHGs). "
    "Savings estimated at 10-15% vs traditional tendering."
), unsafe_allow_html=True)

# ── Section 2: What government buys ──────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
left, right = st.columns(2)

with left:
    st.markdown(
        f"<div class='section-label'>🛒 &nbsp; Top Procurement Categories (FY 2023-24)</div>",
        unsafe_allow_html=True,
    )
    cats = sorted(GEM_CATEGORIES_2023_24.items(), key=lambda x: x[1], reverse=True)
    df_cats = pd.DataFrame(cats, columns=["Category", "Value (₹ Th cr)"])
    fig_cat = go.Figure(go.Bar(
        x=df_cats["Value (₹ Th cr)"], y=df_cats["Category"],
        orientation="h",
        marker=dict(
            color=df_cats["Value (₹ Th cr)"],
            colorscale=[[0, BG_ELEVATED], [0.5, ORANGE_LIGHT], [1, ORANGE]],
        ),
        text=[f"₹{v:.2f}k cr" for v in df_cats["Value (₹ Th cr)"]],
        textposition="outside",
        textfont=dict(color=TEXT_MUTED, size=9),
        hovertemplate="%{y}: ₹%{x:.2f}k cr<extra></extra>",
    ))
    fig_cat.update_layout(
        paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
        height=420,
        margin=dict(l=8, r=80, t=8, b=8),
        xaxis=dict(gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
        yaxis=dict(gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    )
    st.plotly_chart(fig_cat, use_container_width=True)

with right:
    st.markdown(
        f"<div class='section-label'>🏗️ &nbsp; Major Infrastructure Contracts by Sector</div>",
        unsafe_allow_html=True,
    )
    infra = sorted(MAJOR_CONTRACTS_BY_SECTOR.items(), key=lambda x: x[1], reverse=True)
    df_infra = pd.DataFrame(infra, columns=["Sector", "Contracts (₹ Th cr)"])
    colors_infra = [TEAL if i % 2 == 0 else ORANGE_LIGHT for i in range(len(df_infra))]
    fig_infra = go.Figure(go.Bar(
        x=df_infra["Contracts (₹ Th cr)"], y=df_infra["Sector"],
        orientation="h",
        marker_color=colors_infra,
        text=[f"₹{v:.2f}k cr" for v in df_infra["Contracts (₹ Th cr)"]],
        textposition="outside",
        textfont=dict(color=TEXT_MUTED, size=9),
        hovertemplate="%{y}: ₹%{x:.2f}k cr<extra></extra>",
    ))
    fig_infra.update_layout(
        paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
        height=420,
        margin=dict(l=8, r=80, t=8, b=8),
        xaxis=dict(title=dict(text="₹ Thousand Crore", font=dict(color=TEXT_SEC)),
                   gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
        yaxis=dict(gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    )
    st.plotly_chart(fig_infra, use_container_width=True)

# ── Section 3: State-wise GeM procurement ────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-label'>🗺️ &nbsp; State-wise GeM Procurement (FY 2023-24)</div>",
    unsafe_allow_html=True,
)

sorted_states = sorted(STATE_GEM_PROCUREMENT_2023_24.items(), key=lambda x: x[1], reverse=True)
df_states = pd.DataFrame(sorted_states, columns=["State", "GeM Orders (₹ Th cr)"])

fig_states = go.Figure(go.Bar(
    x=df_states["GeM Orders (₹ Th cr)"],
    y=df_states["State"],
    orientation="h",
    marker=dict(
        color=df_states["GeM Orders (₹ Th cr)"],
        colorscale=[[0, BG_ELEVATED], [0.4, ORANGE_LIGHT], [1, ORANGE]],
    ),
    text=[f"₹{v:.2f}k cr" for v in df_states["GeM Orders (₹ Th cr)"]],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=9),
    hovertemplate="%{y}: ₹%{x:.2f}k cr<extra></extra>",
))
fig_states.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=560,
    margin=dict(l=8, r=80, t=8, b=8),
    xaxis=dict(title=dict(text="₹ Thousand Crore", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
)
st.plotly_chart(fig_states, use_container_width=True)
st.markdown(insight_box(
    "<b>UP leads in state-level GeM procurement</b> partly due to its scale and active adoption by state govt bodies. "
    "Southern states like Karnataka and Tamil Nadu rank high due to IT and manufacturing procurement. "
    "Smaller northeast states have low absolute numbers but are growing rapidly in % terms."
), unsafe_allow_html=True)

# ── Section 4: MSME & Women inclusion ─────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"<div class='section-label'>🤝 &nbsp; Inclusive Procurement — MSMEs & Women Enterprises</div>",
    unsafe_allow_html=True,
)
yrs_msme = list(GEM_MSME_PCT.keys())
fig_inc = go.Figure()
fig_inc.add_trace(go.Scatter(
    x=yrs_msme, y=list(GEM_MSME_PCT.values()),
    name="MSME Share %", mode="lines+markers+text",
    line=dict(color=ORANGE, width=2.5),
    marker=dict(size=8, color=ORANGE),
    text=[f"{v}%" for v in GEM_MSME_PCT.values()],
    textposition="top center", textfont=dict(color=TEXT_MUTED, size=9),
    hovertemplate="%{x}: %{y}% MSME<extra></extra>",
))
fig_inc.add_trace(go.Scatter(
    x=yrs_msme, y=list(GEM_WOMEN_ENTERPRISES_PCT.values()),
    name="Women Enterprise Share %", mode="lines+markers+text",
    line=dict(color=TEAL, width=2.5, dash="dot"),
    marker=dict(size=8, color=TEAL),
    text=[f"{v}%" for v in GEM_WOMEN_ENTERPRISES_PCT.values()],
    textposition="top center", textfont=dict(color=TEXT_MUTED, size=9),
    hovertemplate="%{x}: %{y}% women-owned<extra></extra>",
))
fig_inc.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_PRIMARY, family="DM Sans, sans-serif"),
    height=280,
    margin=dict(l=8, r=8, t=12, b=8),
    legend=dict(bgcolor="rgba(245,237,216,0.9)", bordercolor=BORDER,
                borderwidth=1, font=dict(color=TEXT_SEC, size=11)),
    xaxis=dict(gridcolor=GRID_COLOR, linecolor=BORDER, tickfont=dict(color=TEXT_SEC)),
    yaxis=dict(title=dict(text="% of GeM Orders", font=dict(color=TEXT_SEC)),
               gridcolor=GRID_COLOR, tickfont=dict(color=TEXT_SEC)),
)
st.plotly_chart(fig_inc, use_container_width=True)

st.markdown(footer_html(), unsafe_allow_html=True)
