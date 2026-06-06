"""State Finance Tracker — How much does each state get from the Centre?"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from utils.styling import (
    GLOBAL_CSS, footer_html, insight_box,
    ORANGE, TEAL, RED, TEXT_MUTED, NAVY_LIGHT, NAVY_CARD, TEXT_MAIN, BLUE_SOFT,
    BEIGE, BEIGE_MUTED, BG_PRIMARY, PLOTLY_PAPER, PLOTLY_PLOT, BORDER, GRID_COLOR,
)
from data.states import (
    STATE_METADATA, PER_CAPITA_TRANSFER_2023_24,
    TOTAL_TRANSFERS_BY_YEAR, STATE_GSDP_GROWTH, FC_DEVOLUTION_SHARE,
)

st.set_page_config(
    page_title="State Finance Tracker — BharatBudget",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        f"<h2 style='color:{ORANGE}; font-size:1.1rem;'>🗺️ State Finance Tracker</h2>",
        unsafe_allow_html=True,
    )
    sort_by = st.selectbox(
        "Sort states by",
        ["Per-capita transfer", "Total transfer", "GSDP Growth", "FC Devolution Share"],
        index=0,
    )
    show_special_cat = st.checkbox("Highlight Special Category States", value=True)
    st.markdown("---")
    st.markdown(
        f"<p style='font-size:0.78rem;color:{TEXT_MUTED};'>"
        "Central transfers include: Tax Devolution, Grants-in-Aid, Centrally Sponsored Schemes (CSS), "
        "and Central Sector Schemes. Data based on Finance Commission XV award + CGA actuals."
        "</p>",
        unsafe_allow_html=True,
    )

# Special category states (hilly/northeast)
SPECIAL_CATEGORY = {
    "Uttarakhand", "Himachal Pradesh", "Jammu & Kashmir",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland",
    "Tripura", "Sikkim", "Arunachal Pradesh", "Assam",
}

# ── Build main dataframe ──────────────────────────────────────────────────────
rows = []
for state, meta in STATE_METADATA.items():
    pc  = PER_CAPITA_TRANSFER_2023_24.get(state, 0)
    pop = meta["population_cr"]
    total_transfer = pc * pop / 1e5  # Lakh Crore
    rows.append({
        "state":          state,
        "population_cr":  pop,
        "lat":            meta["lat"],
        "lon":            meta["lon"],
        "per_capita":     pc,
        "total_transfer": round(total_transfer, 4),
        "gsdp_growth":    STATE_GSDP_GROWTH.get(state, 0),
        "fc_share":       FC_DEVOLUTION_SHARE.get(state, 0),
        "special":        state in SPECIAL_CATEGORY,
    })

df = pd.DataFrame(rows)

# Sort
sort_col_map = {
    "Per-capita transfer": "per_capita",
    "Total transfer":      "total_transfer",
    "GSDP Growth":         "gsdp_growth",
    "FC Devolution Share": "fc_share",
}
df = df.sort_values(sort_col_map[sort_by], ascending=False).reset_index(drop=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    f"<h1 style='color:{ORANGE}; font-size:1.8rem; margin-bottom:0.2rem;'>"
    f"🗺️ State Finance Tracker</h1>"
    f"<p style='color:{TEXT_MUTED};'>How much does the Centre transfer to each state — and is it fair?</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# ── Key stats ─────────────────────────────────────────────────────────────────
total_2324 = TOTAL_TRANSFERS_BY_YEAR["2023-24"]
highest_pc_state = df.loc[df["per_capita"].idxmax(), "state"]
highest_pc_val   = df["per_capita"].max()
lowest_pc_state  = df.loc[df["per_capita"].idxmin(), "state"]
lowest_pc_val    = df["per_capita"].min()

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Total Central Transfers 2023-24", f"₹{total_2324:.2f} L cr",
              "+12.7% vs 2022-23")
with c2:
    st.metric("Highest Per-Capita State", highest_pc_state,
              f"₹{highest_pc_val:,}/person")
with c3:
    st.metric("Lowest Per-Capita State", lowest_pc_state,
              f"₹{lowest_pc_val:,}/person")
with c4:
    ratio = highest_pc_val / lowest_pc_val
    st.metric("Disparity Ratio", f"{ratio:.1f}×",
              "between highest & lowest")

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# MAP: India bubble map
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown(
    "<div class='section-header'>🗺️ India Map — Per-Capita Central Transfer</div>",
    unsafe_allow_html=True,
)

max_pc   = df["per_capita"].max()
fig_map  = go.Figure()

for _, row in df.iterrows():
    color = ORANGE if row["special"] and show_special_cat else TEAL
    fig_map.add_trace(go.Scattergeo(
        lon=[row["lon"]],
        lat=[row["lat"]],
        text=[row["state"]],
        customdata=[[row["per_capita"], row["total_transfer"], "Yes" if row["special"] else "No"]],
        mode="markers+text",
        textposition="top center",
        textfont=dict(size=8, color=TEXT_MAIN),
        marker=dict(
            size=row["per_capita"] / max_pc * 50 + 6,
            color=row["per_capita"],
            colorscale=[
                [0.0, "#1A1A22"],
                [0.3, "#7EB8FF"],
                [0.6, ORANGE],
                [1.0, "#FF4D4D"],
            ],
            cmin=df["per_capita"].min(),
            cmax=max_pc,
            showscale=True if _ == 0 else False,
            colorbar=dict(
                title=dict(text="₹ per capita", font=dict(color=TEXT_MUTED, size=10)),
                tickfont=dict(color=TEXT_MUTED, size=9),
                bgcolor=PLOTLY_PAPER,
                len=0.5, y=0.5,
            ) if _ == 0 else {},
            opacity=0.85,
            line=dict(width=1, color="#ffffff"),
        ),
        hovertemplate=(
            "<b>%{text}</b><br>"
            "Per capita: ₹%{customdata[0]:,}<br>"
            "Total transfer: ₹%{customdata[1]:.3f} L cr<br>"
            "Special category: %{customdata[2]}<extra></extra>"
        ),
        showlegend=False,
    ))

fig_map.update_geos(
    scope="asia",
    center=dict(lat=22.5, lon=82.5),
    projection_scale=4.8,
    showcoastlines=True,  coastlinecolor=NAVY_LIGHT,
    showland=True,        landcolor=PLOTLY_PLOT,
    showocean=True,       oceancolor=PLOTLY_PAPER,
    showlakes=True,       lakecolor=PLOTLY_PAPER,
    showcountries=True,   countrycolor=NAVY_LIGHT,
    bgcolor=PLOTLY_PAPER,
)
fig_map.update_layout(
    paper_bgcolor=PLOTLY_PAPER,
    height=560,
    margin=dict(l=0, r=0, t=0, b=0),
    geo=dict(bgcolor=PLOTLY_PAPER),
)
st.plotly_chart(fig_map, use_container_width=True)
st.markdown(
    insight_box(
        "Bubble size and colour both represent per-capita central transfers. "
        f"<b>Smaller/poorer states</b> (especially northeastern states and J&K) receive "
        f"significantly more <em>per person</em> than large states like Delhi or Maharashtra. "
        f"This <b>equalisation</b> is deliberate — the Finance Commission's formula "
        f"weights states based on income distance, area, forest cover, and tax effort."
    ),
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════════════════════
# BAR: Per-capita ranking
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-header'>📊 Per-Capita Central Transfer — State Ranking (2023-24)</div>",
    unsafe_allow_html=True,
)

df_sorted_pc = df.sort_values("per_capita", ascending=True)
bar_colors   = [ORANGE if row["special"] else TEAL for _, row in df_sorted_pc.iterrows()]

fig_bar = go.Figure(go.Bar(
    x=df_sorted_pc["per_capita"],
    y=df_sorted_pc["state"],
    orientation="h",
    marker=dict(color=bar_colors),
    text=[f"₹{v:,}" for v in df_sorted_pc["per_capita"]],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=9),
    hovertemplate="<b>%{y}</b><br>₹%{x:,} per capita<extra></extra>",
))
fig_bar.update_layout(
    paper_bgcolor=PLOTLY_PAPER,
    plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_MAIN),
    height=760,
    margin=dict(l=10, r=120, t=10, b=10),
    xaxis=dict(title="₹ per capita", gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
    yaxis=dict(tickfont=dict(size=10, color=TEXT_MUTED)),
)
# Legend annotation
fig_bar.add_annotation(
    x=0.98, y=0.02, xref="paper", yref="paper",
    text=(
        f"<span style='color:{ORANGE};'>■</span> Special Category State&nbsp;&nbsp;"
        f"<span style='color:{TEAL};'>■</span> General State"
    ),
    showarrow=False, font=dict(size=10, color=TEXT_MUTED),
    align="right", bgcolor="#0B1437",
)
st.plotly_chart(fig_bar, use_container_width=True)
st.markdown(
    insight_box(
        f"<b>Special Category States</b> (shown in orange) receive disproportionately high "
        f"per-capita transfers. Sikkim tops the list at ₹31,230/person — about <b>7.4×</b> "
        f"Delhi's ₹4,230/person. This reflects India's <b>fiscal federalism</b> goal: "
        f"ensuring even the smallest, most remote state can fund basic services."
    ),
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════════════════════
# BAR: Total transfer (absolute)
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-header'>💰 Total Central Transfer by State (absolute, 2023-24 est.)</div>",
    unsafe_allow_html=True,
)

df_sorted_tt = df.sort_values("total_transfer", ascending=True)
fig_abs = go.Figure(go.Bar(
    x=df_sorted_tt["total_transfer"],
    y=df_sorted_tt["state"],
    orientation="h",
    marker=dict(
        color=df_sorted_tt["total_transfer"],
        colorscale=[[0, "#1A1A22"], [1, ORANGE]],
        showscale=False,
    ),
    text=[f"₹{v:.3f} L cr" for v in df_sorted_tt["total_transfer"]],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=9),
    hovertemplate="<b>%{y}</b><br>₹%{x:.4f} L cr<extra></extra>",
))
fig_abs.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_MAIN), height=760,
    margin=dict(l=10, r=120, t=10, b=10),
    xaxis=dict(title="₹ Lakh Crore", gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
    yaxis=dict(tickfont=dict(size=10, color=TEXT_MUTED)),
)
st.plotly_chart(fig_abs, use_container_width=True)
st.markdown(
    insight_box(
        "<b>Uttar Pradesh</b> gets the largest absolute transfer (~₹1.97 L cr) due to its "
        "massive population (23.4 crore). But in <em>per-capita</em> terms it ranks near the "
        "bottom — ₹8,450/person vs Sikkim's ₹31,230. "
        "Large populous states are the biggest beneficiaries in absolute terms, "
        "small states in per-capita terms."
    ),
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════════════════════
# Finance Commission devolution share
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-header'>📐 Finance Commission XV — Tax Devolution Share</div>",
    unsafe_allow_html=True,
)

df_fc = df[df["fc_share"] > 0].sort_values("fc_share", ascending=True)
fig_fc = go.Figure(go.Bar(
    x=df_fc["fc_share"], y=df_fc["state"], orientation="h",
    marker=dict(
                color=df_fc["fc_share"].tolist(),
                colorscale=[[0, "#1A1A22"], [1, "#7EB8FF"]],
                showscale=False),
    text=[f"{v:.3f}%" for v in df_fc["fc_share"]],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=9),
    hovertemplate="<b>%{y}</b><br>FC share: %{x:.3f}%<extra></extra>",
))

fig_fc.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_MAIN), height=680,
    margin=dict(l=10, r=80, t=10, b=10),
    xaxis=dict(title="% of divisible pool", gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
    yaxis=dict(tickfont=dict(size=10, color=TEXT_MUTED)),
)
st.plotly_chart(fig_fc, use_container_width=True)
st.markdown(
    insight_box(
        "The Finance Commission XV (2021-26) distributes <b>41% of central taxes</b> to states. "
        "UP alone gets <b>17.93%</b> of this — the highest share. The formula weighs "
        "<b>income distance</b> (poorer = more), population, area, forest cover, and tax effort. "
        "Richer states like Delhi and Goa get near zero as they're largely self-sufficient."
    ),
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════════════════════
# Scatter: Transfer vs GSDP Growth
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-header'>📈 Does more central money = faster state growth?</div>",
    unsafe_allow_html=True,
)

fig_sc2 = go.Figure()
for _, row in df.iterrows():
    color = ORANGE if (show_special_cat and row["special"]) else TEAL
    fig_sc2.add_trace(go.Scatter(
        x=[row["per_capita"]],
        y=[row["gsdp_growth"]],
        mode="markers+text",
        text=[row["state"][:10]],
        textposition="top center",
        textfont=dict(size=8, color=TEXT_MUTED),
        marker=dict(size=10, color=color, opacity=0.85,
                    line=dict(width=1, color=TEXT_MAIN)),
        hovertemplate=(
            f"<b>{row['state']}</b><br>"
            f"Per-capita transfer: ₹{row['per_capita']:,}<br>"
            f"GSDP Growth: {row['gsdp_growth']}%<extra></extra>"
        ),
        showlegend=False,
    ))

# Trendline
x_arr = df["per_capita"].values.astype(float)
y_arr = df["gsdp_growth"].values.astype(float)
m, b  = np.polyfit(x_arr, y_arr, 1)
xs    = np.linspace(x_arr.min(), x_arr.max(), 100)
fig_sc2.add_trace(go.Scatter(
    x=xs, y=m*xs+b, mode="lines", name="Trend",
    line=dict(color="#9E9E9E", dash="dot", width=1.5), hoverinfo="skip",
))
fig_sc2.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_MAIN), height=400,
    margin=dict(l=16, r=16, t=10, b=16),
    xaxis=dict(title="Per-capita central transfer (₹)", gridcolor=NAVY_LIGHT,
               tickfont=dict(color=TEXT_MUTED)),
    yaxis=dict(title="GSDP Growth 2023-24 (%)", gridcolor=NAVY_LIGHT,
               tickfont=dict(color=TEXT_MUTED)),
    showlegend=False,
)
st.plotly_chart(fig_sc2, use_container_width=True)
st.markdown(
    insight_box(
        "There's a <b>weak/flat correlation</b> between per-capita transfers and GSDP growth — "
        "suggesting transfers alone don't drive growth. Fast-growing states like "
        "<b>Telangana, Arunachal Pradesh, and Karnataka</b> vary widely in transfer levels. "
        "Good governance, ease of doing business, and natural resources matter more. "
        "Transfers are about <em>equity</em>, not <em>efficiency</em>."
    ),
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════════════════════
# Table
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown(
    "<div class='section-header'>📋 Full State Data Table (2023-24)</div>",
    unsafe_allow_html=True,
)

df_table = df[["state", "population_cr", "per_capita", "total_transfer", "gsdp_growth", "fc_share", "special"]].copy()
df_table.columns = ["State", "Population (Cr)", "Per-Capita Transfer (₹)", "Total Transfer (₹ L cr)",
                     "GSDP Growth (%)", "FC XV Share (%)", "Special Category"]
df_table["Special Category"] = df_table["Special Category"].map({True: "Yes", False: "No"})
df_table["Per-Capita Transfer (₹)"] = df_table["Per-Capita Transfer (₹)"].apply(lambda x: f"₹{x:,}")
df_table["Total Transfer (₹ L cr)"] = df_table["Total Transfer (₹ L cr)"].apply(lambda x: f"₹{x:.4f}")
df_table["FC XV Share (%)"] = df_table["FC XV Share (%)"].apply(lambda x: f"{x:.3f}%")
df_table = df_table.sort_values("Per-Capita Transfer (₹)", ascending=False)
st.dataframe(df_table, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════════
# Central transfer trend
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-header'>📈 Total Central Transfers to States (2018–2025)</div>",
    unsafe_allow_html=True,
)

transfer_years = list(TOTAL_TRANSFERS_BY_YEAR.keys())
transfer_vals  = list(TOTAL_TRANSFERS_BY_YEAR.values())

fig_tt = go.Figure(go.Bar(
    x=transfer_years, y=transfer_vals,
    marker=dict(color=transfer_vals, colorscale=[[0,"#1A1A22"],[1,ORANGE]], showscale=False),
    text=[f"₹{v:.2f}" for v in transfer_vals],
    textposition="outside",
    textfont=dict(color=TEXT_MUTED, size=11),
    hovertemplate="%{x}: ₹%{y:.2f} L cr<extra></extra>",
))
fig_tt.update_layout(
    paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
    font=dict(color=TEXT_MAIN), height=300,
    margin=dict(l=16, r=16, t=10, b=16),
    xaxis=dict(gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
    yaxis=dict(title="₹ Lakh Crore", gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
)
st.plotly_chart(fig_tt, use_container_width=True)
st.markdown(
    insight_box(
        f"Total central transfers to states have grown from <b>₹14.07 L cr (2018-19)</b> to "
        f"<b>₹27.34 L cr (2024-25)</b> — nearly doubling. The Finance Commission XV "
        f"award increased the states' share of the divisible pool from 32% (FC XIV) to "
        f"<b>41%</b>, giving states significantly more fiscal autonomy."
    ),
    unsafe_allow_html=True,
)

st.markdown(footer_html(), unsafe_allow_html=True)
