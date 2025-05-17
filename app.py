# Streamlit app integrating forecasting and optimization UI

import streamlit as st
import pandas as pd
from forecast import forecast_demand
from optimize import optimize_inventory
from preprocess import preprocess_data

st.set_page_config(page_title="Inventory Forecasting App", layout="wide")

st.title("📦 Inventory Forecasting & Optimization")
st.markdown("""
Upload your sales data to generate forecasts and optimize inventory levels.
""")

uploaded_file = st.file_uploader("📁 Upload sales data (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Preprocess
    st.subheader("🔍 Raw Data Preview")
    raw_df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
    st.dataframe(raw_df.head())

    # Forecast
    st.subheader("📈 Forecasted Demand")
    preprocessed_df = preprocess_data(uploaded_file)
    forecast_df = forecast_demand(preprocessed_df)
    st.line_chart(forecast_df.set_index("ds")["yhat"])
    st.dataframe(forecast_df.tail())

    # Optimization
    st.subheader("⚙️ Inventory Optimization")
    reorder_plan = optimize_inventory(forecast_df)
    st.dataframe(reorder_plan)

else:
    st.info("Please upload a sales file to get started.")

