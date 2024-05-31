"""
test_app.py

This module contains test cases for the Energy Consumption Prediction API.

Test Cases:
- test_index: Tests the index route (/) of the API.
- test_predict_valid_date: Tests the /predict route with a valid date.
- test_predict_invalid_date_format: Tests the /predict route with various invalid date formats.
- test_predict_missing_date: Tests the /predict route with a missing date parameter.
- test_predict_past_date: Tests the /predict route with a past date.

Modules Required:
- pytest
- src.app: Imports the Flask app for testing.
"""

import pytest
from app import app

@pytest.fixture
def client():
    """
    Fixture to provide a test client for the Flask app.

    Yields:
        FlaskClient: A Flask test client instance.
    """
    with app.test_client() as client:
        yield client

def test_index(client):
    """
    Test the index route (/) of the API.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Energy Consumption Prediction API!" in response.data

def test_predict_valid_date(client):
    """
    Test the /predict route with a valid date.
    """
    response = client.get('/predict?date=2024-05-31T12:00:00')
    assert response.status_code == 200
    assert 'prediction' in response.json

def test_predict_invalid_date_format(client):
    """
    Test the /predict route with various invalid date formats.
    """
    invalid_dates = [
        '2023-05-31', 
        '2023-31-05T12:00:00', 
        '31-05-2023T12:00:00', 
        '20230531T120000', 
        '2023-05-31T12:00', 
        '2023-05-31 12:00:00', 
        'invalid-date',
        '12345',
        'Today'
    ]
    for date in invalid_dates:
        response = client.get(f'/predict?date={date}')
        assert response.status_code == 400
        assert 'error' in response.json

def test_predict_missing_date(client):
    """
    Test the /predict route with a missing date parameter.
    """
    response = client.get('/predict')
    assert response.status_code == 400
    assert 'error' in response.json

def test_predict_past_date(client):
    """
    Test the /predict route with a past date.
    """
    response = client.get('/predict?date=2000-01-01T00:00:00')
    assert response.status_code == 400
    assert 'error' in response.json
