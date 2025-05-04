import streamlit as st
import pandas as pd
import os
from sponsor_usage_reporter import generate_sponsor_summary_report

st.set_page_config(page_title="Sponsor Admin Analytics", layout="wide")
st.title("📊 Sponsor Activity Analytics & Reporting")

LOG_FILE = "sponsor_usage_log.csv"

if not os.path.exists(LOG_FILE):
    st.warning("No sponsor activity log found yet.")
else:
    df = pd.read_csv(LOG_FILE)

    tab = st.radio("Select View", ["Full Log Viewer", "Summary Report Generator"])

    if tab == "Full Log Viewer":
        st.subheader("📋 Full Activity Log")
        st.dataframe(df)

        st.subheader("🔍 Filter by Criteria")
        sponsor_filter = st.multiselect("Sponsor Email", options=df["Sponsor Email"].unique())
        action_filter = st.multiselect("Action Type", options=df["Action"].unique())
        date_range = st.date_input("Filter by Date Range", [])

        filtered_df = df.copy()
        if sponsor_filter:
            filtered_df = filtered_df[filtered_df["Sponsor Email"].isin(sponsor_filter)]
        if action_filter:
            filtered_df = filtered_df[filtered_df["Action"].isin(action_filter)]
        if len(date_range) == 2:
            start_date = pd.to_datetime(date_range[0])
            end_date = pd.to_datetime(date_range[1])
            filtered_df["Timestamp"] = pd.to_datetime(filtered_df["Timestamp"])
            filtered_df = filtered_df[(filtered_df["Timestamp"] >= start_date) & (filtered_df["Timestamp"] <= end_date)]

        st.write("📈 Filtered Results")
        st.dataframe(filtered_df)

        csv_export = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Filtered Report", data=csv_export, file_name="filtered_sponsor_activity.csv", mime="text/csv")

    elif tab == "Summary Report Generator":
        st.subheader("📆 Generate Activity Summary")
        group_by = st.selectbox("Group by", ["month", "week"])
        summary_df, msg = generate_sponsor_summary_report(LOG_FILE, group_by=group_by)

        if summary_df.empty:
            st.warning(msg)
        else:
            st.dataframe(summary_df)
            summary_csv = summary_df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Summary CSV", data=summary_csv, file_name=f"sponsor_summary_{group_by}.csv", mime="text/csv")
