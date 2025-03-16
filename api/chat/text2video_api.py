from typing import AsyncGenerator
import aiohttp
from fastapi.responses import PlainTextResponse, StreamingResponse
from services.llms.tongyi_wanxiang_service import TongyiWanxiangService
from fastapi import APIRouter
import logging

router = APIRouter(prefix="/text2", tags=["text2"])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
        
@router.post("/video/task_id")
async def generate_task_id(model: str, prompt: str, size: str):
    logger.info("model: %s, prompt: %s, size: %s" % (model, prompt, size))
    match model:
        case "wanx2.1-t2v-turbo":
            task_id = TongyiWanxiangService.generate_task_id(model, prompt, size)
        case _:
            logger.error("model not found: %s" % model)
            return {"error": "model not found"}
    
    return PlainTextResponse(content=task_id)

@router.post("/video/task_status")
async def fetch_task_status(task_id: str):
    logger.info("task_id: %s" % task_id)
    try:
        status = TongyiWanxiangService.fetch_task_status(task_id)
    except Exception as e:
        logger.error("fetch_task_status error: %s" % e)
        return PlainTextResponse(status_code=500, content="fetch_task_status error: %s" % e)
    
    return PlainTextResponse(content=status)

@router.get("/video/url")
async def get_video_url(task_id: str):
    logger.info("task_id: %s" % task_id)
    try:
        video_url = TongyiWanxiangService.get_video_url(task_id)
    except Exception as e:
        logger.error("get_video_url error: %s" % e)
        return PlainTextResponse(status_code=500, content="get_video_url error: %s" % e)
    
    return PlainTextResponse(content=video_url)

@router.get("/video", response_class=StreamingResponse, responses={200: {"content": {"video/mp4": {}}}})
async def get_video(url: str):
    async def video_generator() -> AsyncGenerator[bytes, None]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    raise Exception(f"Failed to fetch video, status code: {resp.status}")
                async for chunk in resp.content.iter_chunked(1024 * 1024):  # 1MB chunks
                    yield chunk

    return StreamingResponse(video_generator(), media_type="video/mp4", headers={"Content-Disposition": "attachment; filename=video.mp4"})