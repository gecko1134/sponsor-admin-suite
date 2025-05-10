
import streamlit as st
import pandas as pd

def run():
    st.title("🔑 Admin Token Manager")
    df = pd.DataFrame({
        "Admin": ["admin@demo.com", "bob@demo.com"],
        "Token": ["abc123", "xyz456"],
        "Expires": ["2024-12-01", "2024-07-15"]
    })
    st.dataframe(df)
    email = st.selectbox("Revoke Token For", df["Admin"])
    if st.button("Revoke Token"):
        st.warning(f"Token for {email} revoked.")
