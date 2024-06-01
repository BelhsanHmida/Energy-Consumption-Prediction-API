# Energy Consumption Prediction API

Welcome to the Energy Consumption Prediction API, an open-source project designed to predict energy consumption based on a given date. This project uses a pre-trained XGBoost model and provides a simple HTTP API for making predictions.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Improvements](#improvements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides an API for predicting energy consumption using a pre-trained XGBoost model. The API accepts a date in the format `YYYY-MM-DDTHH:MM:SS` and returns a prediction of energy consumption for that date and time.

## Directory Structure


```plaintext
energy-consumption-prediction-api/
  ├── app.py
  ├── data_ingestion.py
  ├── models/
  │   └── xgboost_energy_model.pkl
  ├── tests/
  │   └── test_app.py
  ├── utils.py
  ├── improvements/
  │   └── README.md
  ├── requirements.txt
  ├── README.md
  └── CONTRIBUTING.md
```
  



## Installation

### Prerequisites

- Python 3.9 or higher
- Flask
- Pandas
- XGBoost
- Flask-Marshmallow

### Setup

#### Unix Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/energy-consumption-prediction-api.git
    cd energy-consumption-prediction-api
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Make sure the pre-trained model is available in the `models` directory:**
    ```bash
    mkdir -p models
    # Place your xgboost_energy_model.pkl in the models directory
    ```

5. **Run the Flask application:**
    ```bash
    python app.py
    ```

## Usage

To use the API, send a GET request to the `/predict` endpoint with a `date` parameter in the correct format.

Example:
```bash
curl "http://127.0.0.1:5000/predict?date=2024-05-31T12:00:00"
