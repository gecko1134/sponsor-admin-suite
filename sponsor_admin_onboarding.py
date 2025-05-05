import streamlit as st
import json
import os

def run():
    SPONSOR_DB = "sponsor_accounts.json"

    def load_accounts():
        if os.path.exists(SPONSOR_DB):
            with open(SPONSOR_DB, "r") as f:
                return json.load(f)
        return {}

    def save_accounts(accounts):
        with open(SPONSOR_DB, "w") as f:
            json.dump(accounts, f, indent=2)

    st.title("👥 Add a New Sponsor Account")

    accounts = load_accounts()

    with st.form("onboard_form"):
        email = st.text_input("Sponsor Email")
        name = st.text_input("Sponsor Name")
        password = st.text_input("Temporary Password")
        submitted = st.form_submit_button("Add Sponsor")

        if submitted:
            if email in accounts:
                st.warning("That email is already registered.")
            else:
                accounts[email] = {"name": name, "password": password}
                save_accounts(accounts)
                st.success(f"Sponsor '{name}' added successfully.")

    st.subheader("Current Sponsors")
    for email, data in accounts.items():
        st.markdown(f"- **{data['name']}** ({email})")
