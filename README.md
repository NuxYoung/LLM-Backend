# 文生视频平台

基于FastAPI和LangChain的文生视频平台，支持对接多个大模型。

## 功能特性

- 多模型支持
- 视频生成API
- 模型管理
- 任务队列
- 用户认证

## 快速开始

1. 安装依赖
```bash
pip install -r requirements.txt
```

2. 启动服务
```bash
uvicorn main:app --reload
```

3. 访问API文档
```
http://localhost:8000/docs
```

## 项目结构

```
.
├── app/            # 主应用模块
├── config/         # 配置管理
├── models/         # 模型管理
├── services/       # 业务服务
├── static/         # 静态文件
├── templates/      # 模板文件
├── tests/          # 测试
├── utils/          # 工具函数
├── main.py         # 入口文件
├── requirements.txt # 依赖文件
└── README.md       # 项目说明
