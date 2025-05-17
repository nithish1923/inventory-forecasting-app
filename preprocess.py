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
    # Reset file pointer to start
    uploaded_file.seek(0)
    
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
        df = pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload CSV or Excel file.")

    df.columns = [col.lower().strip() for col in df.columns]

    if 'date' not in df.columns:
        raise ValueError("Input data must contain a 'date' column.")
    if 'units_sold' not in df.columns:
        raise ValueError("Input data must contain a 'units_sold' column.")

    df['ds'] = pd.to_datetime(df['date'])
    df['y'] = df['units_sold']

    return df[['ds', 'y']]
