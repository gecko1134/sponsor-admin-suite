
import streamlit as st
import pandas as pd

def run():
    st.title("📦 Sponsorship Inventory Checklist")
    df = pd.DataFrame({
        "Asset": ["Court A", "Dome Banner", "App Footer Ad"],
        "Status": ["Sold", "Available", "Sold"]
    })
    st.dataframe(df)
