import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings"""
    
    # API Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama-3.3-70b-versatile"  # Fast and good quality
    MAX_TOKENS = 4096
    
    # App Configuration
    APP_NAME = os.getenv("APP_NAME", "AI Document Analyzer")
    MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", 10))
    DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
    
    # Supported file types
    SUPPORTED_FILE_TYPES = ["pdf", "txt"]
    
    @classmethod
    def validate(cls):
        """Validate required settings"""
        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        return True

settings = Settings()