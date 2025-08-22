from fastapi import APIRouter
import os

router = APIRouter(prefix="/health", tags=["Health & Utility"])


@router.get("/")
def health_check():
    """Simple Health check endpoint"""
    return {"status": "ok"}


def version_info():
    """Return app version and environment info"""
    return {
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "environment": os.getenv("APP_ENV", "development"),
    }