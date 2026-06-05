from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str
    BASE_URL: str
    API_KEY: str
    model_config = ConfigDict(
        env_file = ".env",
        extra="ignore"
    )        
settings = Settings()