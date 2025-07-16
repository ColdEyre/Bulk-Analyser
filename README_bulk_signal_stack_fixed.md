
# 📊 Bulk Signal Stack Analyzer

This Streamlit app scores a list of businesses based on acquisition-readiness using signal stacking criteria.

## Features
- Upload a CSV file with business details
- Automatically scores each business on:
  - Years in operation
  - Google review count
  - Website presence
  - Landline contact
  - Owner presence in reviews
  - Staff stability
- Verdicts: ✅ Strong, ⚠️ Moderate, ❌ Weak
- Download the scored CSV

## Required Columns in Your CSV
- Business Name
- Industry
- Years in Operation
- Google Review Count
- Has Website (Y/N)
- Landline Only (Y/N)
- Owner Name in Reviews (Y/N)
- Staff Stability (Y/N)

## To Run Locally
```bash
pip install streamlit pandas
streamlit run bulk_signal_stack_app_fixed.py
```
