"""
Defines the base settings of the application
"""

from typing import Optional, List
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Environment variables and settings for the application
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # database
    postgres_host: str = Field(..., json_schema_extra={"env": "POSTGRES_HOST"})
    postgres_db_name: str = Field(..., json_schema_extra={"env": "POSTGRES_DB_NAME"})
    postgres_port: str = Field(default="5432", json_schema_extra={"env": "POSTGRES_PORT"})
    postgres_user: str = Field(..., json_schema_extra={"env": "POSTGRES_USER"})
    postgres_password: str = Field(..., json_schema_extra={"env": "POSTGRES_PASSWORD"})
    # cors
    cors_origins: Optional[List[str]] = Field(default=["*"], json_schema_extra={"env": "CORS_ORIGINS"})

    database_url: Optional[str] = None

    @field_validator("database_url", mode="before")
    @classmethod
    def assemble_database_url(cls, _, info):
        """
        Assembles the database URL based on whether postgres_user and postgres_password is defined
        """
        return (
            f"postgresql+asyncpg://{info.data['postgres_user']}:{info.data['postgres_password']}@"
            f"{info.data['postgres_host']}:{info.data['postgres_port']}/{info.data['postgres_db_name']}"
        )

    @field_validator("cors_origins", mode="before")
    @classmethod
    def split_cors_origins(cls, v):
        """
        Converts comma-separated string to list for CORS origins
        """
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
