# 智能体核心模块：负责接收指令并调用本地大模型
import requests

def ask_agent(prompt):
    # 作为 Model Provider，调用 Ollama 的 API
    res = requests.post("http://localhost:11434/api/generate", 
                        json={"model": "qwen2:0.5b", "prompt": prompt, "stream": False})
    return res.json()["response"]

# 创意作品核心：AI视觉哨兵汇报
def report_detection(detected_objects):
    # 将检测结果作为提示词，让大模型用自然语言汇报
    prompt = f"你是一个安防哨兵。刚刚摄像头检测到了以下物体：{', '.join(detected_objects)}。请用一句话向我汇报情况，语气要简洁、专业。"
    res = requests.post("http://localhost:11434/api/generate", 
                        json={"model": "qwen2:0.5b", "prompt": prompt, "stream": False})
    return res.json()["response"]