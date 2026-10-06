# 工程日志
## 项目进展
今天也是开始了为人工智能协会二面做准备，我成功安装并注册GitHub账号。问ai学习如何写工程日志，建好了仓库，还没有正式开始完成任务。

## 卡住的问题
1. GitHub网络访问超时，无法正常进入网站。 （下载了一个Watt Toolkit）
2. 很多专业知识不清楚，频繁依靠ai
3. 打代码容易出错
4. 有些英文没有被翻译成中文，有点不习惯，看不大懂

## AI使用情况
在本次学习过程中，遇到报错提示、网络问题等问题，都是通过AI查询理解。

## 吐槽
1：这个GitHub网页也太不稳定了吧，总是打不开，卡了我好久
2：GitHub的用户名居然不能重复，天知道我试了多少个名字才注册好

## 2026年10月5日 (任务一 + 任务二)

### 📅 项目进展记录

#### 阶段一：本地大模型部署与智能体开发 (任务一)
- **本地大模型部署**：
  - 完成了 Ollama 的本地安装，并成功拉取并运行了 `qwen2:0.5b` 模型，跑通了基础的中文对话测试。
  - 将大模型作为 Model Provider，通过 API 形式对外提供服务。
- **智能体开发**：
  - 编写了 `backend/agent.py`，封装了对本地 Ollama 服务的请求逻辑，实现了基础的智能体封装。
- **后端接口与前端联调**：
  - 使用 FastAPI 编写了 `backend/main.py`，暴露了 `/chat` 接口，实现了前后端解耦。
  - 编写了前端界面 `frontend/index.html`，通过 Fetch API 调用后端接口，完成了 Web 应用的对话交互。
  - 编写了 `backend/cli.py`，实现了 CLI 命令行交互形式

#### 阶段二：YOLO 跑通与应用接入 (任务二)
- **模型训练**：
  - 根据提供的参考博客，使用 `X-AnyLabeling` 对本地搜集的 10 张图片（猫、狗）进行了矩形框标注。
  - 编写/运行了 `script/json2txt.py` 将 JSON 标注转换为 YOLO 格式，并运行 `script/DataProcess.py` 完成了训练集/验证集/测试集的划分。
  - 修改 `config/dataset.yaml` 和 `config/train.yaml`，在本地成功完成了一次 10 个 epoch 的 YOLOv8 训练，模型权重保存为 `best.pt`。
- **实时推理部署**：
  - 参考官方 `ultralytics` 库，编写了 `backend/yolo_demo.py`，通过 Python 快速实现了对本地图片的实时推理，成功弹窗显示了检测框。
- **Web 应用接入**：
  - 修改 `backend/yolo_service.py` 加载本地训练好的 `best.pt` 权重。
  - 在 `backend/main.py` 中新增了 `/detect` 上传接口，并在前端 `index.html` 中增加了图片上传检测模块，实现了 Web 端图片检测闭环。

### 🧗 遇到的困难与解决思路 
1. **Git 分支名不匹配问题**：
   - **卡点**：初次推送到 GitHub 时报错 `src refspec main does not match any`。
   - **解决**：排查发现本地默认分支为 `master`，而远程期望 `main`。通过 `git branch -M main` 强制重命名分支后，成功推送到远程仓库。
2. **网络限制导致官方数据集与模型下载失败 (SSL 证书错误)**：
   - **卡点**：在 YOLO 训练初期，由于网络环境限制，无法从 GitHub 自动下载 `yolov8n.pt` 权重和 `coco8.zip` 数据集，报错 `CERTIFICATE_VERIFY_FAILED`。
   - **解决**：
     1. 手动下载了 `yolov8n.pt` 并放入本地目录，修改 `main.py` 优先读取本地权重。
     2. 放弃官方 `coco8` 数据集，改为自己通过 `X-AnyLabeling` 标注本地图片，并在 `DataProcess.py` 的帮助下，构建了本地小数据集，成功绕过网络限制完成了训练。
3. **本地数据集路径配置错误**：
   - **卡点**：训练时一直报错 `images not found`，无法找到验证集目录。
   - **解决**：通过检查文件树，发现 `DataProcess.py` 生成的路径与 `dataset.yaml` 中默认的相对路径不一致。将 `dataset.yaml` 中的 `path` 改为正确的绝对路径后，训练顺利启动。
4. **Web 端上传图片时的环境依赖缺失**：
   - **卡点**：前端上传图片到后端时报 `RuntimeError: Form data requires "python-multipart" to be installed`。
   - **解决**：识别到 FastAPI 处理表单数据需要额外依赖，通过 `pip install python-multipart` 安装后解决。

### 🤖 AI 使用情况说明
基本全是ai

## 2026年10月6日
- 重新设计了工程结构，将大模型对话与YOLO视觉检测整合，实现了“AI视觉哨兵”创意作品。
- 模块化拆分：agent.py(认知) + yolo_service.py(感知) + main.py(组装)+cli.py(cli应用)
- 解决了昨天遇到的路径混乱问题，将训练好的best.pt直接放在backend目录下，简化了引用路径。
-**遇到的卡点**：在尝试使用官方 `coco8` 数据集训练时，遭遇网络 SSL 证书拦截。后改为手动下载 `yolov8n.pt` 并放弃下载数据集，改用本地标注图片进行训练，成功绕过网络限制。
- **另一个卡点**：前端上传图片时，FastAPI 报错缺少 `python-multipart` 依赖，通过 `pip install python-multipart` 解决。
- 下一步：整理文档，准备面试答辩。