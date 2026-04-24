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


settings = Settings()
