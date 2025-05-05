import streamlit as st
from sponsor_optimizer import suggest_package, claim_package

def run():
    st.title("🧠 AI Sponsor Package Optimizer (Live Inventory Check)")

    budget = st.number_input("Enter Budget ($)", value=25000, step=1000)
    tier = st.selectbox("Preferred Tier", ["Bronze", "Silver", "Gold", "Presenting", "Exclusive Naming"])
    duration = st.slider("Preferred Duration (months)", 1, 240, 12)
    sponsor_name = st.text_input("Sponsor Name to Claim Package")

    if st.button("Generate Optimal Package"):
        result = suggest_package(budget=budget, tier=tier, preferred_duration=duration)

        if result["Recommended Package"]:
            st.success(result["Note"])
            st.write(f"**Total Estimated Cost:** ${result['Total Cost']:,.2f}")
            st.write(f"**Estimated Impressions:** {result['Estimated Impressions']:,}")
            st.markdown("### 📦 Package Contents")
            for item in result["Recommended Package"]:
                st.write(f"- {item['Asset']} ({item['Tier']}, {item['Duration']} mo): "
                         f"${item['Suggested Cost']:,.2f}, Est. {item['Estimated Impressions']:,} impressions "
                         f"({item['Remaining Slots']} slot(s) remaining)")

            if sponsor_name:
                if st.button("✅ Claim This Package"):
                    claim_package(result["Recommended Package"], sponsor_name=sponsor_name)
                    st.success("Package claimed and saved to ledger.")
            else:
                st.warning("Enter a sponsor name to enable claiming.")
        else:
            st.error("No package available for this budget and selection.")
