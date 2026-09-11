from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "JourneyMatch AI"
    database_url: str | None = None
    cors_origins: str = "*"
    rate_limit_per_minute: int = 120
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
