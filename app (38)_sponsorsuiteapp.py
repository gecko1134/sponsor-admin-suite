
import streamlit as st
from pathlib import Path
import importlib.util

st.set_page_config(page_title="Sponsor Admin Suite", layout="wide")

st.sidebar.title("🧭 Sponsor Admin Navigation")

modules = [
    "sponsor_admin_onboarding", "sponsor_admin_user_manager", "sponsor_admin_token_manager",
    "sponsor_reset_token_manager", "sponsor_intelligence_feed", "sponsor_optimizer",
    "sponsor_presentation_mode", "sponsor_portal", "sponsor_usage_reporter",
    "sponsor_admin_analytics", "fill_sponsorship_contract", "sponsorship_pricing_app",
    "sponsorship_contract_app", "pricing_calculator", "inventory_checklist",
    "creative_plan_generator", "auto_renewal_engine", "wp_sync_tools", "wp_embed_module", "flipbook_embed"
]

tab = st.sidebar.selectbox("Choose Module", ["Welcome"] + [m.replace("_", " ").title() for m in modules])

if tab == "Welcome":
    st.title("🎯 Sponsor Admin Suite")
    st.markdown("Use the sidebar to access contracts, analytics, dashboards, and tools.")
else:
    mod_name = tab.replace(" ", "_").lower()
    file_path = Path(__file__).parent / f"{mod_name}.py"
    try:
        spec = importlib.util.spec_from_file_location(mod_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.run()
    except Exception as e:
        st.error(f"⚠️ Failed to load module: {mod_name}")
        st.exception(e)
