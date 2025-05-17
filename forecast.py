# Code to forecast demand using ML models
from prophet import Prophet

def forecast_demand(df):
    """
    Build a forecasting model using Prophet.
    Input df must have 'ds' and 'y' columns.

    Returns:
        DataFrame with forecast results including 'ds', 'yhat', 'yhat_lower', 'yhat_upper'.
    """
    model = Prophet()
    model.fit(df)

    # Forecast for next 30 days (you can adjust horizon)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    # Return relevant columns
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
