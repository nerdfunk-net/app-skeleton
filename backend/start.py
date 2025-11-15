#!/usr/bin/env python3
"""
App Template Backend Startup Script
Loads configuration and starts the FastAPI server.
"""

import uvicorn
import os
from config import settings
import logging

logger = logging.getLogger(__name__)


def main():
    """Start the FastAPI server with configuration."""

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, settings.log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Log startup information
    logger.info("Starting App Template Backend Server")
    logger.info(f"Server: {settings.host}:{settings.port}")
    logger.info(f"Debug: {settings.debug}")
    logger.info(f"Data Directory: {settings.data_directory}")

    # Start the server
    # Get the backend directory path
    backend_dir = os.path.dirname(__file__)

    # Change to backend directory to ensure Uvicorn only watches backend files
    original_cwd = os.getcwd()
    os.chdir(backend_dir)

    try:
        uvicorn.run(
            "main:app",
            host=settings.host,
            port=settings.port,
            reload=settings.debug,
            reload_dirs=["."],  # Only watch current directory (backend)
            reload_excludes=["../data/**", "data/**"],  # Exclude data directories
            log_level=settings.log_level.lower(),
            access_log=True,
        )
    finally:
        os.chdir(original_cwd)


if __name__ == "__main__":
    main()
