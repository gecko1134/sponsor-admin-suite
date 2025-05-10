
import streamlit as st

def run():
    st.title("🤖 AI Sponsor Match Scoring Tool")

    st.markdown("This tool uses weighted scoring from your Nexus Domes sponsorship questionnaire.")

    st.subheader("📋 Sponsorship Goals")
    awareness = st.slider("Brand Awareness Importance", 0, 10, 5)
    community = st.slider("Community Involvement", 0, 10, 5)
    athlete_support = st.slider("Athlete Access & NIL", 0, 10, 5)

    st.subheader("💸 Budget & Duration")
    budget = st.number_input("Estimated Budget ($)", min_value=0)
    duration = st.slider("Contract Duration (months)", 1, 36, 12)

    st.subheader("🎯 Activation Preferences")
    wants_naming = st.checkbox("Interested in Naming Rights?")
    wants_digital = st.checkbox("Wants Digital Visibility?")
    wants_exclusivity = st.checkbox("Exclusive Category Request?")

    if st.button("🔍 Calculate Match Score"):
        goal_score = awareness * 2 + community * 1.5 + athlete_support * 2
        budget_score = min(budget / 1000, 30)
        duration_score = duration / 12 * 10
        bonus = 0
        if wants_naming: bonus += 10
        if wants_digital: bonus += 5
        if wants_exclusivity: bonus += 10

        total_score = goal_score + budget_score + duration_score + bonus
        tier = (
            "Title Partner" if total_score >= 90 else
            "Premier Sponsor" if total_score >= 70 else
            "Community Sponsor" if total_score >= 50 else
            "Entry-Level Sponsor"
        )

        st.success(f"🎯 Match Score: {int(total_score)} / 100")
        st.markdown(f"**Recommended Tier: {tier}**")
        st.info("Use this insight to guide proposal customization and follow-up.")
