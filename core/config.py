from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_ENDPOINT: str
    OPENAI_API_KEY: str
    OPENAI_MODEL_NAME: str
    OPENAI_MODEL_4_1_NANO: str

    class Config:
        env_file = ".env"

Settings = Settings()