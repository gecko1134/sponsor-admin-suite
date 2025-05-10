
import streamlit as st

def run():
    st.title("📝 Sponsorship Contract App")
    sponsor = st.text_input("Sponsor Name")
    asset = st.selectbox("Asset", ["Court", "Team Suite", "Naming Rights", "Event Title"])
    duration = st.slider("Months", 1, 36, 12)
    value = st.number_input("Contract Value ($)", min_value=1000, value=5000)
    deliverables = st.text_area("Deliverables & Notes")
    if st.button("Save Contract"):
        st.success(f"Contract created for {sponsor} – {asset} at ${value:,.0f}")
        st.markdown(f"**Duration:** {duration} months")
        st.markdown(f"**Deliverables:** {deliverables if deliverables else 'N/A'}")
