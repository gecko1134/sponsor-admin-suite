
import streamlit as st
import requests

def run():
    st.title("🔗 WordPress Sync Tools")
    st.markdown("Push updates to your WordPress site using REST API.")
    url = st.text_input("WordPress API URL")
    token = st.text_input("Bearer Token", type="password")
    if st.button("Send Test"):
        st.success("Mock push successful (demo mode).")
