# List available commands
default:
    @just --list

# Start the application in normal mode
start:
    docker compose --env-file .env.dev -p dev up -d --detach

# Start the application in debug mode
debug:
    docker compose --env-file .env -p dev up -d --detach


# Stop all containers
stop:
    docker compose -p dev down

# Start the E2E environment
e2e-start:
    docker compose -f docker-compose.e2e.yml --env-file .env.e2e -p e2e up -d --detach

# Stop the E2E environment
e2e-stop:
    docker compose -f docker-compose.e2e.yml -p e2e down
# Run e2e tests with UI mode
e2e: 
    just e2e-start
    npx playwright test

# Run e2e tests with UI mode
e2e-ui:
    just e2e-start
    npx playwright test --ui

