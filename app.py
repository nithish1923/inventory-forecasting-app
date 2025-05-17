# Streamlit app integrating forecasting and optimization UI

import streamlit as st
import preprocess
import forecast
import optimize  # or inventory_optimize if renamed

st.title("📦 Inventory Demand Forecasting App")

uploaded_file = st.file_uploader("Upload your sales data (CSV or Excel)", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Step 1: Preprocessing
        preprocessed_df = preprocess.preprocess_data(uploaded_file)
        st.subheader("✅ Preprocessed Data")
        st.dataframe(preprocessed_df.head())

        # Step 2: Forecasting
        forecast_df = forecast.forecast_demand(preprocessed_df)
        st.subheader("📈 Forecasted Demand")
        st.line_chart(forecast_df.set_index("ds")["yhat"])

        # Step 3: Inventory Optimization
        optimized_inventory = optimize.optimize_inventory(forecast_df)
        st.subheader("📦 Optimized Inventory")
        st.dataframe(optimized_inventory)

    except Exception as e:
        st.error(f"❌ Error: {e}")

else:
    st.info("Please upload a CSV or Excel file to begin.")
