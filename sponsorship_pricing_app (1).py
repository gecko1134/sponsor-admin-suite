
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
    total_price = base * (duration / 12) * multiplier
    annual_price = total_price / (duration / 12) if duration else 0
    monthly_price = total_price / duration if duration else 0

    st.metric("Total Contract Value", f"${total_price:,.0f}")
    st.metric("Price Per Year", f"${annual_price:,.0f}")
    st.metric("Monthly Avg Cost", f"${monthly_price:,.0f}")

    st.markdown("_Formula: Base × Tier Multiplier × (Duration / 12)_")
