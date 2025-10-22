# DatasetForge Backend

FastAPI application that powers the DatasetForge OCR and annotation platform.

## Local Development

```bash
uv venv
uv pip install -e ".[dev]"
uv run uvicorn app.main:app --reload
```

Create a `.env` file based on `.env.example`. The default Docker Compose stack
provides PostgreSQL and MinIO services.

## Testing

```bash
uv run pytest
```

## Migrations

```bash
uv run alembic revision --autogenerate -m "describe change"
uv run alembic upgrade head
```
