# CPI Dashboard Data System

A comprehensive data pipeline and visualization system that combines Consumer Price Index (CPI) data with stock market information, providing insights through an interactive dashboard.

## 🌟 Features

- Fetches CPI data from AlphaVantage API
- Processes and transforms time-series data
- Interactive dashboard built with Streamlit
- Azure Blob Storage integration for data persistence
- FastAPI backend for data serving
- Docker support for containerization

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Data Processing**: Pandas
- **Cloud Storage**: Azure Blob Storage
- **API Integration**: AlphaVantage
- **Containerization**: Docker

## 📋 Prerequisites

- Python 3.8+
- Azure Account with Blob Storage
- AlphaVantage API Key

## 📊 Project Structure

- `main.py` - FastAPI application entry point
- `run.py` - Streamlit dashboard configuration
- `blob_quickstart1.py` - Azure Blob Storage integration
- `extract_api.py` - AlphaVantage API data extraction
- `cpi_vs_ticker_chart/` - Dashboard application directory
  - `app.py` - Streamlit dashboard
  - `dockerfile` - Container configuration
