
import streamlit as st

def run():
    st.title("🧠 AI Sponsorship Pricing & ROI Optimizer")

    st.markdown("### 🎯 Sponsorship Goals")
    goals = st.multiselect("Select Goals", ["Brand Awareness", "Community Impact", "Event Presence", "Youth Development", "Digital Reach"])
    audience = st.slider("Estimated Impressions", 1000, 1000000, 100000, step=5000)
    engagement_rate = st.slider("Expected Engagement (%)", 0.0, 20.0, 4.0)

    st.markdown("### 💼 Budget & Package Setup")
    budget = st.number_input("Total Budget ($)", min_value=1000, value=10000, step=500)
    duration = st.slider("Contract Duration (months)", 1, 60, 12)
    exclusivity = st.radio("Exclusive Category?", ["Yes", "No"])

    st.markdown("### 🧮 AI-Suggested Package")

    # Mock combo output
    if budget < 5000:
        suggestion = ["Mobile App Banner", "Livestream Bundle"]
    elif budget < 15000:
        suggestion = ["Court A Banner", "Food Truck Zone", "Batting Cage"]
    else:
        suggestion = ["Dome Naming Rights", "Livestream", "Team Suite", "Event Series"]

    roi_estimate = (audience * (engagement_rate / 100) * 2.5) / budget if budget else 0
    value_generated = audience * 0.02 + (engagement_rate * 100)

    st.success(f"📦 Suggested Assets: {', '.join(suggestion)}")
    st.metric("Estimated ROI", f"{roi_estimate:.2f}x")
    st.metric("Estimated Exposure Value", f"${value_generated:,.0f}")

    st.markdown("Use this recommendation in your proposal or contract discussion.")
