from ultralytics import YOLO
from PIL import Image
import numpy as np

model = YOLO("bike-detector.pt") 
def predict(image: Image.Image):
    results = model.predict(image)
    return results[0]
