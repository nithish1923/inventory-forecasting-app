# Code to clean and preprocess the data

import pandas as pd

def preprocess_data(uploaded_file):
    """
    Preprocess uploaded sales data for forecasting.
    
    Parameters:
    uploaded_file : Uploaded file object (CSV or Excel)
    
    Returns:
    pd.DataFrame : DataFrame with columns 'ds' (datetime) and 'y' (numeric sales)
    """
    # Read CSV or Excel file based on extension
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
        df = pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload CSV or Excel file.")

    # Normalize column names: lower case and strip whitespace
    df.columns = [col.lower().strip() for col in df.columns]

    # Check required columns
    if 'date' not in df.columns:
        raise ValueError("Input data must contain a 'date' column.")
    if 'units_sold' not in df.columns:
        raise ValueError("Input data must contain a 'units_sold' column.")

    # Convert date column to datetime
    df['ds'] = pd.to_datetime(df['date'])

    # Rename sales column to 'y' (target variable for forecasting)
    df['y'] = df['units_sold']

    # Return only columns needed for forecasting
    return df[['ds', 'y']]
