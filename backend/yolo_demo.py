# YOLO 实时推理部署脚本
from ultralytics import YOLO
import cv2

def infer_local_image():
    print(">>> 加载本地模型进行实时推理")
    model = YOLO("yolov8n.pt") # 或者用你训练的 best.pt
    # 推理本地的一张测试图片
    results = model("1.jpg") 
    
    for r in results:
        im_array = r.plot()
        cv2.imshow("YOLO Inference", im_array)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(">>> 推理完成")

if __name__ == "__main__":
    infer_local_image()