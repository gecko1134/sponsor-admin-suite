
import streamlit as st

def run():
    st.title("📊 Pricing Calculator")
    asset = st.selectbox("Asset Type", ["Court", "Event", "Digital", "Naming Rights"])
    duration = st.slider("Months", 1, 12, 6)
    base = 1000 if asset == "Court" else 2500
    rate = base * (duration / 3)
    st.metric("Suggested Price", f"${rate:,.2f}")
