import logging

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Transport mode: "stdio" (local dev) or "http" (deployed)
    transport: str = "stdio"
    port: int = 7860

    # StatsCan API timeout settings (seconds)
    timeout_connect: float = 5.0
    timeout_read: float = 30.0
    timeout_write: float = 5.0
    timeout_pool: float = 5.0

    # Logging level: "DEBUG", "INFO", "WARNING", "ERROR"
    log_level: str = "INFO"

    # Retry settings for transient API failures
    retry_attempts: int = 3
    retry_min_wait: float = 1.0  # seconds before first retry
    retry_max_wait: float = 8.0  # max seconds between retries (exponential backoff)


settings = Settings()

logging.basicConfig(
    level=settings.log_level,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
