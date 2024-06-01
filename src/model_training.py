"""
model_training.py

This module contains functions for training an XGBoost forecasting model and saving it to a file.

The primary functions provided in this module are `train_xgb_model` and `save_xgb_model`.
- `train_xgb_model` trains an XGBoost model on the provided data.
- `save_xgb_model` saves the trained model to a specified file path.

Example usage:
    >>> from model_training import train_xgb_model, save_xgb_model
    >>> from data_ingestion import load_data, preprocess_data
    >>> from utils import create_features
    >>> data = load_data('data/SF_hospital_load.csv')
    >>> data = preprocess_data(data)
    >>> X, y = create_features(data, label='load')
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    >>> model = train_xgb_model(X_train, y_train, X_test, y_test, feature_names=['hour', 'dayofweek'])
    >>> save_xgb_model(model, 'models/energy_forecast_xgb_model.pkl')
"""

import pickle
import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from utils import create_features
from data_ingestion import load_data, preprocess_data

def train_xgb_model(X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame,
                    y_test: pd.Series, feature_names: list) -> xgb.XGBRegressor:
    """
    Trains an XGBoost model on the provided data.

    Parameters:
    - X_train (pd.DataFrame): Training data features.
    - y_train (pd.Series): Training data target variable.
    - X_test (pd.DataFrame): Validation data features.
    - y_test (pd.Series): Validation data target variable.
    - feature_names (list): List of feature names to use for training.

    Returns:
    - xgb.XGBRegressor: The trained XGBoost model.

    Example:
    >>> X_train, y_train, X_test, y_test = create_features(train_data, val_data, label='y')
    >>> model = train_xgb_model(X_train, y_train, X_test, y_test, feature_names=['hour', 'dayofweek'])
    """
    X_train = X_train[feature_names]
    X_test = X_test[feature_names]

    model = xgb.XGBRegressor(n_estimators=1000)
    model.fit(X_train, y_train,
              eval_set=[(X_train, y_train), (X_test, y_test)],
              early_stopping_rounds=50,
              verbose=False)

    return model


def save_xgb_model(model: xgb.XGBRegressor, file_path: str) -> None:
    """
    Saves the trained XGBoost model to a specified file path.

    Parameters:
    - model (xgb.XGBRegressor): The trained XGBoost model to save.
    - file_path (str): The path to the file where the model will be saved.

    Example:
    >>> save_xgb_model(model, 'models/energy_forecast_xgb_model.pkl')
    """
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    # Load and preprocess the data
    data = load_data("data/SF_hospital_load.csv")
    data = preprocess_data(data)

    # Create features and target variable
    X, y = create_features(data, label='load')

    # Split the data into training and validation sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train the XGBoost model
    model = train_xgb_model(X_train, y_train, X_test, y_test, feature_names=['hour', 'dayofweek'])

    # Save the model
    save_xgb_model(model, 'models/xgboost_energy_model.pkl')

    print("Model training and saving completed successfully.")
