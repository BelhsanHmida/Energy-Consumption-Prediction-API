name: CI

on:
  push:
    branches:
      - main
    paths:
      - 'src/**'         # Trigger on changes within the src directory
      - 'utils/**'       # Trigger on changes within the utils directory
      - 'tests/**'       # Trigger on changes within the tests directory
  pull_request:
    branches:
      - main
    paths:
      - 'src/**'         # Trigger on changes within the src directory
      - 'utils/**'       # Trigger on changes within the utils directory
      - 'tests/**'       # Trigger on changes within the tests directory

jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: debian:latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Install dependencies
        run: |
          apt-get update
          apt-get install -y python3 python3-pip python3-venv
        shell: bash

      - name: Set up virtual environment
        run: |
          python3 -m venv venv
          source venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        shell: bash

      - name: Run tests
        run: |
          source venv/bin/activate
          pytest --maxfail=5 --disable-warnings
        shell: bash
