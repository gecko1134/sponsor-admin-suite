import pandas as pd
import streamlit as st

def generate_sponsor_summary_report(log_path="sponsor_usage_log.csv", group_by="month"):
    if not pd.io.common.file_exists(log_path):
        return pd.DataFrame(), "No log file found."

    df = pd.read_csv(log_path, parse_dates=["Timestamp"])
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    if group_by == "week":
        df["Period"] = df["Timestamp"].dt.to_period("W").apply(lambda r: r.start_time.strftime('%Y-%m-%d'))
    else:
        df["Period"] = df["Timestamp"].dt.to_period("M").astype(str)

    summary = df.groupby(["Period", "Sponsor Email", "Action"]).size().reset_index(name="Count")
    pivot = summary.pivot_table(index=["Period", "Sponsor Email"], columns="Action", values="Count", fill_value=0).reset_index()

    return pivot, "Report generated."

def run():
    st.title("📊 Usage Report Generator")
    log_path = "sponsor_usage_log.csv"
    group_by = st.selectbox("Group by", ["month", "week"])
    summary_df, msg = generate_sponsor_summary_report(log_path, group_by)

    if summary_df.empty:
        st.warning(msg)
    else:
        st.dataframe(summary_df)
        csv = summary_df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", csv, file_name="sponsor_summary.csv", mime="text/csv")
