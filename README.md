# IndicGlyph AI & OCR Platform (Powered by Taapset Technologies)

This repository hosts the IndicGlyph AI & OCR platform, powered by Taapset Technologies. Cluster 1 lays down the foundation services, tooling, and deployment pipeline.

## Repository Structure

- `backend/` – FastAPI service with PostgreSQL, Alembic migrations, and S3 access helpers.
- `frontend/` – React + Tailwind web application scaffolded with Vite.
- `infra/` – Shared infrastructure assets (Nginx reverse proxy, TLS cert placeholders).
- `.github/workflows/` – Continuous integration pipeline definition.
- `qa/` – Manual QA execution reports and checklists.

## Getting Started

1. Copy `.env.example` to `.env` and adjust values as needed.
2. Start the full stack:

   ```bash
   docker compose up --build
   ```

3. Access services:

   - Backend API: <http://localhost:8000/docs>
   - Frontend UI: <https://localhost>
   - MinIO Console: <http://localhost:9001>

## Developer Tooling

- Backend: `uv` for environment management, `pytest`, and `ruff`.
- Frontend: Vite dev server with ESLint.
- CI: GitHub Actions pipeline running linting, tests, and Docker builds.

## Next Steps

- Flesh out Cluster 2 features (upload & slicing).
- Implement detailed reviewer workflows and gamification.
- Harden security and add production observability tooling.
