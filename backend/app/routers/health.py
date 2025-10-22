"""Healthcheck endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/healthz", summary="Liveness probe")
async def healthcheck() -> dict[str, str]:
    """Return a simple success payload for liveness checks."""

    return {"status": "ok"}
