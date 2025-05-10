
import streamlit as st
import pandas as pd

def run():
    st.title("👥 Sponsor Admin User Manager")
    st.subheader("Manage Sponsor Admin Users")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    role = st.selectbox("Role", ["Admin", "Viewer", "Finance"])
    if st.button("Add User"):
        st.success(f"User {name} ({email}) added with role {role}.")
    st.markdown("### Current Users")
    df = pd.DataFrame({
        "Name": ["Alice Admin", "Bob Viewer"],
        "Email": ["alice@demo.com", "bob@demo.com"],
        "Role": ["Admin", "Viewer"]
    })
    st.dataframe(df)
