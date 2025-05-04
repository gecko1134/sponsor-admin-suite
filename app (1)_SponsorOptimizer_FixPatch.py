import streamlit as st

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "secure123"

# Safe session state initialization
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if not st.session_state.admin_logged_in:
    st.title("🔐 Admin Login")
    user = st.text_input("Username", key="username")
    pw = st.text_input("Password", type="password", key="password")
    login_btn = st.button("Login")

    if login_btn:
        if user == ADMIN_USERNAME and pw == ADMIN_PASSWORD:
            st.session_state.admin_logged_in = True
            st.success("Access granted.")
            st.stop()  # Stop instead of rerun
        else:
            st.error("Invalid credentials.")
else:
    st.title("🧭 Admin Dashboard")
    st.write("Welcome to the secure sponsor admin suite.")
    # Additional admin tools would go here
