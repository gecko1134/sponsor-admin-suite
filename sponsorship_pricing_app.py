
import streamlit as st

def run():
    st.title("💰 Sponsorship Pricing App")
    asset = st.selectbox("Asset Type", ["Court", "Dome", "Team Suite", "Digital Ad", "Event"])
    base_price = {"Court": 6500, "Dome": 25000, "Team Suite": 8000, "Digital Ad": 3000, "Event": 5000}
    duration = st.slider("Duration (months)", 1, 36, 12)
    tier = st.selectbox("Tier", ["Bronze", "Silver", "Gold", "Platinum", "Title Partner"])
    tier_multiplier = {"Bronze": 0.9, "Silver": 1.0, "Gold": 1.25, "Platinum": 1.5, "Title Partner": 2.0}
    price = base_price.get(asset, 3000) * (duration / 12) * tier_multiplier[tier]
    st.metric("Suggested Price", f"${price:,.0f}")
