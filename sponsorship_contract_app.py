import streamlit as st
from fill_sponsorship_contract import fill_contract
from datetime import date

def run():
    st.set_page_config(page_title="Contract Generator", layout="centered")
    st.title("📄 Generate Sponsorship Agreement")

    sponsors = {
        "NextGen Energy": {
            "Email": "sponsor@nextgen.com",
            "Address": "123 Sponsor Blvd, Energy City",
            "Asset Type": "Field Naming Rights",
            "Location": "Outdoor Field A",
            "Tier": "Gold",
            "Exclusivity": True,
            "Impressions": 250000,
            "Duration": 12,
            "Price": 35000
        },
        "ACME Corp": {
            "Email": "contact@acme.com",
            "Address": "789 ACME Ave, Industrial Park",
            "Asset Type": "Dome Naming Rights",
            "Location": "Main Dome",
            "Tier": "Exclusive Naming",
            "Exclusivity": True,
            "Impressions": 1000000,
            "Duration": 36,
            "Price": 125000
        }
    }

    facility_name = "National Sports Dome"
    facility_address = "456 Facility Way, Duluth, MN"

    sponsor_choice = st.selectbox("Select Sponsor", list(sponsors.keys()))
    generate = st.button("Generate Contract")

    if generate:
        sponsor = sponsors[sponsor_choice]
        contract_data = {
            "Date": str(date.today()),
            "Sponsor": sponsor_choice,
            "Email": sponsor["Email"],
            "Address": sponsor["Address"],
            "Facility": facility_name,
            "Facility Address": facility_address,
            "Asset Type": sponsor["Asset Type"],
            "Location": sponsor["Location"],
            "Tier": sponsor["Tier"],
            "Exclusivity": sponsor["Exclusivity"],
            "Impressions": sponsor["Impressions"],
            "Duration": sponsor["Duration"],
            "Price": sponsor["Price"]
        }

        output_path = "generated_contract.docx"
        filled_path = fill_contract(contract_data, output_path=output_path)

        with open(filled_path, "rb") as f:
            st.download_button("📥 Download Contract (DOCX)", f, file_name="sponsorship_agreement.docx")
