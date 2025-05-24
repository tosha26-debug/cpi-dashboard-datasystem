# run.py

import requests
import pandas as pd
import streamlit as st

# ----------------------------------------------------------
# API Base URLs
# ----------------------------------------------------------
# Symbols API URL
BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"    

# CPI API URL (local for now)
CPI_BASE_URL = "http://127.0.0.1:8000"

# ----------------------------------------------------------
# Fetch Symbols Data
# ----------------------------------------------------------
SYMBOLS_ENDPOINT = f"{BASE_URL}/v0/symbols/"
params = {"skip": 0, "limit": 100}
response = requests.get(SYMBOLS_ENDPOINT, params=params)
response.raise_for_status()
symbols_data = response.json()
symbols_df = pd.DataFrame(symbols_data)

# ----------------------------------------------------------
# Fetch CPI Facts Data
# ----------------------------------------------------------
CPI_FACTS_ENDPOINT = f"{CPI_BASE_URL}/v0/cpi/facts"
cpi_response = requests.get(CPI_FACTS_ENDPOINT)
cpi_response.raise_for_status()
cpi_data = cpi_response.json()
cpi_df = pd.DataFrame(cpi_data)

# Ensure 'date' is datetime
cpi_df['date'] = pd.to_datetime(cpi_df['date'])
cpi_df = cpi_df.sort_values('date')

# ----------------------------------------------------------
# Streamlit App Layout
# ----------------------------------------------------------
st.title("📊 Stock Symbols & CPI Data Dashboard")

# Sidebar Section
st.sidebar.title("🔎 Filters")

# ----------------------------------------------------------
# Symbols Dashboard
# ----------------------------------------------------------
st.header("🏢 Symbol Data")

# Filters for Symbols
st.sidebar.subheader("Symbols Filters")
selected_sectors = st.sidebar.multiselect("Select Sector(s)", symbols_df['sector'].dropna().unique())
selected_industries = st.sidebar.multiselect("Select Industry(ies)", symbols_df['industry'].dropna().unique())

# Apply Filters
filtered_symbols_df = symbols_df.copy()
if selected_sectors:
    filtered_symbols_df = filtered_symbols_df[filtered_symbols_df['sector'].isin(selected_sectors)]
if selected_industries:
    filtered_symbols_df = filtered_symbols_df[filtered_symbols_df['industry'].isin(selected_industries)]

# Display Filtered Symbols
if not filtered_symbols_df.empty:
    st.subheader("Filtered Symbols Data")
    st.dataframe(filtered_symbols_df)
else:
    st.info("No symbol data matches the selected filters.")

# Sector Insights
st.subheader("Sector Insights")
sector_counts = symbols_df['sector'].value_counts().reset_index()
sector_counts.columns = ['Sector', 'Count']
st.bar_chart(sector_counts.set_index('Sector'))

# Industry Insights
st.subheader("Industry Insights")
if not filtered_symbols_df.empty:
    industry_counts = filtered_symbols_df['industry'].value_counts().reset_index()
else:
    industry_counts = symbols_df['industry'].value_counts().reset_index()
industry_counts.columns = ['Industry', 'Count']
st.bar_chart(industry_counts.set_index('Industry'))

# ----------------------------------------------------------
# CPI Dashboard
# ----------------------------------------------------------
st.header("📈 CPI Data")

# Filters for CPI
st.sidebar.subheader("CPI Filters")
selected_year = st.sidebar.selectbox("Select Year", sorted(cpi_df['year'].dropna().unique()))
selected_month = st.sidebar.selectbox("Select Month", sorted(cpi_df['month'].dropna().unique()))

filtered_cpi_df = cpi_df.copy()
if selected_year:
    filtered_cpi_df = filtered_cpi_df[filtered_cpi_df['year'] == selected_year]
if selected_month:
    filtered_cpi_df = filtered_cpi_df[filtered_cpi_df['month'] == selected_month]

# Display Raw CPI Data
st.subheader(f"CPI Data for {selected_year} - Month {selected_month}")
if not filtered_cpi_df.empty:
    st.dataframe(filtered_cpi_df)
else:
    st.info("No CPI data matches the selected filters.")

# CPI Line Chart
st.subheader("CPI Trend Over Time")
st.line_chart(cpi_df.set_index('date')['cpi_value'])

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, FastAPI, and Azure")

