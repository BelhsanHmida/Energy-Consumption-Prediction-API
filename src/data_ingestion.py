"""
This module contains functions for loading and preprocessing data for the energy consumption prediction model.

The primary functions provided in this module are `load_data` and `preprocess_data`.

Example usage:
    >>> from data_ingestion import load_data, preprocess_data
    >>> data = load_data('data/SF_hospital_load.csv')
    >>> data = preprocess_data(data)
"""

import os
import pandas as pd
from utils import download_file, create_features

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
    data = pd.read_csv(file_path, index_col=[0], parse_dates=[0])
    return data

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ourownstory/neuralprophet-data/main/datasets/energy/SF_hospital_load.csv"
    local_filename = "data/SF_hospital_load01.csv"

    # Create the data directory if it doesn't exist
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)

    # Download the file
    download_file(url, local_filename)

    print(f"File downloaded and saved to {local_filename}")
