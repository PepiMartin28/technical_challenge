from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    TYPESENSE_HOST: str
    TYPESENSE_PORT: int
    TYPESENSE_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    
    class Config:
        env_file = ".env" 

settings = Settings()