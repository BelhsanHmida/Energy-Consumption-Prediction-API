"""
app.py

This file defines a Flask API for predicting energy consumption based on a given date.

Endpoints:
- /predict: Predicts energy consumption based on the input date.
- /: Welcome route for the API.


"""

import pickle
import pandas as pd
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize Flask app and Marshmallow for input validation
app = Flask(__name__)
ma = Marshmallow(app)

# Load the pre-trained model from a file
with open(r'models/xgboost_energy_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the schema for input validation


class PredictionSchema(ma.Schema):
    class Meta:
        fields = ('date',)


prediction_schema = PredictionSchema()


@app.route('/predict', methods=['GET'])
def predict():
    """
    Prediction route to predict energy consumption based on the input date.
    """
    try:
        # Validate and parse input
        errors = prediction_schema.validate(request.args)
        if errors:
            return jsonify(errors), 400

        # Extract and validate the date from the request args
        date_str = request.args.get('date')
        if not date_str:
            return jsonify({'error': 'Missing date parameter.'}), 400

        try:
            date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            return jsonify(
                {'error': 'Invalid date format. Please use YYYY-MM-DDTHH:MM:SS format.'}), 400

        # Check if the date is within the valid range
        training_start_date = datetime.strptime('2015-12-29', '%Y-%m-%d')
        if date < training_start_date:
            return jsonify(
                {'error': f'Date must be on or after {training_start_date.strftime("%Y-%m-%d")}.', 'invalid_date': date_str}), 400

        # Extract features from the date
        hour = date.hour
        dayofweek = date.weekday()
        quarter = (date.month - 1) // 3 + 1  # Calculate the quarter
        month = date.month
        year = date.year
        dayofyear = date.timetuple().tm_yday
        dayofmonth = date.day
        weekofyear = date.isocalendar()[1]

        # Create a DataFrame with the input features
        input_df = pd.DataFrame({
            'date': [date],
            'hour': [hour],
            'dayofweek': [dayofweek],
            'quarter': [quarter],
            'month': [month],
            'year': [year],
            'dayofyear': [dayofyear],
            'dayofmonth': [dayofmonth],
            'weekofyear': [weekofyear]
        })

        input_df.set_index('date', inplace=True)

        # Make prediction using the pre-trained model
        y_pred = model.predict(input_df)

        # Format the response
        response = {
            'prediction': y_pred.tolist()
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/')
def index():
    """
    Welcome route for the Energy Consumption Prediction API.
    """
    return "Welcome to the Energy Consumption Prediction API!"


# Main block to start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
