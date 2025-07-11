# Backend (FastAPI)

This directory contains the backend application built with FastAPI.

## Overview

- **Framework**: FastAPI
- **Language**: Python (version 3.12 recommended)
- **Database**: PostgreSQL (version 17 recommended)
- **Authentication**: JWT (JSON Web Tokens)

## Project Structure

```
backend/
├── app/
│   ├── config/           # Configuration settings (from .env)
│   ├── db/               # Database models and sessions
│   ├── logs/             # Log files
│   ├── routes/           # API routes and endpoints
│   ├── schemas/          # Pydantic schemas (data validation)
│   ├── services/         # Business logic services
│   ├── utils/            # Utility functions and constants
│   └── main.py           # FastAPI application instance and main router
├── alembic/              # Alembic migrations (if using Alembic)
├── tests/                # Unit and integration tests
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore file
├── alembic.ini           # Alembic configuration (if used)
├── Dockerfile            # Dockerfile for containerization
├── pyproject.toml        # pyproject.toml for Poetry
├── README.md             # This file
└── requirements.txt      # Project dependencies
```

## Getting Started

### Prerequisites

- Python (version 3.12 recommended)
- Pip (Python package installer)
- A running PostgreSQL instance (version 17 recommended)

### Installation & Setup

1.  **Navigate to the `backend` directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables:**
    Create a `.env` file in the `backend` directory by copying `.env.example` (if one exists) or by creating it manually. This file will store sensitive configuration and should not be committed to version control if it contains real secrets.

    Key environment variables:

    - `DATABASE_URL`: The connection string for your PostgreSQL database (e.g., `postgresql://user:password@host:port/dbname`).
    - `SECRET_KEY`: A strong, unique secret key used for signing JWTs and other security purposes. Generate one using `openssl rand -hex 32`.
    - `ALGORITHM`: The algorithm used for JWTs (e.g., `HS256`).
    - `ACCESS_TOKEN_EXPIRE_MINUTES`: Expiration time for access tokens.
    - `CORS_ORIGINS`: Comma-separated list of allowed CORS origins (e.g., `http://localhost:5173,https://yourdomain.com`).

    Example `.env`:
    ```env
    DATABASE_URL="postgresql://postgres:changethis@localhost:5432/appdb"
    SECRET_KEY="your_very_strong_secret_key_here"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    CORS_ORIGINS="http://localhost:5173,http://127.0.0.1:5173"
    ```

5.  **Database Migrations (with Alembic):**
    This project uses Alembic to manage database schema migrations. Ensure your `alembic.ini` is configured and your `migrations/env.py` correctly points to your SQLAlchemy models' metadata.

    Common commands (run from the `backend` directory):

    -   **Generate a new migration script (after model changes):**
        ```bash
        alembic revision -m "your_descriptive_migration_message" --autogenerate
        ```
        *(Always review autogenerated scripts carefully.)*
    -   **Apply all pending migrations to the database:**
        ```bash
        alembic upgrade head
        ```
    -   **View migration history:**
        ```bash
        alembic history
        ```

    For a comprehensive guide on using Alembic, including setup, writing migrations, and best practices, please refer to the [Database Migrations with Alembic](../../docs/backend/alembic-migrations.md) documentation.

### Running the Development Server

## Key FastAPI Concepts

This project leverages several powerful features of FastAPI:

*   **Pydantic Models:** Used for data validation, serialization, and settings management (see `app/schemas/`).
*   **APIRouter:** For structuring your application into multiple, manageable modules (see `app/api/v1/endpoints/` and `app/api/api.py`).
*   **Dependency Injection:** Extensively used for database sessions, authentication, and other shared logic (see `app/api/v1/deps.py`).
*   **Automatic API Docs:** Interactive Swagger UI available at `/docs` and ReDoc at `/redoc` when the development server is running.

For a detailed guide on FastAPI usage within this project, including creating endpoints, working with Pydantic, and authentication, refer to the [FastAPI Guide for Backend Development](../../docs/backend/fastapi-guide.md).


Once dependencies are installed and the `.env` file is configured, you can run the FastAPI development server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- `--reload`: Enables auto-reloading when code changes.
- The API will be accessible at `http://localhost:8000`.
- Interactive API documentation (Swagger UI) will be at `http://localhost:8000/docs`.
- Alternative API documentation (ReDoc) will be at `http://localhost:8000/redoc`.

## API Structure

- API endpoints are defined in `app/api/v1/endpoints/`.
- Pydantic schemas for request/response validation are in `app/schemas/`.
- Database models (SQLAlchemy) are in `app/db/models/`.
- Business logic and CRUD operations are typically in `app/crud/` or `app/services/`.

## Testing

*(Describe how to run tests, e.g., `pytest`)*

```bash
# Example: pytest
pytest
```

## Further Information

**Project-Specific Guides:**

- [FastAPI Guide for Backend Development](../../docs/backend/fastapi-guide.md)
- [Database Migrations with Alembic](../../docs/backend/alembic-migrations.md)

**Official Documentation:**

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
