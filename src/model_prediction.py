"""
This module contains functions for loading a trained model and making predictions.

The primary functions provided in this module are `load_model` and `predict`.
- `load_model` loads a model from a specified file path.
- `predict` generates future predictions using the loaded model.

Example usage:
    >>> from model_prediction import load_model, predict
    >>> model = load_model('models/energy_forecast_xgb_model.pkl')
    >>> forecast = predict(model, X_input)
"""

import pickle
import pandas as pd
from xgboost import XGBRegressor
from utils import create_features
from data_ingestion import load_data

def load_model(file_path: str) -> XGBRegressor:
    """
    Loads a trained model from a given file path.

    """
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict(model: XGBRegressor, X_input: pd.DataFrame) -> pd.DataFrame:
    """
    Generates predictions using the loaded model.

    Args:
        model (XGBRegressor): The trained model to use for making predictions.
        X_input (pd.DataFrame): The input features for making predictions.

    Returns:
        pd.DataFrame: The predicted values.

    Example:
        >>> forecast = predict(model, X_input)
    """
    predictions = model.predict(X_input)
    return pd.DataFrame(predictions, columns=['prediction'])

if __name__ == "__main__":
    # Example usage
    file_path = 'models/xgboost_energy_model01.pkl'
    model = load_model(file_path)

    # Load and preprocess the data
    data = load_data("data/SF_hospital_load.csv")
    
    # Create features and target variable
    X, y = create_features(data, label='y')
    
    # Predict the future periods (example: next 10 periods)
    X_input = X.tail(10)  # Replace this with appropriate feature creation for future periods
    forecast = predict(model, X_input)
    
    print(forecast)
