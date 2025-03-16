from fastapi import APIRouter

from api.chat import text2video_api

api_router = APIRouter()
api_router.include_router(text2video_api.router)