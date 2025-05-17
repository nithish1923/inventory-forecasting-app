# Streamlit app integrating forecasting and optimization UI

import streamlit as st

st.title("Inventory Forecasting App")

st.write("Upload your sales and inventory data to begin.")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file:
    st.success("File uploaded successfully!")
    # TODO: Add data preview, forecast, optimize logic
