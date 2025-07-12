from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO
from app.detector import predict

app = FastAPI()

@app.post("/predict/")
async def detect_bike(file: UploadFile = File(...)):
    img_bytes = await file.read()
    image = Image.open(BytesIO(img_bytes)).convert("RGB")
    results = predict(image)
    
    detections = []
    for box in results.boxes:
        cls = results.names[int(box.cls[0])]
        conf = float(box.conf[0])
        xyxy = box.xyxy[0].tolist()
        detections.append({"class": cls, "confidence": conf, "box": xyxy})
    
    return JSONResponse(content={"results": detections})
