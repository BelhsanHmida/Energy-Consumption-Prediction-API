"""
Unit tests for the Energy Consumption Prediction API.

These tests use pytest to validate the behavior of the API endpoints:
- /: Tests the index route.
- /predict: Tests the predict route with various date inputs.

Tests:
- test_index: Checks if the index route returns a 200 status code and the correct welcome message.
- test_predict_valid_date: Tests the predict route with a valid date.
- test_predict_invalid_date_format: Tests the predict route with various invalid date formats.
- test_predict_missing_date: Tests the predict route with a missing date parameter.
- test_predict_past_date: Tests the predict route with a past date.
- test_predict_valid_date_edge_case: Tests the predict route with the edge case of the earliest valid date.

Usage:
    To run these tests, use pytest:

    $ pytest test_app.py

Requirements:
    - pytest
    - Flask (included in the project dependencies)
"""
import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Energy Consumption Prediction API!" in response.data


def test_predict_valid_date(client):
    """Test the predict route with a valid date"""
    response = client.get('/predict?date=2023-07-31T12:00:00')
    assert response.status_code == 200
    assert 'prediction' in response.json


def test_predict_invalid_date_format(client):
    """Test the predict route with various invalid date formats"""
    invalid_dates = [
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
        if response.status_code == 200:
            print(
                f"Date '{date}' incorrectly parsed as valid. Response: {response.json}")
        else:
            print(
                f"Date '{date}' correctly parsed as invalid. Status code: {response.status_code}")
        assert response.status_code == 400
        assert 'error' in response.json


def test_predict_missing_date(client):
    """Test the predict route with a missing date parameter"""
    response = client.get('/predict')
    assert response.status_code == 400
    assert 'error' in response.json


def test_predict_past_date(client):
    """Test the predict route with a past date"""
    response = client.get('/predict?date=2000-01-01T00:00:00')
    assert response.status_code == 400
    assert 'error' in response.json
    assert 'invalid_date' in response.json


def test_predict_valid_date_edge_case(client):
    """Test the predict route with the edge case of the earliest valid date"""
    response = client.get('/predict?date=2015-12-29T00:00:00')
    assert response.status_code == 200
    assert 'prediction' in response.json
