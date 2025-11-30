#!/bin/bash

echo "Running in DEBUG mode"

# Run migrations first
./scripts/migrate.sh

# Seed the development environment
python ./dev/seed_data.py

# Start the FastAPI application in debug mode
echo "Starting FastAPI application in debug mode..."
python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
