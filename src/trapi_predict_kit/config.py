from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    BIOLINK_VERSION: str = "3.1.0"
    TRAPI_VERSION: str = "1.5.0"

    TIMEOUT: int = 30
    LOG_LEVEL: str = "ERROR"

    VIRTUAL_HOST: Optional[str] = None


settings = Settings()
