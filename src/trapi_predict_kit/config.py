import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    VIRTUAL_HOST: str = None
    TIMEOUT: int = 30

    DEV_MODE: bool = False
    LOG_LEVEL: str = "ERROR"

    BIOLINK_VERSION: str = "3.1.0"
    TRAPI_VERSION: str = "1.4.0"

    OPENPREDICT_DATA_DIR: str = os.path.join(os.getcwd(), "data")


settings = Settings()
