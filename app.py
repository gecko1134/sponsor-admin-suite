import streamlit as st
import importlib

# Hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "secure123"

# Authentication check
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if not st.session_state.admin_logged_in:
    st.title("🔐 Admin Login")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == ADMIN_USERNAME and pw == ADMIN_PASSWORD:
            st.session_state.admin_logged_in = True
            st.success("Access granted.")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials.")
else:
    st.set_page_config(page_title="Sponsor Admin Dashboard", layout="wide")
    st.title("🧭 Sponsor Admin Dashboard")

    section = st.sidebar.radio("Select Admin Tool", [
        "Onboarding – Add Sponsor",
        "User Manager – Edit/Delete",
        "Token Manager – Password Reset",
        "Analytics Dashboard",
        "Usage Reporter",
        "Pricing Calculator",
        "Contract Generator",
        "Logout"
    ])

    if section == "Logout":
        st.session_state.admin_logged_in = False
        st.experimental_rerun()

    elif section == "Onboarding – Add Sponsor":
        st.subheader("➕ Add New Sponsor")
        import sponsor_admin_onboarding

    elif section == "User Manager – Edit/Delete":
        st.subheader("👤 Manage Sponsor Accounts")
        import sponsor_admin_user_manager

    elif section == "Token Manager – Password Reset":
        st.subheader("🔐 Token Manager")
        import sponsor_admin_token_manager

    elif section == "Analytics Dashboard":
        st.subheader("📊 View Sponsor Logs")
        import sponsor_admin_analytics

    elif section == "Usage Reporter":
        st.subheader("📆 Generate Activity Reports")
        import sponsor_usage_reporter

    elif section == "Pricing Calculator":
        st.subheader("💵 Run Sponsorship Pricing Tool")
        import sponsorship_pricing_app

    elif section == "Contract Generator":
        st.subheader("📄 Generate Sponsorship Agreement")
        import sponsorship_contract_app
