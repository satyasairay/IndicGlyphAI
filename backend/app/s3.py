"""S3/MinIO connectivity utilities."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

import aioboto3

from .config import get_settings


@asynccontextmanager
async def get_s3_client() -> AsyncIterator[Any]:
    """
    Yield an aioboto3 client using configuration from settings.

    The helper centralises connection handling so that other modules can focus
    on business logic without duplicating setup code.
    """

    settings = get_settings()

    session = aioboto3.Session()
    client = await session.client(
        service_name="s3",
        endpoint_url=settings.s3_endpoint_url,
        region_name=settings.s3_region,
        aws_access_key_id=settings.s3_access_key,
        aws_secret_access_key=settings.s3_secret_key,
    ).__aenter__()

    try:
        yield client
    finally:
        await client.__aexit__(None, None, None)
