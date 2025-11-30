# 🧭 Sample Text Application

Sample Text Application is a full-stack application composed of a **Python backend** (managed with Poetry) and a **TypeScript frontend** (using npm and Vite).  
It provides an integrated environment for AI-driven exploration and analysis, supported by robust local development tooling.

---

## ⚙️ Prerequisites

Before starting, make sure you have the following installed:

- **Python 3.10+**
- **[Poetry](https://python-poetry.org/docs/#installation)**
- **Node.js 20+** and **npm**
- **Docker** and **Docker Compose**
- **[Just](https://github.com/casey/just)**

---

## 🚀 Installation

### 🐍 Backend setup

```bash
cd backend
poetry install
```

This installs all backend dependencies, including formatters and linters such as Black and Pylint.

### 🧩 Frontend setup

```
cd ../frontend
npm install
```

Make sure your `package.json` includes the following scripts (these should already exist):

## 🪄 Pre-commit Hooks

This project uses pre-commit to automatically lint and format code before each commit.

### 📦 Installation

From the project root (where .pre-commit-config.yaml is located):

```
poetry run pre-commit install
```

This installs a Git hook that will automatically:

- Format Python code with Black
- Lint Python code with Pylint
- Lint TypeScript with ESLint
- Check code formatting with Prettier

### 🧪 Run Hooks Manually

To run all pre-commit checks across the entire project:

```
poetry run pre-commit run --all-files
```

Expected behavior:

- 🐍 Backend Python files are formatted and linted
- 🧩 Frontend TypeScript files are linted and checked for formatting

## 🐳 Local Development with Docker Compose

You can run the full stack locally using Docker Compose.

Make sure Docker is running, then execute:

```
docker compose up --build
```

This starts the following services:

| Service     | Purpose                   | URL/Port              |
| ----------- | ------------------------- | --------------------- |
| ⚙️ Traefik  | Reverse proxy + dashboard | http://localhost:8080 |
| 🖼️ Frontend | React/Vite dev server     | http://localhost      |
| 🤖 Backend  | FastAPI service           | http://localhost/api  |
| 📀 Database | Postgres DB               | http://localhost:5432 |
