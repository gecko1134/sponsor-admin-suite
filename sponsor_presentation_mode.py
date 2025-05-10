
import streamlit as st

def run():
    st.title("🎤 Sponsor Presentation Mode")
    st.markdown("Use this view for meetings with sponsors.")
    sponsor = st.text_input("Sponsor Name")
    focus = st.selectbox("Presentation Focus", ["Digital", "On-Site Branding", "Events", "Naming Rights"])
    package = st.text_area("Custom Bundle Description")
    if st.button("Generate Pitch Slide"):
        st.success(f"Presentation view prepped for {sponsor} on {focus}")
        st.markdown(f"**Bundle:** {package}")
