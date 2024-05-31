"""
This module contains functions for loading and preprocessing data.

The primary function provided in this module is `load_data`, which loads data from a given
CSV file path into a pandas DataFrame. Additional preprocessing steps can be added as needed.

Example usage:
    >>> from data_ingesting import load_data
    >>> df = load_data('data/SF_hospital_load.csv')
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads and preprocesses the dataset from a given file path.

    Args:
        file_path (str): The path to the CSV file containing the dataset.

    Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame.

    Example:
        >>> df = load_data('data/SF_hospital_load.csv')
    """
    data = pd.read_csv(file_path)

    # Add additional preprocessing steps here if needed
    # For example: data.dropna(inplace=True)

    return data


if __name__ == "__main__":
    # Example usage
    url = 'https://raw.githubusercontent.com/ourownstory/neuralprophet-data/main/datasets/energy/SF_hospital_load.csv'
    df = pd.read_csv(url)
    df.to_csv('data/SF_hospital_load.csv', index=False)
