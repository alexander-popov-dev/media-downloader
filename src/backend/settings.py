from functools import cache

from pydantic import Field

from src.core.settings import BaseProjectSettings


class BackendSettings(BaseProjectSettings):
    """HTTP-layer configuration for the FastAPI backend."""

    secret_key: str = Field(alias="SECRET_KEY")
    cors_origins: list[str] = Field(alias="CORS_ORIGINS", default=[])


# noinspection PyArgumentList
@cache
def get_backend_settings() -> BackendSettings:
    """Return the singleton BackendSettings instance."""
    return BackendSettings()  # pyright: ignore[reportCallIssue]