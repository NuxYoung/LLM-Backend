from fastapi import APIRouter

from api.chat import text2vedio_api

api_router = APIRouter()
api_router.include_router(text2vedio_api.router)