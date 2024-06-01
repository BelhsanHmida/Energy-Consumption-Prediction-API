"""
data_ingestion.py

This module contains functions for loading, preprocessing, and feature engineering for the energy consumption prediction model.

The primary functions provided in this module are `load_data`, `preprocess_data`, `create_features`, and `download_file`.
- `load_data` loads data from a specified CSV file.
- `preprocess_data` preprocesses the loaded data.
- `create_features` creates time series features from the datetime index.
- `download_file` downloads a file from a given URL and saves it locally.

Example usage:
    >>> from data_ingestion import load_data, preprocess_data, create_features, download_file
    >>> data = load_data('data/SF_hospital_load.csv')
    >>> data = preprocess_data(data)
    >>> X, y = create_features(data, label='load')
    >>> download_file(url, 'data/SF_hospital_load.csv')
"""

import os
import requests
import pandas as pd

def download_file(url: str, local_filename: str):
    """
    Downloads a file from the given URL and saves it locally.

    Args:
        url (str): The URL of the file to download.
        local_filename (str): The local path where the file will be saved.
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from a specified CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data.
    
    Example:
        >>> data = load_data('data/SF_hospital_load.csv')
    """
    data = pd.read_csv(file_path, parse_dates=['timestamp'], index_col='timestamp')
    return data

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the loaded data.

    Args:
        data (pd.DataFrame): The raw data.

    Returns:
        pd.DataFrame: The preprocessed data.
    
    Example:
        >>> data = preprocess_data(data)
    """
    # Example preprocessing steps
    data = data.fillna(method='ffill')
    data = data.dropna()
    return data

def create_features(df: pd.DataFrame, label: str = None) -> pd.DataFrame:
    """
    Creates time series features from datetime index.

    Parameters:
    - df (pd.DataFrame): The input dataframe with datetime index.
    - label (str): The name of the target variable column (optional).

    Returns:
    - X (pd.DataFrame): DataFrame containing the time series features.
    - y (pd.Series): Series containing the target variable if label is provided.
    """
    df['date'] = df.index
    df['hour'] = df['date'].dt.hour
    df['dayofweek'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.isocalendar().week

    X = df[['hour', 'dayofweek', 'quarter', 'month', 'year',
            'dayofyear', 'dayofmonth', 'weekofyear']]
    
    if label:
        y = df[label]
        return X, y
    
    return X

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ourownstory/neuralprophet-data/main/datasets/energy/SF_hospital_load.csv"
    local_filename = "data/SF_hospital_load.csv"

    # Create the data directory if it doesn't exist
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)

    # Download the file
    download_file(url, local_filename)

    print(f"File downloaded and saved to {local_filename}")
