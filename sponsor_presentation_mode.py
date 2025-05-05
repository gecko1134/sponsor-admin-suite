import streamlit as st
import json
from sponsor_optimizer import suggest_package

def run():
    st.title("🧠 AI Sponsor Package Optimizer")

    budget = st.number_input("Enter Budget ($)", value=25000, step=1000)
    tier = st.selectbox("Preferred Tier", ["Bronze", "Silver", "Gold", "Presenting", "Exclusive Naming"])
    duration = st.slider("Preferred Duration (months)", 1, 36, 12)

    if st.button("Generate Optimal Package"):
        result = suggest_package(budget=budget, tier=tier, preferred_duration=duration)

        if result["Recommended Package"]:
            st.success(result["Note"])
            st.write(f"**Total Estimated Cost:** ${result['Total Cost']:,.2f}")
            st.write(f"**Estimated Impressions:** {result['Estimated Impressions']:,}")
            st.markdown("### 📦 Package Contents")
            for item in result["Recommended Package"]:
                st.write(f"- {item['Asset']} ({item['Tier']}, {item['Duration']} mo): ${item['Suggested Cost']:,.2f}, Est. {item['Estimated Impressions']:,} impressions")
        else:
            st.error("No package available for this budget.")
