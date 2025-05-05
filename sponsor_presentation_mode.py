import streamlit as st
import json
from pricing_calculator import calculate_sponsorship_price

def run():
    st.title("🎁 Build a Sponsor Package – Live Presentation Mode")

    with open("sponsorship_assets.json", "r") as f:
        asset_list = json.load(f)

    with st.form("builder_form"):
        col1, col2 = st.columns(2)

        with col1:
            asset_type = st.selectbox("Choose Sponsorship Asset", asset_list)
            location = st.text_input("Asset Location or Zone", "Main Dome")
            base_value = st.number_input("Base Value ($)", value=10000, step=100)

        with col2:
            tier = st.selectbox("Select Sponsorship Tier", ["Bronze", "Silver", "Gold", "Presenting", "Exclusive Naming"])
            exclusivity = st.slider("Exclusivity Level", 0, 5, 3)
            duration = st.slider("Sponsorship Duration (months)", 1, 36, 12)
            impressions = st.number_input("Estimated Impressions", value=250000, step=10000)

        submit = st.form_submit_button("Calculate Package")

    if submit:
        result = calculate_sponsorship_price(
            asset_type=asset_type,
            location=location,
            base_value=base_value,
            impressions=impressions,
            exclusivity_level=exclusivity,
            duration_months=duration,
            tier=tier
        )

        st.markdown("## 📋 Package Summary")
        st.write(f"**Asset:** {asset_type} – {location}")
        st.write(f"**Tier:** {tier}")
        st.write(f"**Duration:** {duration} months")
        st.write(f"**Estimated Impressions:** {impressions}")
        st.write(f"**Exclusivity Level:** {exclusivity}")
        st.write(f"**Base Value:** ${base_value:,.2f}")
        st.write("---")
        st.subheader("💰 Pricing Breakdown")
        st.write(f"**Suggested Price:** ${result['Final Suggested Price']:,.2f}")
        st.write(f"**Market Average:** ${result['Market Average']:,.2f}")
        st.write(f"**Position vs Market:** {result['Comparison to Market']}")
        st.success(f"✅ Recommendation: {result['Recommendation']}")
