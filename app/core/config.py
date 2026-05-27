from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "production"
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
