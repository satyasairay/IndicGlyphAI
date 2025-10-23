"""Application configuration helpers."""

from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "DatasetForge API"
    environment: str = Field(default="development", validation_alias="ENVIRONMENT")
    debug: bool = Field(default=False, validation_alias="DEBUG")

    database_url: str = Field(
        default="postgresql+asyncpg://datasetforge:datasetforge@db:5432/datasetforge",
        validation_alias="DATABASE_URL",
    )
    alembic_ini_path: str = Field(default="alembic.ini", validation_alias="ALEMBIC_INI_PATH")

    s3_endpoint_url: Optional[str] = Field(default=None, validation_alias="S3_ENDPOINT_URL")
    s3_access_key: Optional[str] = Field(default=None, validation_alias="S3_ACCESS_KEY")
    s3_secret_key: Optional[str] = Field(default=None, validation_alias="S3_SECRET_KEY")
    s3_region: Optional[str] = Field(default="us-east-1", validation_alias="S3_REGION")
    s3_bucket: str = Field(default="datasetforge", validation_alias="S3_BUCKET")

    cors_origins: list[str] = Field(
        default_factory=lambda: ["http://localhost:5173"],
        validation_alias="CORS_ORIGINS",
    )
    log_level: str = Field(default="INFO", validation_alias="LOG_LEVEL")
    version: str = Field(default="0.1.0", validation_alias="APP_VERSION")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached Settings instance."""

    return Settings()
