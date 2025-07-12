YOLOv8 Object Detection API using FastAPI and Docker

This project demonstrates an object detection API built using a custom-trained YOLOv8 model. 
The model is served via FastAPI and containerized with Docker. It enables real-time predictions on uploaded images and is suitable for deployment or integration into larger production systems.

Project Highlights

•	- YOLOv8-based object detection (e.g., bike/person)
•	- FastAPI for serving predictions over HTTP
•	- Docker support for easy deployment
•	- Swagger UI for testing the API via browser

Project Structure
.
├── app/
│   ├── detector.py        # Handles model loading and inference logic
│   ├── infer_api.py       # FastAPI route to handle image upload & prediction
│   ├── test.jpg           # Sample input image
│   └── yolov8s.pt         # Trained YOLOv8 model weights
├── Dockerfile             # Docker instructions to containerize the app
├── main.py                # App entry point for uvicorn
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation (this file)


Setup Instructions
1.	 Clone the Repository

git clone https://github.com/Ajinkya-001/BIKE-DETECTOR-USING-YOLO-AND-FAST-API.git
cd BIKE-DETECTOR-USING-YOLO-AND-FAST-API

2.	Run Locally (Conda)

conda create -n yolo-env python=3.10 -y
conda activate yolo-env
pip install -r requirements.txt
python main.py

Access the API at: http://localhost:8000/docs

3.	Run with Docker

docker build -t yolo-fastapi-app .
docker run -it --rm -p 8000:8000 yolo-fastapi-app

API Usage

- Navigate to: http://localhost:8000/docs
- Use the /predict/ endpoint
- Upload an image and receive the output with bounding boxes

Use Cases
•	- Real-time helmet or bike detection in surveillance systems
•	- Traffic violation detection in smart cities
•	- Safety compliance systems in industrial zones
•	- Object detection model deployment templates for computer vision projects

Model Information
•	- Architecture: YOLOv8s
•	- Framework: PyTorch
•	- Format: .pt weights
•	- Classes: Bike, Person, Truck (customizable)

Author Info
Ajinkya Patil
Pursuing BTech in Artificial Intelligence and Robotics
Dayananda Sagar University (Batch of 2027)
GitHub: https://github.com/Ajinkya-001

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.
