"""
This module contains functions for loading a trained model and making predictions.

The primary functions provided in this module are `load_model` and `predict`.
- `load_model` loads a model from a specified file path.
- `predict` generates future predictions using the loaded model.

Example usage:
    >>> from model_prediction import load_model, predict
    >>> model = load_model('models/energy_forecast_model.pkl')
    >>> forecast = predict(model, periods=10)
"""

import pickle
from prophet import Prophet
import pandas as pd


def load_model(file_path: str) -> Prophet:
    """
    Loads a trained model from a given file path.

    Args:
        file_path (str): The path to the file containing the saved model.

    Returns:
        Prophet: The loaded model.

    Example:
        >>> model = load_model('models/energy_forecast_model.pkl')
    """
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model


def predict(model: Prophet, periods: int) -> pd.DataFrame:
    """
    Generates future predictions using the loaded model.

    Args:
        model (Prophet): The trained model to use for making predictions.
        periods (int): The number of periods (e.g., hours, days) to forecast.

    Returns:
        pd.DataFrame: The forecasted data as a pandas DataFrame.

    Example:
        >>> forecast = predict(model, periods=10)
    """
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast


if __name__ == "__main__":
    # Example usage
    file_path = 'models/energy_forecast_model.pkl'
    model = load_model(file_path)
    forecast = predict(model, periods=10)
    print(forecast.head())
