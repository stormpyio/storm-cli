from functools import lru_cache
from storm.core.settings import AppSettings


class Settings(AppSettings):
    app_name: str = "demo-app"


@lru_cache()
def get_settings():
    return Settings()
