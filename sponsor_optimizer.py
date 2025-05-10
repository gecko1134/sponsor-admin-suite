
import streamlit as st

def run():
    st.title("🧠 Sponsor Optimizer")
    goal = st.multiselect("Campaign Goals", ["Brand Awareness", "Youth Support", "Live Visibility"])
    budget = st.number_input("Budget ($)", value=10000)
    if st.button("Generate Optimized Package"):
        if budget < 5000:
            st.warning("Consider digital-only assets.")
        else:
            st.success("Recommended: Court Banner + Livestream Bundle + Concession Exposure")
