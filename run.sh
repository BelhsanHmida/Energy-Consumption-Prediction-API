#!/bin/bash

# Step 1: Activate the Python Virtual Environment
source env/bin/activate

# Step 2: Install Testing Dependencies
pip install -r requirements.txt

# Step 3: Run Tests
pytest

# Step 4: Deactivate the Virtual Environment
deactivate