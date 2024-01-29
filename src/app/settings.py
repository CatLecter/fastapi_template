from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEVELOP: bool = False
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000
    TITLE: str = 'Data API'
    VERSION: str = 'v1.0'
    DOC_URL: str = '/docs'
    OPENAPI_URL: str = '/openapi.json'
    LOG_LEVEL: str = 'debug'
    STORAGE_URI: str = 'postgresql+asyncpg://admin:admin@localhost:5432/db'
    POOL_SIZE: int = 20
    MAX_OVERFLOW: int = 5


settings = Settings()
