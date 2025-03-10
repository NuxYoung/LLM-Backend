from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "文生视频平台"
    debug: bool = True
    api_prefix: str = "api/v1"
    tongyi_api_key: str  # 通过.env文件或环境变量注入
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
    

settings = Settings()
