# Streamlit app integrating forecasting and optimization UI

import streamlit as st
import preprocess
import forecast
import optimize

optimized_inventory = optimize.optimize_inventory(forecast_df)


st.title("📊 Inventory Demand Forecasting App")

uploaded_file = st.file_uploader("Upload your sales data (CSV or Excel)", type=['csv', 'xlsx', 'xls'])

if uploaded_file is not None:
    try:
        preprocessed_df = preprocess.preprocess_data(uploaded_file)
        st.write("### Preprocessed Data Preview:")
        st.dataframe(preprocessed_df.head())

        forecast_df = forecast.forecast_demand(preprocessed_df)
        st.write("### Forecasted Demand:")
        st.line_chart(forecast_df.set_index('ds')['yhat'])

        optimized_inventory = optimize.optimize_inventory(forecast_df)
        st.write("### Optimized Inventory Levels:")
        st.dataframe(optimized_inventory)

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please upload a CSV or Excel file to get started.")
