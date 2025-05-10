
import streamlit as st

def run():
    st.title("📝 Sponsorship Contract App")

    sponsor = st.text_input("Sponsor Name")
    asset = st.selectbox("Asset", ["Court", "Team Suite", "Naming Rights", "Event Title"])
    tier = st.selectbox("Tier Level", ["Bronze", "Silver", "Gold", "Platinum", "Title Partner"])
    duration = st.slider("Contract Duration (months)", 1, 360, 12)

    base_price = {
        "Court": 6500, "Team Suite": 8000, "Naming Rights": 50000, "Event Title": 10000
    }

    tier_multiplier = {
        "Bronze": 0.9, "Silver": 1.0, "Gold": 1.2, "Platinum": 1.5, "Title Partner": 2.0
    }

    base = base_price.get(asset, 3000)
    price = base * (duration / 12) * tier_multiplier[tier]
    annual_price = price / (duration / 12) if duration else 0
    monthly_price = price / duration if duration else 0

    st.metric("Total Contract Value", f"${price:,.0f}")
    st.metric("Price Per Year", f"${annual_price:,.0f}")
    st.metric("Monthly Avg Cost", f"${monthly_price:,.0f}")

    deliverables = st.text_area("Deliverables & Notes")
    if st.button("Save Contract"):
        st.success(f"Contract created for {sponsor} – {asset} at ${price:,.0f}")
        st.markdown(f"**Duration:** {duration} months")
        st.markdown(f"**Deliverables:** {deliverables if deliverables else 'N/A'}")
