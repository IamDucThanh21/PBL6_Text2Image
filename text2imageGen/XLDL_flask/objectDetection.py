from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

def objectDetection_run(link):
    results = model.predict(link, device='0')
    return results[0]