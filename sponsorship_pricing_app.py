
import streamlit as st

def run():
    st.title("💰 Sponsorship Pricing App (Expanded)")

    st.subheader("📦 Asset & Contract Configuration")
    asset = st.selectbox("Sponsored Asset", [
        "Court", "Turf (Half)", "Turf (Full)", "Team Suite", "Locker Room",
        "Workout Facility", "Dome Naming Rights", "Food Truck Zone",
        "Retail Vendor", "Event Naming Rights", "Wellness Wing", "Batting Cage",
        "Parking Zone", "Livestream Bundle", "Mobile App Banner"
    ])
    tier = st.selectbox("Tier Level", ["Bronze", "Silver", "Gold", "Platinum", "Title Partner"])
    duration = st.slider("Contract Duration (months)", 1, 360, 12)

    st.subheader("💰 Price Estimate")

    base_prices = {
        "Court": 6500, "Turf (Half)": 8000, "Turf (Full)": 15000,
        "Team Suite": 8000, "Locker Room": 5000, "Workout Facility": 5000,
        "Dome Naming Rights": 50000, "Food Truck Zone": 2500,
        "Retail Vendor": 10000, "Event Naming Rights": 10000,
        "Wellness Wing": 12000, "Batting Cage": 4000,
        "Parking Zone": 5000, "Livestream Bundle": 3000, "Mobile App Banner": 2500
    }

    tier_multiplier = {
        "Bronze": 0.9, "Silver": 1.0, "Gold": 1.2, "Platinum": 1.5, "Title Partner": 2.0
    }

    base = base_prices.get(asset, 3000)
    multiplier = tier_multiplier.get(tier, 1.0)
    price = base * (duration / 12) * multiplier

    st.metric("Suggested Price", f"${price:,.0f}")
    st.markdown("_Pricing = Base × Tier Multiplier × (Duration / 12)_")
