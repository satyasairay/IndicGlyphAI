"""FastAPI application entrypoint."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.db import init_database
from app.routers import health, settings as settings_router


def create_application() -> FastAPI:
    settings = get_settings()

    app = FastAPI(title=settings.app_name, version=settings.version, debug=settings.debug)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router, tags=["health"])
    app.include_router(settings_router.router, prefix="/api", tags=["settings"])

    return app


app = create_application()


@app.on_event("startup")
async def on_startup() -> None:
    """Perform bootstrap checks."""

    logger = logging.getLogger("uvicorn")
    try:
        await init_database()
        logger.info("Database connection check succeeded")
    except Exception as exc:  # pragma: no cover - startup log path
        logger.error("Database connection check failed: %s", exc)
        raise
