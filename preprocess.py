# Code to clean and preprocess the data

import pandas as pd

def preprocess_data(uploaded_file):
    """
    Preprocess uploaded sales data for forecasting.
    Accepts CSV or Excel files.

    Returns:
        pd.DataFrame with columns 'ds' (datetime) and 'y' (sales units).
    """
    uploaded_file.seek(0)

    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
        df = pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload CSV or Excel file.")

    # Normalize column names
    df.columns = [col.lower().strip() for col in df.columns]

    # Check date column
    if 'date' not in df.columns:
        raise ValueError("Input data must contain a 'date' column.")

    # Check sales quantity column (try common alternatives)
    possible_sales_cols = ['units_sold', 'sales', 'quantity', 'sold_units']
    sales_col = None
    for col in possible_sales_cols:
        if col in df.columns:
            sales_col = col
            break
    if not sales_col:
        raise ValueError(f"Input data must contain one of the sales columns: {possible_sales_cols}")

    # Create required columns for forecasting
    df['ds'] = pd.to_datetime(df['date'])
    df['y'] = df[sales_col]

    return df[['ds', 'y']]
