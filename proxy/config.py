import os
from typing import List


class Config:
    HOST: str = os.environ.get("HOST", "0.0.0.0")
    PORT: str = os.environ.get("PORT", 8000)
    TARGET_URL: str = "https://habr.com/"
    REPLACE_URLS: List[str] = [
        "https://habr.com/",
        "http://habrahabr.ru/",
        "https://habrahabr.ru/",
    ]
    HTTP_TIMEOUT: int = 60


config = Config()
