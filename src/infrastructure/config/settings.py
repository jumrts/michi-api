"""Settings for the API Michi."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Settings for the API Michi."""

    name: str = "API Michi"
    version: str = "0.1.0"
    description: str = "Backend for API Michi"

    host: str = "0.0.0.0"
    port: int = 8080

    methods: list[str] = ["*"]
    headers: list[str] = ["*"]
    origins: list[str] = [
        "http://localhost:5173",  # SvelteKit dev
    ]
    allow_credentials: bool = True

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def domain_url(self) -> str:
        return f"http://{self.host}:{self.port}"


class DatabaseSettings(BaseSettings):
    """Settings for the database."""

    host: str = Field(validation_alias="POSTGRES_HOST")
    port: int = Field(validation_alias="POSTGRES_PORT")
    name: str = Field(validation_alias="POSTGRES_NAME")
    user: str = Field(validation_alias="POSTGRES_USER")
    password: str = Field(validation_alias="POSTGRES_PASSWORD")

    model_config = SettingsConfigDict(
        prefix="postgres", env_file=".env", extra="ignore"
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.name}"
        )


class AuthSettings(BaseSettings):
    """Settings for authentication."""

    secret_key: str = Field(validation_alias="AUTH_SECRET_KEY")
    expiration_seconds: int = Field(validation_alias="AUTH_EXPIRATION_SECONDS")
    algorithm: str = Field(validation_alias="AUTH_ALGORITHM")
    token_prefix: str = Field(validation_alias="AUTH_TOKEN_PREFIX")
    cookie_secure: str = Field(validation_alias="AUTH_COOKIE_SECURE")

    model_config = SettingsConfigDict(prefix="auth", env_file=".env", extra="ignore")


class RateLimitSettings(BaseSettings):
    enabled: bool = Field(
        default=True,
        validation_alias="RATE_LIMIT_ENABLED",
    )

    requests: int = Field(
        default=100,
        validation_alias="RATE_LIMIT_REQUESTS",
    )

    window_seconds: int = Field(
        default=60,
        validation_alias="RATE_LIMIT_WINDOW_SECONDS",
    )

    auth_requests: int = Field(
        default=3,
        validation_alias="AUTH_RATE_LIMIT_REQUESTS",
    )

    auth_window_seconds: int = Field(
        default=60,
        validation_alias="AUTH_RATE_LIMIT_WINDOW_SECONDS",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @property
    def default_limit(self) -> str:
        return f"{self.requests}/{self.window_seconds} seconds"

    @property
    def auth_limit(self) -> str:
        return f"{self.auth_requests}/{self.auth_window_seconds} seconds"


app_settings = AppSettings()
database_settings = DatabaseSettings()
auth_settings = AuthSettings()
rate_limit_settings = RateLimitSettings()
