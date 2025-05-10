
import streamlit as st
import pandas as pd

def run():
    st.title("📦 Complete Sponsorship Inventory Tracker – Venture North")

    st.markdown("### Indoor & Dome Zones")
    dome_inventory = pd.DataFrame({
        "Asset": [
            "Full Turf Field", "Half Turf (1)", "Half Turf (2)", "Court A", "Court B",
            "Court C", "Court D", "Batting Cage 1", "Batting Cage 2", "Workout Facility",
            "Team Suite 1", "Team Suite 2", "Team Suite 3", "Team Suite 4",
            "Team Suite 5", "Team Suite 6", "Locker Room A", "Locker Room B"
        ],
        "Status": ["Available", "Sold", "Available", "Sold", "Available", "Available", "Available",
                   "Available", "Sold", "Available", "Sold", "Available", "Sold", "Available",
                   "Available", "Available", "Available", "Available"],
        "Tier": ["Platinum", "Gold", "Gold", "Silver", "Silver", "Silver", "Silver",
                 "Bronze", "Bronze", "Gold", "Gold", "Gold", "Gold", "Gold", "Gold", "Gold", "Gold", "Gold"],
        "Price ($)": [15000, 8000, 8000, 6500, 6500, 6500, 6500, 3000, 3000, 5000, 8000, 8000, 8000, 8000, 8000, 8000, 5000, 5000],
        "Start": ["TBD"] * 18,
        "End": ["TBD"] * 18,
        "Slots": [1] * 18,
        "Renewal Notes": [""] * 18
    })

    st.dataframe(dome_inventory)

    st.markdown("### Outdoor, Vendor & Special Sponsorship Zones")
    other_inventory = pd.DataFrame({
        "Asset": [
            "Dome Naming Rights", "Main Entrance", "Wellness Wing", "Food Truck Zone A",
            "Food Truck Zone B", "Retail Vendor Zone", "Healthcare Partner", "Parking Zone"
        ],
        "Status": ["Available", "Sold", "Available", "Available", "Available", "Sold", "Sold", "Available"],
        "Tier": ["Title", "Platinum", "Premier", "Community", "Community", "Premier", "Premier", "Community"],
        "Price ($)": [50000, 15000, 20000, 2500, 2500, 10000, 20000, 5000],
        "Start": ["TBD"] * 8,
        "End": ["TBD"] * 8,
        "Slots": [1] * 8,
        "Renewal Notes": ["Multi-year available", "", "", "", "", "", "", "VIP sponsor parking available"]
    })

    st.dataframe(other_inventory)

    st.download_button("📤 Download All Inventory (CSV)", 
                       pd.concat([dome_inventory, other_inventory]).to_csv(index=False),
                       "venture_north_sponsorship_inventory.csv")
