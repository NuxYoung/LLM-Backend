from http import HTTPStatus
from dashscope import VideoSynthesis
import dashscope
from core.config import settings
dashscope.api_key = settings.tongyi_api_key

class TongyiWanxiangService:
    def text2vedio(model: str, prompt: str, size: str):
        rsp = VideoSynthesis.call(model=model,
                              prompt=prompt,
                              size='1280*720',
                              api_key=settings.tongyi_api_key)
        print(rsp)
        if rsp.status_code == HTTPStatus.OK:
            print(rsp.output.video_url)
            return rsp.output.video_url
        else:
            print('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))
            raise Exception('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))

    def text2vedio_async(model: str, prompt: str, size: str):
        # call async api, will return the task information
        # you can get task status with the returned task id.
        rsp = VideoSynthesis.async_call(model=model,
                                        prompt=prompt,
                                        size='1280*720',
                                        api_key=settings.tongyi_api_key);
        print(rsp)
        if rsp.status_code == HTTPStatus.OK:
            print("task_id: %s" % rsp.output.task_id)
        else:
            print('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))
                            
        # get the task information include the task status.
        status = VideoSynthesis.fetch(rsp)
        if status.status_code == HTTPStatus.OK:
            print(status.output.task_status)  # check the task status
        else:
            print('Failed, status_code: %s, code: %s, message: %s' %
                (status.status_code, status.code, status.message))

        # wait the task complete, will call fetch interval, and check it's in finished status.
        rsp = VideoSynthesis.wait(rsp)
        print(rsp)
        if rsp.status_code == HTTPStatus.OK:
            print(rsp.output.video_url)
        else:
            print('Failed, status_code: %s, code: %s, message: %s' %
                (rsp.status_code, rsp.code, rsp.message))
