import streamlit as st

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "secure123"

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if not st.session_state.admin_logged_in:
    st.set_page_config(page_title="Admin Login", layout="centered")
    st.title("🔐 Admin Login")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == ADMIN_USERNAME and pw == ADMIN_PASSWORD:
            st.session_state.admin_logged_in = True
            st.success("Access granted.")
            st.stop()
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
        "Presentation Mode",
        "Creative Plan Generator",
        "Logout"
    ])

    if section == "Logout":
        st.session_state.admin_logged_in = False
        st.experimental_rerun()

    elif section == "Onboarding – Add Sponsor":
        import sponsor_admin_onboarding
        sponsor_admin_onboarding.run()

    elif section == "User Manager – Edit/Delete":
        import sponsor_admin_user_manager
        sponsor_admin_user_manager.run()

    elif section == "Token Manager – Password Reset":
        import sponsor_admin_token_manager
        sponsor_admin_token_manager.run()

    elif section == "Analytics Dashboard":
        import sponsor_admin_analytics
        sponsor_admin_analytics.run()

    elif section == "Usage Reporter":
        import sponsor_usage_reporter
        sponsor_usage_reporter.run()

    elif section == "Pricing Calculator":
        import sponsorship_pricing_app
        sponsorship_pricing_app.run()

    elif section == "Contract Generator":
        import sponsorship_contract_app
        sponsorship_contract_app.run()

    elif section == "Presentation Mode":
        import sponsor_presentation_mode
        sponsor_presentation_mode.run()

    elif section == "Creative Plan Generator":
        import creative_plan_generator
        creative_plan_generator.run()
