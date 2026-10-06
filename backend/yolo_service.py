# YOLO 推理服务模块：负责图像检测
from ultralytics import YOLO

def detect_image(image_path):
    # 加载我们训练好的模型（best.pt 需要放在 backend 目录下）
    model = YOLO("yolov8n.pt")  # 改用官方预训练模型，识别能力更强
    results = model(image_path)
    # 提取去重后的物体名称列表
    detected_classes = [model.names[int(cls)] for cls in results[0].boxes.cls]
    return list(set(detected_classes))