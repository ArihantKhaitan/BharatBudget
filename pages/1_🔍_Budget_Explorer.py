"""Budget Explorer — Ministry-wise breakdown for any year."""

import streamlit as st
import pandas as pd

from utils.styling import (
    GLOBAL_CSS, footer_html, insight_box,
    ORANGE, TEAL, TEXT_MUTED, NAVY_CARD, NAVY_LIGHT,
    BEIGE, BEIGE_MUTED, BG_PRIMARY, PLOTLY_PAPER, PLOTLY_PLOT, BORDER, GRID_COLOR,
)
from data.budget_data import (
    BUDGET_YEARS, TOTAL_BUDGET, MINISTRY_ALLOCATIONS, NOMINAL_GDP, MINISTRY_CATEGORIES, CATEGORY_COLORS
)
from components.charts import treemap_chart, bar_top10, donut_chart, fmt_lcr

st.set_page_config(
    page_title="Budget Explorer — BharatBudget",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── Sidebar controls ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        f"<h2 style='color:{ORANGE}; font-size:1.1rem;'>🔍 Budget Explorer</h2>",
        unsafe_allow_html=True,
    )
    selected_year = st.selectbox("Select Year", BUDGET_YEARS[::-1], index=0)
    view_type = st.radio("Show values", ["Allocated", "Actual Expenditure"], index=0)
    st.markdown("---")
    st.markdown(
        f"<p style='font-size:0.78rem;color:{TEXT_MUTED};'>"
        "Actual expenditure is the amount <em>actually spent</em> by end of financial year. "
        "It may differ from what was budgeted at the start."
        "</p>",
        unsafe_allow_html=True,
    )

value_key = "allocated" if view_type == "Allocated" else "actual"

year_data  = MINISTRY_ALLOCATIONS[selected_year]
total_val  = TOTAL_BUDGET[selected_year]
gdp_val    = NOMINAL_GDP[selected_year]

# Handle year where actual is None (current year)
if value_key == "actual":
    has_actual = any(d["actual"] is not None for d in year_data.values())
    if not has_actual:
        st.warning(
            f"Actual expenditure data for {selected_year} is not yet finalised. "
            "Showing allocated figures instead."
        )
        value_key = "allocated"

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    f"<h1 style='color:{ORANGE}; font-size:1.8rem; margin-bottom:0.2rem;'>"
    f"🔍 Budget Explorer</h1>"
    f"<p style='color:{TEXT_MUTED};'>Union Budget {selected_year} — "
    f"{'Allocated' if value_key=='allocated' else 'Actual Expenditure'}</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# ── Top metrics ───────────────────────────────────────────────────────────────
prev_year_idx = BUDGET_YEARS.index(selected_year)
prev_total    = TOTAL_BUDGET[BUDGET_YEARS[prev_year_idx - 1]] if prev_year_idx > 0 else None
yoy_pct       = (total_val - prev_total) / prev_total * 100 if prev_total else None
budget_gdp    = total_val / gdp_val * 100

biggest_m = max(
    {m: d for m, d in year_data.items() if d.get(value_key) is not None},
    key=lambda m: year_data[m].get(value_key, 0)
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    delta = f"{yoy_pct:+.1f}% vs {BUDGET_YEARS[prev_year_idx-1]}" if yoy_pct else ""
    st.metric(f"Total Budget {selected_year}", fmt_lcr(total_val), delta)
with c2:
    st.metric("As % of GDP", f"{budget_gdp:.1f}%", f"GDP = {fmt_lcr(gdp_val)}")
with c3:
    st.metric("Biggest Ministry", biggest_m,
              fmt_lcr(year_data[biggest_m].get(value_key, 0)))
with c4:
    per_capita = total_val * 1e5 / 140
    st.metric("Per Citizen (est.)", f"₹{per_capita:,.0f}", "per Indian")

st.markdown("<br>", unsafe_allow_html=True)

# ── Treemap ───────────────────────────────────────────────────────────────────
st.markdown(
    "<div class='section-header'>🗂️ Where does the money go?</div>",
    unsafe_allow_html=True,
)

fig_tree = treemap_chart(
    year_data, value_key=value_key,
    title=f"Ministry-wise Budget — {selected_year} ({view_type})"
)
st.plotly_chart(fig_tree, use_container_width=True)
st.markdown(
    insight_box(
        f"The treemap shows every ministry's share of the ₹{total_val:.2f} L cr budget. "
        f"Hover over any tile to see the exact amount. "
        f"<b>Interest Payments</b> and <b>Defence</b> consistently dominate — together "
        f"they account for about {(year_data['Interest Payments']['allocated'] + year_data['Defence']['allocated'])/total_val*100:.0f}% of the budget."
    ),
    unsafe_allow_html=True,
)

# ── Top 10 bar chart ──────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-header'>🏆 Top 10 Ministries by Spend</div>",
    unsafe_allow_html=True,
)

fig_bar = bar_top10(year_data, value_key=value_key,
                    title=f"Top 10 — {selected_year}", total=total_val)
