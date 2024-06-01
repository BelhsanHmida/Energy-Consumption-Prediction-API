#!/bin/bash

# Ensure the script exits if any command fails
set -e

# Print each command before executing it
set -x

# Step 1: Update package list and install dependencies
echo "Updating package list and installing dependencies..."
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv

# Step 2: Set up a virtual environment
echo "Setting up virtual environment..."
python3 -m venv venv

# Step 3: Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Step 4: Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 5: Run the application
echo "Running the application..."
export FLASK_APP=app.py
flask run &

# Wait a few seconds for the Flask app to start
sleep 5

# Step 6: Run tests
echo "Running tests..."
pytest tests/

# Step 7: Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate
