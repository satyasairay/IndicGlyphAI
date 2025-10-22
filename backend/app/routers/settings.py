"""Admin configuration endpoints placeholder."""

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter(prefix="/settings")


@router.get("", summary="Fetch runtime configuration snapshot")
async def read_settings(settings: Settings = Depends(get_settings)) -> dict[str, object]:
    """
    Provide a sanitized view of environment configuration.

    Cluster 0 relies on admin-managed configuration. The endpoint returns
    selected values that are safe for clients.
    """

    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "cors_origins": settings.cors_origins,
        "version": settings.version,
        "s3_bucket": settings.s3_bucket,
        "s3_endpoint_url": settings.s3_endpoint_url,
    }
