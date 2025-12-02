"""
Main application
"""

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.health import router as health_router
from api.routers.games import games_router
from api.settings import Settings

settings = Settings()


def initialize_application():
    """
    Initialize the fastapi application

    1. Include routers
    2. Mount static folder
    """

    # Initialize FastAPI application
    application = FastAPI(
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # sets the base path of the api. Eg. /api/...
    base_router = APIRouter(prefix="/api")

    # Add routers in application
    base_router.include_router(health_router, prefix="/health", tags=["Health"])
    base_router.include_router(games_router, prefix="/games", tags=["Games"])

    application.include_router(base_router)

    return application


app = initialize_application()
