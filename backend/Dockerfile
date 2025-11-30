# WARNING: This is a Dockerfile used for development purposes
# In case of productionizing, a different Dockerfile should be written

FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry==1.8.5 uvicorn

RUN apt-get update && \
    apt-get install -y postgresql-client

ENV POETRY_VIRTUALENVS_CREATE=false

# Copy only the poetry files first for caching dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Install debugpy
RUN pip install debugpy

# Copy the rest of the application
COPY ./api ./api

COPY ./alembic ./alembic

COPY alembic.ini .

# Copy the scripts
COPY ./scripts /app/scripts

# Copy the development data
COPY ./dev /app/dev

# Make the scripts executable
RUN chmod +x /app/scripts/migrate.sh /app/scripts/startup-dev.sh /app/scripts/startup.sh

# Expose backend port
EXPOSE 8000

ENV PYTHONPATH="${PYTHONPATH}:/app/api"