import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

# get the current working directory
CWD = os.getcwd()
# print(f"CWD={CWD}")

BASE_DIR = Path(__file__).resolve().parent.parent
logger.info(f"BASE_DIR={BASE_DIR}")

# find the .env in parent dir
load_dotenv(verbose=True)


class Settings(BaseSettings):
    env_file: str
    APP_NAME: str

    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "ci", "production"] = "local"

    JWT_SECRET: str
    CSRF_SECRET: str

    # assume the .env file is in the directory above the project
    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env", extra="allow")


settings = Settings(env_file=f"{BASE_DIR}/.env")
