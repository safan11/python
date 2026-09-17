from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3"
    ollama_api_key: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
