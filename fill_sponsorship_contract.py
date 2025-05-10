
import streamlit as st

def run():
    st.title("📝 Fill Sponsorship Contract")

    assets = [
        "Court", "Turf (Half)", "Turf (Full)", "Team Suite", "Locker Room",
        "Workout Facility", "Dome Naming Rights", "Food Truck Zone",
        "Retail Vendor", "Event Naming Rights"
    ]
    tiers = ["Bronze", "Silver", "Gold", "Platinum", "Title Partner"]

    sponsor = st.text_input("Sponsor Name")
    asset = st.selectbox("Sponsored Asset", assets)
    tier = st.selectbox("Tier Level", tiers)
    duration = st.slider("Contract Duration (months)", 1, 36, 12)

    base_price = {
        "Court": 6500, "Turf (Half)": 8000, "Turf (Full)": 15000,
        "Team Suite": 8000, "Locker Room": 5000, "Workout Facility": 5000,
        "Dome Naming Rights": 50000, "Food Truck Zone": 2500,
        "Retail Vendor": 10000, "Event Naming Rights": 10000
    }

    tier_multiplier = {
        "Bronze": 0.9, "Silver": 1.0, "Gold": 1.2,
        "Platinum": 1.5, "Title Partner": 2.0
    }

    base = base_price.get(asset, 3000)
    price = base * (duration / 12) * tier_multiplier.get(tier, 1.0)

    st.metric("Suggested Contract Value", f"${price:,.0f}")
    notes = st.text_area("Additional Notes or Deliverables")

    if st.button("Generate Summary"):
        st.success(f"Contract for {sponsor} confirmed.")
        st.markdown(f"**Asset:** {asset} | **Tier:** {tier} | **Duration:** {duration} months")
        st.markdown(f"**Suggested Value:** ${price:,.0f}")
        st.markdown(f"**Notes:** {notes if notes else 'None'}")
