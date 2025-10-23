"""Database session management utilities."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from .config import get_settings


def _create_engine() -> AsyncEngine:
    settings = get_settings()
    return create_async_engine(
        settings.database_url,
        echo=settings.debug,
        future=True,
        pool_pre_ping=True,
    )


engine: AsyncEngine = _create_engine()
SessionFactory = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def init_database() -> None:
    """
    Perform a lightweight connectivity check.

    Alembic migrations will manage schema changes; here we just ensure the
    configured database is reachable.
    """

    async with engine.connect() as connection:
        await connection.execute(text("SELECT 1"))


@asynccontextmanager
async def get_session() -> AsyncIterator[AsyncSession]:
    """Provide a request-scoped session for FastAPI dependencies."""

    session: AsyncSession = SessionFactory()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
