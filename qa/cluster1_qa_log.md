# Cluster 1 QA Log
_Date: 2025-10-22_

## Checklist Outcomes

1. **Containers build and deploy**
   - Command: `docker compose build backend`
   - Result: ❌ `docker` CLI unavailable in the environment (`CommandNotFoundException`).
   - Follow-up: Requires Docker Desktop or compatible CLI on the host to validate container builds.

2. **CI tests run on PR**
   - Backend command: `& ..\.venv\Scripts\python.exe -m pip install -e .[dev]`
   - Result: ❌ Multiple attempts failed — pip could not download dependencies because of SSL `DECRYPTION_FAILED_OR_BAD_RECORD_MAC` errors.
   - Frontend command: `npm install`
   - Result: ⏳ Not executed; backend dependency installation blocked upstream testing workflow.
   - Follow-up: Retry in an environment with stable TLS egress or cached wheels.

3. **DB migrations apply cleanly**
   - Command: `alembic upgrade head` (intended via virtualenv above)
   - Result: ⚠️ Blocked by dependency installation failure.
   - Follow-up: Re-run once Python dependencies install successfully.

4. **.env loads per env**
   - Verification: `.env.example` created with all required keys; FastAPI `Settings` uses `pydantic-settings` to load `.env`.
   - Result: ✅ Configuration bootstrap validated via static inspection (`backend/app/config.py`).

5. **HTTPS enforced in staging/prod**
   - Verification: `infra/nginx/default.conf` terminates TLS on port 443 with certificates in `infra/certs`.
   - Result: ✅ Static configuration review confirms HTTPS-only reverse proxy.

## Notes

- Repeated SSL failures occurred while fetching packages from PyPI; logs preserved in the command history above.
- Suggest running QA pipeline on CI/GitHub Actions once network access is stable.
