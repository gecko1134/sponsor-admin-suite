
import streamlit as st
import pandas as pd

def run():
    st.title("🔁 Auto-Renewal Engine")
    df = pd.DataFrame({
        "Sponsor": ["GoldCo", "SportFuel"],
        "End Date": ["2024-10-01", "2024-12-15"],
        "Auto-Renew": ["Yes", "No"]
    })
    st.dataframe(df)
    st.markdown("Sponsors within 90 days of renewal:")
    st.warning("GoldCo needs renewal reminder.")
