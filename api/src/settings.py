from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "luna_db"
    DB_USER: str = "luna"
    DB_PASSWORD: str = "prikol"
    DB_DRIVER: str = "postgresql+asyncpg"

    HEADLESS_TOGGLE: bool = False
    IMAGE_PATH: str = "image.jpg"

    SENTRY_DSN: str = ""

    @property
    def db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
