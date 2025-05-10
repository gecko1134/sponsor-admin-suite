
import streamlit as st

def run():
    st.title("🌐 WordPress Embed Instructions")
    st.markdown("Use the HTML block in WordPress:")
    st.code('<iframe src="https://your-app.streamlit.app/?embed=true" width="100%" height="600" frameborder="0"></iframe>', language="html")
