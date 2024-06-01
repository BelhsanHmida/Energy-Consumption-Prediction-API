"""
conftest.py

This module defines pytest fixtures used across the test suite.

Fixtures:
- client: Provides a test client for the Flask app.
"""

import os
import sys

sys.path.insert(0,os.path.abspath(
        os.path.join(os.path.dirname(__file__),'../src')) )# Add the project root directory to the Python path

from app import app  # Ensure this imports your Flask app correctly
import pytest


@pytest.fixture
def client():
    """
    Fixture to provide a test client for the Flask app.

    Yields:
        FlaskClient: A Flask test client instance.
    """
    with app.test_client() as client:
        yield client
