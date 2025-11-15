"""
Main FastAPI application template.

Minimal application with authentication and permission management.
"""

from __future__ import annotations
import logging
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from routers.auth import router as auth_router
from routers.profile import router as profile_router
from routers.rbac import router as rbac_router
from routers.oidc import router as oidc_router
from health import router as health_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="App Template API",
    description="Minimal application template with authentication and RBAC",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    redirect_slashes=True,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(rbac_router)
app.include_router(oidc_router)
app.include_router(health_router)


# Health check and basic endpoints
@app.get("/")
async def root():
    """Root endpoint with basic API information."""
    return {
        "message": "App Template API - Minimal template with authentication and RBAC",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
    }


if __name__ == "__main__":
    import uvicorn
    from config import settings

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=True
    )
