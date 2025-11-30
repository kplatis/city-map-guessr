#!/bin/bash

# Wait until the database is ready to accept connections
echo "Waiting for Postgres to be ready..."
until pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER; do
  echo "Postgres is not ready yet. Waiting..."
  sleep 2
done

echo "Postgres is ready. Running migrations..."

# Run the Alembic migrations
alembic upgrade head

echo "Migrations applied successfully."
