def process_image(image_path):
    print(f"Processing image: {image_path}")
    detected_objects = [
        {"label": "knife", "confidence": 0.92, "position": (100, 200)},
        {"label": "blood", "confidence": 0.87, "position": (150, 250)},
        {"label": "body", "confidence": 0.95, "position": (300, 400)},
        {"label": "broken_window", "confidence": 0.80, "position": (500, 100)}
    ]
    return {
        "image_path": image_path,
        "objects": detected_objects,
        "timestamp": "2025-04-11T14:00:00",
        "location": "Sector 5, Downtown City"
    }
