
import streamlit as st
import pandas as pd

def run():
    st.title("🔑 Sponsor Reset Token Manager")
    st.markdown("Track and reset admin tokens")
    df = pd.DataFrame({
        "Email": ["alice@demo.com", "bob@demo.com"],
        "Token Status": ["Active", "Expired"],
        "Last Reset": ["2024-06-01", "2024-04-18"]
    })
    st.dataframe(df)
    email = st.selectbox("Reset token for:", df["Email"])
    if st.button("Reset Token"):
        st.success(f"Token reset for {email}")
