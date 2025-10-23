# Cluster 1 QA Log
_Date: 2025-10-23_

## Checklist Outcomes

1. **Containers build and deploy**
   - Command: `docker compose build backend`
   - Result: Blocked because the local environment does not provide a Docker CLI (`CommandNotFoundException`). Static Dockerfiles reviewed; full validation pending on a host with Docker.

2. **CI tests run on PR**
   - Backend:
     - `& .venv\Scripts\python.exe -m pip install -e "./backend[dev]"`
     - `& .venv\Scripts\python.exe -m ruff check backend`
     - `& .venv\Scripts\python.exe -m pytest`
   - Frontend:
     - `npm install`
     - `npm run lint`
     - `npm run build`
   - Result: All commands completed successfully; lint and unit tests pass for backend and frontend.

3. **DB migrations apply cleanly**
   - Command: `& ..\.venv\Scripts\python.exe -m alembic upgrade head --sql`
   - Result: Generated upgrade SQL without error, confirming migration scripts are syntactically valid. A live PostgreSQL instance is still required for a full online migration run.

4. **.env loads per env**
   - Verification: `.env.example` audited; `backend/app/config.py` uses `pydantic-settings` with `.env` defaults.
   - Result: Confirmed.

5. **HTTPS enforced in staging/prod**
   - Verification: `infra/nginx/default.conf` proxies only over TLS with cert mounts.
   - Result: Confirmed.

## Follow-ups

- Execute `docker compose build` and `docker compose up` on a machine with Docker installed to close out the remaining open QA item.
- Re-run `docker compose up --build` once Docker Desktop can pull `nginx:1.25-alpine`; current attempt on 2025-10-23 failed with `unexpected end of JSON input` while fetching the image, likely due to a registry/network hiccup.
