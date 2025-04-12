# 🕵️ AI Detective System (Final Version)

This system analyzes a crime scene image using YOLOv8, extracts key evidence, matches it with previous cases, generates theories, reconstructs the event, and provides legal guidance.

## ✅ Features
- Real image input via prompt
- Object detection using YOLOv8 (`ultralytics`)
- IPC and legal recommendation
- No hardcoded image dependency

## 🚀 How to Run

1. **Install requirements**
```bash
pip install -r requirements.txt
```

2. **Install system-level dependencies (for OpenCV)**
```bash
sudo apt install libgl1
```

3. **Run the system**
```bash
python main.py
```

4. **When prompted**, enter a path to a crime scene image:
```
Enter the full path to the crime scene image:
```

## 📦 Requirements
```
ultralytics
opencv-python
```
