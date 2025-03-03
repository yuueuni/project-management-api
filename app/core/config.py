from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str

    EXCLUDED_PATHS: List[str] = [
        "/docs",
        "/redoc",
        "/openapi.json",
        "/api/v1/auth/swagger/token",
        "/api/v1/auth/signin",
        "/api/v1/auth/login",
        "/api/v1/auth/refresh",
        "/api/v1/auth/logout"
    ]

    class Config:
        env_file = ".env"


settings = Settings()
