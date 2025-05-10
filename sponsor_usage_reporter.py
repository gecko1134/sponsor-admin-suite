
import streamlit as st
import pandas as pd

def run():
    st.title("📊 Sponsor Usage Reporter")
    df = pd.DataFrame({
        "Sponsor": ["GoldCo", "SportFuel"],
        "Asset": ["Court A", "Main Entrance Sign"],
        "Usage": ["12 events", "3,000 impressions"]
    })
    st.dataframe(df)
    st.download_button("Download Report", df.to_csv(index=False), "sponsor_usage.csv")
