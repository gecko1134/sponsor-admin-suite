
import streamlit as st

def run():
    st.title("📖 Investor Flipbook")
    st.markdown("Live view:")
    st.components.v1.iframe("https://online.flippingbook.com/view/893923349/", height=600)