st.plotly_chart(fig_bar, use_container_width=True)

# Build top-10 table
rows = sorted(
    [(m, d.get(value_key) or 0, (d.get(value_key) or 0) / total_val * 100)
     for m, d in year_data.items() if d.get(value_key) is not None],
    key=lambda x: x[1], reverse=True
)[:10]

df_top = pd.DataFrame(rows, columns=["Ministry", "Amount (₹ L cr)", "% of Budget"])
df_top["Amount (₹ L cr)"] = df_top["Amount (₹ L cr)"].apply(lambda x: f"₹{x:.2f}")
df_top["% of Budget"] = df_top["% of Budget"].apply(lambda x: f"{x:.1f}%")
df_top.index = range(1, 11)

st.dataframe(df_top, use_container_width=True)

# ── Category donut ────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-header'>🍩 Budget by Category</div>",
    unsafe_allow_html=True,
)

cat_totals, cat_labels = [], []
for cat, ministries in MINISTRY_CATEGORIES.items():
    cat_sum = sum(
        year_data.get(m, {}).get(value_key) or 0
        for m in ministries
    )
    cat_totals.append(cat_sum)
    cat_labels.append(cat)

col_donut, col_cat_text = st.columns([1, 1])
with col_donut:
    from plotly.graph_objects import Figure, Pie
    import plotly.graph_objects as go
    colors = [CATEGORY_COLORS.get(l, "#546E7A") for l in cat_labels]
    fig_donut = go.Figure(go.Pie(
        labels=cat_labels, values=cat_totals,
        hole=0.55,
        marker=dict(colors=colors, line=dict(width=1.5, color=BG_PRIMARY)),
        textinfo="percent+label",
        textfont=dict(color=BEIGE, size=11),
        hovertemplate="<b>%{label}</b><br>₹%{value:.2f} L cr (%{percent})<extra></extra>",
    ))
    fig_donut.update_layout(
        paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=BEIGE),
        height=360, margin=dict(l=0, r=0, t=10, b=0),
        showlegend=False,
    )
    st.plotly_chart(fig_donut, use_container_width=True)

with col_cat_text:
    st.markdown("<br><br>", unsafe_allow_html=True)
    for cat, val in zip(cat_labels, cat_totals):
        pct = val / total_val * 100
        color = CATEGORY_COLORS.get(cat, "#546E7A")
        st.markdown(
            f"""
            <div style='display:flex; align-items:center; margin-bottom:0.5rem;'>
              <div style='width:12px; height:12px; border-radius:3px;
                          background:{color}; margin-right:0.6rem; flex-shrink:0;'></div>
              <div>
                <span style='color:{BEIGE}; font-size:0.88rem;'>{cat}</span><br>
                <span style='color:{TEXT_MUTED}; font-size:0.78rem;'>
                  ₹{val:.2f} L cr &nbsp;·&nbsp; {pct:.1f}%
                </span>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Allocated vs Actual ───────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<div class='section-header'>⚖️ Allocated vs Actual Expenditure</div>",
    unsafe_allow_html=True,
)

alloc_vals, actual_vals, min_names = [], [], []
for m, d in sorted(year_data.items(), key=lambda x: x[1]["allocated"], reverse=True)[:12]:
    if d["actual"] is not None:
        alloc_vals.append(d["allocated"])
        actual_vals.append(d["actual"])
        min_names.append(m[:22])

if alloc_vals:
    import plotly.graph_objects as go
    fig_cmp = go.Figure()
    fig_cmp.add_trace(go.Bar(
        name="Allocated", x=min_names, y=alloc_vals,
        marker_color=ORANGE, opacity=0.85,
    ))
    fig_cmp.add_trace(go.Bar(
        name="Actual Spent", x=min_names, y=actual_vals,
        marker_color=TEAL, opacity=0.85,
    ))
    fig_cmp.update_layout(
        barmode="group",
        paper_bgcolor=PLOTLY_PAPER, plot_bgcolor=PLOTLY_PLOT,
        font=dict(color=BEIGE),
        height=360,
        margin=dict(l=16, r=16, t=24, b=80),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=TEXT_MUTED)),
        xaxis=dict(gridcolor=NAVY_LIGHT, tickangle=-30, tickfont=dict(size=10, color=TEXT_MUTED)),
        yaxis=dict(title="₹ Lakh Crore", gridcolor=NAVY_LIGHT, tickfont=dict(color=TEXT_MUTED)),
    )
    st.plotly_chart(fig_cmp, use_container_width=True)
    st.markdown(
        insight_box(
            "Bars where <b>actual spend < allocated</b> mean the ministry didn't fully use its budget — "
            "often due to project delays or slow procurement. <b>Food subsidies</b> regularly "
            "<em>exceed</em> their allocation due to supplementary demands mid-year."
        ),
        unsafe_allow_html=True,
    )
else:
    st.info(f"Actual expenditure data for {selected_year} will be available after the fiscal year ends.")

st.markdown(footer_html(), unsafe_allow_html=True)
