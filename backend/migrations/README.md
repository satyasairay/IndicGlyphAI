# Alembic Migrations

This directory stores database migration scripts managed by Alembic.

To create a migration:

```bash
alembic revision --autogenerate -m "describe change"
```

To apply migrations locally:

```bash
alembic upgrade head
```

The Docker entrypoint runs migrations automatically on start so that container
deployments stay in sync with the schema.
