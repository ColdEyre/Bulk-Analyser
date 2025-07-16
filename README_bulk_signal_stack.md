
# 📊 Bulk Signal Stack Analyzer

This is a Streamlit app that allows you to upload a CSV file containing businesses and evaluates their acquisition-readiness using signal stacking criteria.

## How to Use
1. Upload a CSV with business details (e.g., from your Google Places scraper)
2. The app scores each business based on:
   - Review count
   - Presence of a website
   - Landline indicator
   - Owner visibility
   - Staff stability
   - Years in operation
3. Download the results as a scored CSV

## To Run Locally
```bash
pip install streamlit pandas
streamlit run bulk_signal_stack_app.py
```

## Expected CSV Headers
- Business Name
- Industry
- Years in Operation
- Google Review Count
- Has Website (Y/N)
- Landline Only (Y/N)
- Owner Name in Reviews (Y/N)
- Staff Stability (Y/N)
