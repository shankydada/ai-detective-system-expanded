from ultralytics import YOLO
from datetime import datetime

# Load fine-tuned crime-scene-specific model
model = YOLO("yolov8n.pt")  # This will download a small YOLOv8 model

CRIME_LABELS = {
    0: "bloodied_knife",
    1: "broken_window",
    2: "overturned_chair",
    3: "blood_on_bed",
    4: "Bloodied Knife on Carpet",
    5: "Broken Window on North Wall",
    6: "Overturned Chair beside Bed",
    7: "Lamp knocked over",
    8: "Open Drawer with missing contents",
    9: "Knife on Floor",
    10: "Blood Stain on Backsplash",
    11: "Open Refrigerator",
    12: "Broken Plate near Sink",
    13: "Cabinet doors ajar",
    14: "Purse on Floor",
    15: "Broken Window",
    16: "Bookshelf Knocked Over",
    17: "Ranschced",
    18: "Ransckesse - a relnassacked room",
    19: "Point of entry",
    20: "Blood Stain (simirulated)",
    21: "Lamp Knocked Over",
    22: "Blood Trail",
    23: "Handgun",
    24: "Body",
    25: "Shoeprint near dumpster (size 10)",
    26: "Simulated blood trail leading toward trash bin",
    27: "Abandoned purse with contents scattered",
    28: "Metal pipe on ground (potential weapon)",
    29: "Weapon (Bloody Knife)",
    30: "Broken Glass on the floor",
    31: "Blood Splash on Wall",
    32: "Crime Marker Labels",
    33: "Tiled Kitchen Setting",
    34: "Gun near Victim",
    35: "Blood Pool on Grass",
    36: "Evidence Marker",
    37: "Victim's Body Position",
    38: "Outdoor Scene with Natural Lighting",
    39: "Blood Splashes on the Floor",
    40: "Hammer as the Weapon",
    41: "Broken Chair",
    42: "Shoeprints",
    43: "Indoor Room with Curtains",
    44: "Rusty Knife",
    45: "Dried Blood Pool",
    46: "Flipped-over Table",
    47: "Evidence Tags",
    48: "Dimly Lit Dirty Kitchen",
    49: "Shoe",
    50: "Bullet Casings",
    51: "Broken Pot",
    52: "Blood Splatter",
    53: "Outdoor Yard Scene",
    54: "Handgun (9mm)",
    55: "Pool of Blood",
    56: "Torn Fabric",
    57: "Broken Crate",
    58: "Basement Environment with Investigator",
    59: "Rope",
    60: "Syringe",
    61: "Sledgehammer",
    62: "Blood Pool",
    63: "Abandoned Vehicule 3. Cloth",
    64: "Bloodied Knife in Bedroom",
    65: "Broken Window",
    66: "Blood Stain",
    67: "Handgun on Asphalt",
    68: "Cartridge Case",
    69: "Drag Marks",
    70: "Rope in Garage",
    71: "Sledgehammer",
    72: "Blood Pool",
    73: "Syringe by Vehicle",
    74: "Abandoned Vehicle",
    75: "Torn Cloth",
    76: "Pistol - Semi-automatic, near toolbox",
    77: "Bullet Casings - 3 spent casings on floor",
    78: "Blood Splatter - On wall and door",
    79: "Glove - Latex glove under vehicle",
    80: "Broken Lock - Garage door forcibly opened",
    81: "Blunt Weapon (Pipe) - Blood-stained, next to victim",
    82: "Pool of Blood - Adjacent to head trauma",
    83: "Shoe Marks - Two distinct sizes, possible attacker and victim",
    84: "Open Door - Possible escape route",
    85: "Fingerprint Smears - On railing and metal pipe",
    86: "Bloodied Knife - Near victim's outstretched hand",
    87: "Blood Trail - Leading to a nearby dumpster",
    88: "Torn Wallet - Contents scattered, possible motive",
    89: "Shoe Print - Deep impression near victim",
    90: "Broken Phone - Screen shattered, possibly during struggle",

}

def process_image(image_path):
    print(f"[YOLO] Analyzing image: {image_path}")
    results = model(image_path)

    print("\n[DEBUG] YOLO Detections:")
    objects = []
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = CRIME_LABELS.get(cls_id, f"class_{cls_id}")
        conf = float(box.conf[0])
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        print(f"- {label} ({conf:.2f}) at ({center_x:.0f}, {center_y:.0f})")
        objects.append({
            "label": label,
            "confidence": round(conf, 2),
            "position": (round(center_x), round(center_y))
        })

    return {
        "image_path": image_path,
        "objects": objects,
        "timestamp": datetime.now().isoformat(),
        "location": "Unknown (YOLO model does not infer location)"
    }
#Multiple aapproaches
try:
    # Try multiple loading approaches
    try:
        model = YOLO("model/best.pt", device='cpu')
    except Exception as e:
        print(f"First attempt failed: {e}")
        try:
            # Try with a task specified
            model = YOLO("model/best.pt", task='detect')
        except Exception as e:
            print(f"Second attempt failed: {e}")
            # Fall back to a pre-trained model
            print("Falling back to a pre-trained YOLOv8 model")
            model = YOLO("yolov8n.pt")
except Exception as e:
    print(f"All loading attempts failed: {e}")
    raise
