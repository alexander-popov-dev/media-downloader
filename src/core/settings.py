from functools import cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseProjectSettings(BaseSettings):
    """Base settings shared across all layers."""

    model_config = SettingsConfigDict(
        env_file=(".env", ".env.local"), env_file_encoding="utf-8", extra="ignore"
    )

    debug: bool = Field(alias="DEBUG", default=False)


# noinspection PyArgumentList
@cache
def get_project_settings() -> BaseProjectSettings:

    return BaseProjectSettings()
