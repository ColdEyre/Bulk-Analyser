
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bulk Signal Stack Analyzer", layout="wide")
st.title("📊 Bulk Signal Stack Analyzer")

st.markdown("""
Upload a CSV of businesses (e.g., from your Google Maps/Places API or scraper), and this tool will score each one based on acquisition-readiness using signal stacking.
""")

uploaded_file = st.file_uploader("📁 Upload your CSV file", type="csv")

def score_business(row):
    score = 0
    if row.get("Years in Operation", 0) >= 10:
        score += 2
    elif row.get("Years in Operation", 0) >= 5:
        score += 1
    if row.get("Google Review Count", 0) >= 100:
        score += 2
    elif row.get("Google Review Count", 0) >= 50:
        score += 1
    if row.get("Has Website (Y/N)", "N") == "N":
        score += 2
    if row.get("Landline Only (Y/N)", "N") == "Y":
        score += 1
    if row.get("Owner Name in Reviews (Y/N)", "N") == "Y":
        score += 2
    if row.get("Staff Stability (Y/N)", "N") == "Y":
        score += 1
    return min(score, 10)

def get_verdict(score):
    if score >= 8:
        return "✅ Strong"
    elif score >= 5:
        return "⚠️ Moderate"
    else:
        return "❌ Weak"

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Handle missing columns gracefully
    expected_cols = [
        "Business Name", "Industry", "Years in Operation",
        "Google Review Count", "Has Website (Y/N)",
        "Landline Only (Y/N)", "Owner Name in Reviews (Y/N)",
        "Staff Stability (Y/N)"
    ]
    for col in expected_cols:
        if col not in df.columns:
            df[col] = ""

    df["Score"] = df.apply(score_business, axis=1)
    df["Verdict"] = df["Score"].apply(get_verdict)

    st.success(f"{len(df)} businesses analyzed and scored.")
    st.dataframe(df[["Business Name", "Industry", "Years in Operation", "Google Review Count", "Score", "Verdict"]])

    st.download_button(
        label="📥 Download Scored CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="Scored_Businesses.csv",
        mime="text/csv"
    )
