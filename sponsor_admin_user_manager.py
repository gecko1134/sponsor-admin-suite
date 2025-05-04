import streamlit as st
st.set_page_config(page_title="Sponsor User Manager", layout="wide")

import json
import os

SPONSOR_DB = "sponsor_accounts.json"

def load_accounts():
    if os.path.exists(SPONSOR_DB):
        with open(SPONSOR_DB, "r") as f:
            return json.load(f)
    return {}

def save_accounts(accounts):
    with open(SPONSOR_DB, "w") as f:
        json.dump(accounts, f, indent=2)

st.title("🔐 Sponsor Account Manager")

accounts = load_accounts()

if not accounts:
    st.warning("No sponsor accounts found.")
else:
    selected_email = st.selectbox("Select Sponsor Email", list(accounts.keys()))
    sponsor = accounts[selected_email]

    name = st.text_input("Sponsor Name", value=sponsor.get("name", ""))
    password = st.text_input("Password", value=sponsor.get("password", ""))

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save Changes"):
            accounts[selected_email] = {"name": name, "password": password}
            save_accounts(accounts)
            st.success("Changes saved.")

    with col2:
        if st.button("🗑️ Delete Sponsor"):
            del accounts[selected_email]
            save_accounts(accounts)
            st.warning("Sponsor deleted.")

    st.markdown("---")
    st.subheader("All Sponsors")
    for email, data in accounts.items():
        st.markdown(f"- **{data['name']}** ({email})")
