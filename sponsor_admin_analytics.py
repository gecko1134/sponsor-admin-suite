
import streamlit as st
import pandas as pd

def run():
    st.title("📈 Sponsor Analytics")
    st.markdown("Basic performance breakdown:")
    st.metric("Total Sponsors", 28)
    st.metric("Avg Contract Size", "$12,800")
    st.metric("Most Viewed Asset", "Court A Banner")
