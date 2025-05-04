import streamlit as st
from sponsor_reset_token_manager import generate_reset_token, load_tokens, expire_token
import pandas as pd

st.set_page_config(page_title="Sponsor Token Manager", layout="wide")
st.title("🔐 Password Reset Token Manager")

# Generate new token
st.subheader("Generate Reset Token")
email = st.text_input("Sponsor Email")
if st.button("Generate Token"):
    token = generate_reset_token(email)
    st.success(f"Generated Token: {token}")
    st.info("Copy and share this token securely with the sponsor.")

# Display existing tokens
st.subheader("Active Tokens")
tokens = load_tokens()
if tokens:
    df = pd.DataFrame([
        {"Token": k, "Email": v["email"], "Expires": v["expires"]}
        for k, v in tokens.items()
    ])
    st.dataframe(df)

    selected_token = st.selectbox("Select Token to Expire", options=list(tokens.keys()))
    if st.button("Expire Token"):
        expire_token(selected_token)
        st.success("Token expired.")
else:
    st.info("No active tokens found.")
