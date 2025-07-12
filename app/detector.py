from ultralytics import YOLO
from PIL import Image
import numpy as np

model = YOLO("app/yolov8s.pt") 
def predict(image: Image.Image):
    results = model.predict(image)
    return results[0]
