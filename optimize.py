# Code to optimize inventory based on forecast

def optimize_inventory(forecast_df, safety_stock=10):
    optimized = forecast_df[['ds', 'yhat']].copy()
    optimized['optimized_inventory'] = optimized['yhat'].apply(lambda x: max(0, round(x + safety_stock)))
    return optimized[['ds', 'optimized_inventory']]
