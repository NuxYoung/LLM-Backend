FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制项目的依赖文件
COPY requirements.txt .

# 安装依赖并清理缓存
RUN pip install --no-cache-dir -r requirements.txt

ENV ROOT_PATH=/fifan-llm

# 复制项目文件到工作目录
COPY . .

# 暴露应用运行的端口
EXPOSE 8000

# 启动FastAPI应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]