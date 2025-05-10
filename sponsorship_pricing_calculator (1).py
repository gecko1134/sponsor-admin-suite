
import streamlit as st

def run():
    st.title("🧮 Sponsorship Pricing Calculator")

    st.subheader("📦 Asset Selection")
    asset = st.selectbox("Select Sponsored Asset", [
        "Court", "Turf (Half)", "Turf (Full)", "Team Suite", "Locker Room",
        "Workout Facility", "Dome Naming Rights", "Food Truck Zone", "Retail Vendor", "Event"
    ])
    tier = st.selectbox("Tier Level", ["Bronze", "Silver", "Gold", "Platinum", "Title Partner"])
    months = st.slider("Duration (in months)", 1, 36, 12)

    st.subheader("💰 Pricing Estimate")
    base_prices = {
        "Court": 6500, "Turf (Half)": 8000, "Turf (Full)": 15000,
        "Team Suite": 8000, "Locker Room": 5000, "Workout Facility": 5000,
        "Dome Naming Rights": 50000, "Food Truck Zone": 2500,
        "Retail Vendor": 10000, "Event": 3000
    }

    tier_multiplier = {
        "Bronze": 0.9, "Silver": 1.0, "Gold": 1.2,
        "Platinum": 1.5, "Title Partner": 2.0
    }

    base = base_prices.get(asset, 3000)
    multiplier = tier_multiplier.get(tier, 1.0)

    price = base * (months / 12) * multiplier
    st.metric(label="Recommended Price", value=f"${price:,.0f}")
    st.markdown("_Pricing = Base × Tier Multiplier × Contract Duration_")
