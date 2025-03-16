from http import HTTPStatus
from dashscope import VideoSynthesis
import dashscope
from core.config import settings
dashscope.api_key = settings.tongyi_api_key

class TongyiWanxiangService:
            
    def generate_task_id(model: str, prompt: str, size: str):
        rsp = VideoSynthesis.async_call(model=model,
                                        prompt=prompt,
                                        size='1280*720',
                                        api_key=settings.tongyi_api_key);
        if rsp.status_code == HTTPStatus.OK:
            return rsp.output.task_id
        else:
            print('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))
            raise Exception('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))
        
    def fetch_task_status(task_id: str):
        rsp = VideoSynthesis.fetch(task_id)
        if rsp.status_code == HTTPStatus.OK:
            return rsp.output.task_status
        else:
            print('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))
            raise Exception('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))
        
    def get_video_url(task_id: str):
        rsp = VideoSynthesis.fetch(task_id)
        if rsp.status_code == HTTPStatus.OK:
            return rsp.output.video_url
        else:
            print('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))
            raise Exception('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))
