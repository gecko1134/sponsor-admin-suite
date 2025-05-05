
import streamlit as st
import pandas as pd
from sponsor_reset_token_manager import generate_reset_token, load_tokens, expire_token

def run():
    st.set_page_config(page_title="Token Manager", layout="wide")
    st.title("🔐 Password Reset Token Manager")

    st.subheader("Generate Reset Token")
    email = st.text_input("Sponsor Email")
    if st.button("Generate Token"):
        token = generate_reset_token(email)
        st.success(f"Generated Token: {token}")
        st.info("Share this token securely with the sponsor.")

    st.subheader("Active Tokens")
    tokens = load_tokens()
    if tokens:
        df = pd.DataFrame([
            {"Token": k, "Email": v["email"], "Expires": v["expires"]}
            for k, v in tokens.items()
        ])
        st.dataframe(df)

        selected_token = st.selectbox("Expire Token", options=list(tokens.keys()))
        if st.button("Expire Selected Token"):
            expire_token(selected_token)
            st.success("Token expired.")
    else:
        st.info("No active tokens.")
