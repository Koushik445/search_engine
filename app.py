"""
Streamlit Web Application: Conversational Food Delivery Search Engine
Run: streamlit run app.py
"""

import streamlit as st
import os
import sys

from search_engine import AdvancedFoodSearchEngine

st.set_page_config(
    page_title="Zomato-style Conversational Food Search",
    page_icon="🍔",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #E23744;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #666;
        margin-bottom: 1.5rem;
    }
    .dish-card {
        background-color: #FFFFFF;
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #ECECEC;
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .dish-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1C1C1C;
    }
    .restaurant-title {
        font-size: 0.95rem;
        color: #7E7E7E;
        font-weight: 500;
    }
    .price-tag {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1C1C1C;
    }
    .veg-badge {
        color: #0F8A65;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid #0F8A65;
        padding: 2px 6px;
        border-radius: 4px;
    }
    .non-veg-badge {
        color: #E23744;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid #E23744;
        padding: 2px 6px;
        border-radius: 4px;
    }
    .intent-pill {
        background-color: #FFF2F2;
        color: #E23744;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_engine():
    return AdvancedFoodSearchEngine(r"d:\Search_Engine")

try:
    engine = get_engine()
except Exception as e:
    st.error(f"Error loading search engine: {e}")
    st.stop()

st.markdown('<div class="main-header">🍔 Conversational Food Search Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Natural Language & Voice Search powered by Hybrid Retrieval (BM25 + 384-d Dense Vectors)</div>', unsafe_allow_html=True)

# Sidebar: User Location & Settings
st.sidebar.header("📍 User Context & Location")
location_presets = {
    "Koramangala 5th Block (Current)": (12.9352, 77.6245),
    "Indiranagar 100 Feet Rd": (12.9716, 77.6412),
    "HSR Layout Sector 3": (12.9116, 77.6389),
    "Jayanagar 4th Block": (12.9290, 77.5830),
    "Whitefield ITPL": (12.9780, 77.7200),
    "Church Street / MG Road": (12.9750, 77.6050)
}
selected_loc_name = st.sidebar.selectbox("Simulate User Location", list(location_presets.keys()))
user_lat, user_lon = location_presets[selected_loc_name]

top_k = st.sidebar.slider("Results to display (Top-K)", min_value=3, max_value=20, value=6)

# Example query chips
st.markdown("**Try Example Conversational Queries:**")
cols = st.columns(6)
example_queries = [
    "Chai and samosa",
    "Burger with cold drink",
    "Truffles ka burger",
    "pizza under 250",
    "burger 150rs wala",
    "sabse sasta pizza"
]

default_query = "Chai and samosa"
for idx, q_text in enumerate(example_queries):
    if cols[idx].button(q_text, key=f"chip_{idx}"):
        st.session_state["search_input"] = q_text

if "search_input" not in st.session_state:
    st.session_state["search_input"] = default_query

query = st.text_input(
    "Ask anything in everyday English or Hinglish (e.g. 'XYZ ka burger', 'under 200', 'dish and dish'):",
    value=st.session_state["search_input"],
    placeholder="Type e.g. 'Garlic Bread with cheese dip' or 'pizza outlets near me'"
)

if query:
    with st.spinner("Decoding natural language intent and querying index..."):
        res = engine.search(query, user_lat=user_lat, user_lon=user_lon, top_k=top_k)

    # Display Intent Banner
    col_intent, col_stats = st.columns([3, 1])
    with col_intent:
        st.markdown(f'<span class="intent-pill">INTENT: {res["intent"]}</span> &nbsp; <b>{res["explanation"]}</b>', unsafe_allow_html=True)
    with col_stats:
        st.caption(f"Found {res['total_matches']} relevant matches")

    st.write("")

    # Display Results
    if res["intent"] == "MULTI_DISH_COMBO":
        st.subheader("🍱 Single-Order Combo Bundles (Both Dishes from Same Outlet)")
        if not res["results"]:
            st.warning("No single restaurant nearby was found serving both dishes together.")
        else:
            for b in res["results"]:
                with st.container():
                    st.markdown(f"""
                    <div class="dish-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span class="dish-title">🍱 Combo Meal: {b['dish_pair'][0]['name']} + {b['dish_pair'][1]['name']}</span><br>
                                <span class="restaurant-title">from <b>{b['restaurant_name']}</b> ({b['locality']}) • 📍 {b['distance_km']} km away • ⏱ {b['delivery_time_mins']} mins • ⭐ {b['restaurant_rating']}</span>
                            </div>
                            <div style="text-align: right;">
                                <span class="price-tag">Rs. {b['total_bundle_price']}</span><br>
                                <small style="color: #0F8A65; font-weight: 600;">{b['savings_or_offer']}</small>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    elif res["intent"] in ("RESTAURANT_SEARCH", "OUTLET_SEARCH"):
        st.subheader("🏪 Matching Restaurant Outlets")
        for r in res["results"]:
            badge = '<span class="veg-badge">PURE VEG</span>' if r.get('is_pure_veg') else '<span class="non-veg-badge">NON-VEG</span>'
            with st.container():
                st.markdown(f"""
                <div class="dish-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            {badge} &nbsp; <span class="dish-title">{r['restaurant_name']}</span><br>
                            <span class="restaurant-title">📍 {r['locality']} • {r['distance_km']} km away • ⭐ {r['rating']} ({r['rating_count']:,} votes)</span><br>
                            <small>Cuisines: {', '.join(r.get('cuisines', []))}</small>
                        </div>
                        <div style="text-align: right;">
                            <span style="color: #E23744; font-weight: 700;">⏱ {r['delivery_time_mins']} mins</span><br>
                            <small style="color: #0F8A65; font-weight: 600;">{r.get('discount_offer', '')}</small>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.subheader("🍽 Dish Results")
        grid_cols = st.columns(2)
        for idx, d in enumerate(res["results"]):
            badge = '<span class="veg-badge">🟢 VEG</span>' if d['is_veg'] else '<span class="non-veg-badge">🔴 NON-VEG</span>'
            bestseller = '<span style="background-color: #FFF8E7; color: #D97706; padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: 700;">★ BESTSELLER</span>' if d.get('is_bestseller') else ''
            
            with grid_cols[idx % 2]:
                st.markdown(f"""
                <div class="dish-card">
                    <div style="display: flex; justify-content: space-between;">
                        <div>
                            {badge} {bestseller}<br>
                            <span class="dish-title">{d['dish_name']}</span><br>
                            <span class="restaurant-title">at <b>{d['restaurant_name']}</b> ({d['locality']}) • 📍 {d['distance_km']} km</span>
                        </div>
                        <div style="text-align: right;">
                            <span class="price-tag">Rs. {d['price']}</span><br>
                            <small style="color: #888;">⭐ {d['rating']}</small>
                        </div>
                    </div>
                    <p style="color: #555; font-size: 0.9rem; margin-top: 0.6rem;">{d['description']}</p>
                    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #F0F0F0; padding-top: 0.5rem; font-size: 0.8rem; color: #777;">
                        <span>⏱ {d['delivery_time_mins']} mins • {d['calories_kcal']} kcal</span>
                        <span style="color: #E23744; font-weight: 600;">Match Confidence: {d.get('match_confidence', 'High')}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

