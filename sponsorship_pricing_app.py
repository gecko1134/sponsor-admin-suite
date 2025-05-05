
import streamlit as st
from pricing_calculator import calculate_sponsorship_price

def run():
    st.set_page_config(page_title="Sponsorship Pricing", layout="centered")
    st.title("💵 Sponsorship Pricing Calculator")

    with st.form("pricing_form"):
        asset_type = st.selectbox("Asset Type", [
            "Dome Naming Rights", "Field Naming Rights", "Scoreboard Banner",
            "Digital Leaderboard", "Social Media Ad Spot", "Website Featured Logo"
        ])
        location = st.text_input("Location / Scope", "Entire Dome")
        base_value = st.number_input("Base Value ($)", value=10000, step=100)
        impressions = st.number_input("Estimated Impressions", value=250000, step=10000)
        exclusivity_level = st.slider("Exclusivity Level (0 = Shared, 5 = Fully Exclusive)", 0, 5, value=3)
        duration_months = st.number_input("Duration (months)", min_value=1, max_value=36, value=6)
        tier = st.selectbox("Sponsorship Tier", ["Bronze", "Silver", "Gold", "Presenting", "Exclusive Naming"])
        submitted = st.form_submit_button("Calculate Price")

    if submitted:
        result = calculate_sponsorship_price(
            asset_type=asset_type,
            location=location,
            base_value=base_value,
            impressions=impressions,
            exclusivity_level=exclusivity_level,
            duration_months=duration_months,
            tier=tier
        )

        st.subheader("Deal Summary")
        for key, val in result.items():
            st.write(f"**{key}:** {val}")
        
        st.markdown("---")
        if result["Recommendation"].startswith("Reject"):
            st.error(result["Recommendation"])
        elif result["Recommendation"].startswith("Revise"):
            st.warning(result["Recommendation"])
        else:
            st.success(result["Recommendation"])
