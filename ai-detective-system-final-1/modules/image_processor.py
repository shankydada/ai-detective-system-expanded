
from ultralytics import YOLO

def process_image(image_path):
    print(f"[YOLO] Analyzing image: {image_path}")
    model = YOLO("yolov8n.pt")  # Load pre-trained model (or download if not present)
    results = model(image_path)

    objects = []
    for r in results[0].boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = r
        label = model.names[int(cls)]
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        objects.append({
            "label": label,
            "confidence": round(conf, 2),
            "position": (round(center_x), round(center_y))
        })

    return {
        "image_path": image_path,
        "objects": objects,
        "timestamp": "2025-04-11T14:00:00",
        "location": "Unknown (YOLO model does not infer location)"
    }
