from fastapi.responses import PlainTextResponse
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

@router.post("/vedio")
async def text2vedio(model: str, prompt: str, size: str):
    logger.info("model: %s, prompt: %s, size: %s" % (model, prompt, size))
    try:
        match model:
            case "wanx2.1-t2v-turbo":
                vedio_url = TongyiWanxiangService.text2vedio(model, prompt, size)
            case _:
                logger.error("model not found: %s" % model)
                return {"error": "model not found"}
    except Exception as e:
        logger.error("text2vedio error: %s" % e)
        return PlainTextResponse(status_code=500, content="text2vedio error: %s" % e)
    
    return PlainTextResponse(content=vedio_url)

@router.post("/vedio/async")
async def text2vedio_async(model: str, prompt: str, size: str):
    logger.info("model: %s, prompt: %s, size: %s" % (model, prompt, size))
    match model:
        case "wanx2.1-t2v-turbo":
            rsp = TongyiWanxiangService.text2vedio_async(model, prompt, size)
        case _:
            logger.error("model not found: %s" % model)
            return {"error": "model not found"}