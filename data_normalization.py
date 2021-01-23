from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def normalizing(daily_cases_values):
    """function to normalize the data"""
    scaler = MinMaxScaler()
    cases_scaled = scaler.fit_transform(daily_cases_values)
    daily_cases_norm = pd.DataFrame(cases_scaled)
    return daily_cases_norm
