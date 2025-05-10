
import streamlit as st

def run():
    st.title("🧮 Sponsorship Pricing Calculator")

    asset = st.selectbox("Asset", [
        "Court", "Turf (Half)", "Turf (Full)", "Team Suite", "Locker Room", 
        "Workout Facility", "Dome Naming Rights", "Food Truck Zone", "Retail Vendor", "Event"
    ])
    tier = st.selectbox("Tier", ["Bronze", "Silver", "Gold", "Platinum", "Title"])
    months = st.slider("Duration (months)", 1, 36, 12)

    base = {
        "Court": 6500, "Turf (Half)": 8000, "Turf (Full)": 15000,
        "Team Suite": 8000, "Locker Room": 5000, "Workout Facility": 5000,
        "Dome Naming Rights": 50000, "Food Truck Zone": 2500,
        "Retail Vendor": 10000, "Event": 3000
    }.get(asset, 3000)

    tier_multiplier = {"Bronze": 0.9, "Silver": 1.0, "Gold": 1.2, "Platinum": 1.4, "Title": 2.0}[tier]
    price = base * (months / 12) * tier_multiplier

    st.metric("Recommended Price", f"${price:,.0f}")
    st.markdown("_Auto-calculated using asset base × tier × duration_")
