# 后端API主程序：负责组装路由和服务
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from agent import ask_agent, report_detection
from yolo_service import detect_image
import shutil

app = FastAPI()

# 允许跨域，确保前端网页能正常请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 任务一：大模型对话接口
@app.get("/chat")
def chat(prompt: str):
    return {"response": ask_agent(prompt)}

# 任务二 + 五：AI视觉哨兵（YOLO检测 + 大模型汇报）
@app.post("/detect_and_report")
async def detect_and_report(file: UploadFile = File(...)):
    # 1. 保存前端上传的图片
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # 2. 调用YOLO检测图片里的物体
    objects = detect_image(file_location)
    
    # 3. 根据检测结果，让大模型生成自然语言汇报
    if objects:
        report = report_detection(objects)
    else:
        report = "报告，画面一切正常，未发现可疑目标。"
        
    # 4. 返回给前端
    return {"objects": objects, "report": report}