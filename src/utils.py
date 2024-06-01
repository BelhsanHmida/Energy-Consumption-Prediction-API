import pandas as pd

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


