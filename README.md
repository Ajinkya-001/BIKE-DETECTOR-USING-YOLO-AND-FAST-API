# YOLOv8 Object Detection API using FastAPI and Docker

This project demonstrates an object detection API built using a custom-trained YOLOv8 model. The model is served via FastAPI and containerized with Docker. It enables real-time predictions on uploaded images and is suitable for deployment or integration into larger production systems.

## Project Highlights

- YOLOv8-based object detection (e.g., bike/person)
- FastAPI for serving predictions over HTTP
- Docker support for easy deployment
- Swagger UI for testing the API via browser

PROJECT STRUCTURE

<img width="677" height="278" alt="image" src="https://github.com/user-attachments/assets/7d48c399-feca-49e8-b6f1-00cc6f33e837" />







## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ajinkya-001/BIKE-DETECTOR-USING-YOLO-AND-FAST-API.git
cd BIKE-DETECTOR-USING-YOLO-AND-FAST-API
```
2. Run Locally (Conda)
```bash
Copy code
conda create -n yolo-env python=3.10 -y
conda activate yolo-env
pip install -r requirements.txt
python main.py
```
Access the API at: http://localhost:8000/docs

3. Run with Docker
```bash
Copy code
docker build -t yolo-fastapi-app .
docker run -it --rm -p 8000:8000 yolo-fastapi-app
```

API Usage

Navigate to: http://localhost:8000/docs
Use the /predict/ endpoint
Upload an image and receive the output with detection bounding boxes

Use Cases

Real-time helmet or bike detection in surveillance systems
Traffic violation detection in smart cities
Safety compliance systems in industrial zones
Object detection deployment boilerplate for CV projects


Model Information
Architecture: YOLOv8s
Framework: PyTorch
Format: .pt weights
Classes: Bike, Person, Truck (customizable)

Author
Ajinkya Patil
BTech in Artificial Intelligence and Robotics
Dayananda Sagar University, Batch of 2027
GitHub: Ajinkya-001

License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it for commercial or personal purposes.
