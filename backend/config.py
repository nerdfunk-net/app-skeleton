"""
Configuration module for application template.
Simple approach without complex pydantic parsing.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
# Try to load from backend directory first, then from current directory
backend_env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(backend_env_path):
    load_dotenv(backend_env_path)
    print(f"Loaded .env from: {backend_env_path}")
else:
    load_dotenv()
    print("Loaded .env from current directory")


def get_env_bool(key: str, default: bool = False) -> bool:
    """Get boolean environment variable."""
    value = os.getenv(key, str(default)).lower()
    return value in ("true", "1", "yes", "on")


class Settings:
    # Server Configuration
    host: str = os.getenv("BACKEND_SERVER_HOST", os.getenv("SERVER_HOST", "127.0.0.1"))
    port: int = int(os.getenv("BACKEND_SERVER_PORT", os.getenv("SERVER_PORT", "8000")))
    debug: bool = get_env_bool("DEBUG", True)
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    # Authentication Configuration
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "10")
    )

    # Initial credentials for first-time setup
    initial_username: str = os.getenv("INITIAL_USERNAME", "admin")
    initial_password: str = os.getenv("INITIAL_PASSWORD", "admin")

    # Data directory configuration - use project-relative path for Docker compatibility
    data_directory: str = os.getenv(
        "DATA_DIRECTORY",
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "data"),
    )


# Global settings instance
settings = Settings()

if __name__ == "__main__":
    print("App Template Backend Configuration:")
    print(f"  Server: http://{settings.host}:{settings.port}")
    print(f"  Debug Mode: {settings.debug}")

