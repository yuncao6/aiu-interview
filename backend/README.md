# Backend 模块 - 后端推理服务

本模块负责接收前端请求，并调用本地大模型与 YOLO 模型提供服务，实现前后端解耦。

## 📂 文件说明
- `main.py`: FastAPI 主程序，负责定义和组装 API 路由。
- `agent.py`: 智能体核心模块，封装对本地大模型（Ollama）的 API 调用。
- `yolo_service.py`: YOLO 视觉检测模块，负责加载模型并进行图像推理。
- `cli.py`: 命令行交互客户端，满足 CLI 应用形式要求。
- `yolo_demo.py`: YOLO 实时推理部署演示脚本。
- `requirements.txt`: 后端运行所需的 Python 依赖库清单。

## 🚀 启动命令
```bash
pip install -r requirements.txt
uvicorn main:app --reload
