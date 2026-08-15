"""Settings for the API Michi."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Settings for the API Michi."""

    postgres_host: str
    postgres_port: int = 5432
    postgres_name: str
    postgres_user: str
    postgres_password: str

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
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_name}"
        )

    @property
    def domain_url(self) -> str:
        return f"http://{self.host}:{self.port}"


app_settings = AppSettings()
