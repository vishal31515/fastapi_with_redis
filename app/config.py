from pydantic import BaseSettings, Field
from functools import lru_cache
from pathlib import Path
from typing import List

from pydantic import BaseSettings, Field


BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    ENV: str = Field(..., env="ENV")
    REDIS_HOST: str = Field(..., env="REDIS_HOST")
    REDIS_PORT: str = Field(..., env="REDIS_PORT")

    class Config:
        env_file = str(BASE_DIR)+"/.env"


class LocalSettings(Settings):
    DEBUG: bool = True


class ProdSettings(Settings):
    DEBUG: bool = False


@lru_cache()
def get_settings():
    envs = {
        "local": LocalSettings,
        "prod": ProdSettings,
    }
    settings = envs[Settings().ENV]()
    if not settings:
        raise Exception(
            """Environment does not exist
            Please chose one of below:-
            prod
            local
            """
        )
    return settings


settings = get_settings()
