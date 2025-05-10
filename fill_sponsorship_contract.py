
import streamlit as st

def run():
    st.title("📝 Fill Sponsorship Contract")
    name = st.text_input("Sponsor Name")
    asset = st.selectbox("Sponsored Asset", ["Court A", "Livestream", "Event Title"])
    value = st.number_input("Contract Value ($)", min_value=0)
    if st.button("Generate Contract"):
        st.success(f"Contract created for {name} – {asset} @ ${value}")
