from functools import lru_cache
from typing import Union
import os
import pathlib

PROJECT_NAME = "Chatlet"


class Config:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent

    # MongoDB settings
    MONGODB_URI: str = os.environ.get("MONGODB_URI")
    DATABASE_NAME: str = os.environ.get("DATABASE_NAME")

    # Security settings
    JWT_SECRET_KEY: str = os.environ.get("SECRET_KEY")

    # FastMail SMTP settings
    MAIL_CONSOLE: bool = os.environ.get("MAIL_CONSOLE", default=False)
    MAIL_SERVER = os.environ.get("MAIL_SERVER", default="smtp.server.io")
    MAIL_PORT: int = os.environ.get("MAIL_PORT", default=587)
    MAIL_USERNAME: str = os.environ.get("MAIL_USERNAME", default="")
    MAIL_PASSWORD: str = os.environ.get("MAIL_PASSWORD", default="")
    MAIL_SENDER: str = os.environ.get("MAIL_SENDER", default="noreply@chatlet.io")


class TestingConfig(Config):
    DATABASE_NAME: str = "TestChatlet"
    JWT_SECRET_KEY: str = "secret"
    PROJECT_NAME: str = "TestChatlet"


@lru_cache()
def get_config() -> Union[TestingConfig, Config]:
    config = {"test": TestingConfig, "dev": Config}
    get_conf_name = os.environ.get("ENVIRONMENT")
    return config.get(get_conf_name)()


settings = get_config()
