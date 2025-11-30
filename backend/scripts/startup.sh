#!/bin/bash

echo "Running in NORMAL mode"

# Run migrations first
./scripts/migrate.sh

# Seed the development environment
python ./dev/seed_data.py

# Start the FastAPI application with configurable port
echo "Starting FastAPI application..."
uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000} --reload
