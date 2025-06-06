from fastapi import APIRouter, Depends
import os
from helper.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def welcome(app_settings:Settings = Depends(get_settings)):
    return {
        "app_name": app_settings.APP_NAME,
        "version": app_settings.APP_VERSION,
    }