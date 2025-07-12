YOLOv8 Object Detection API with FastAPI and Docker

This repository provides an API for object detection using a custom-trained YOLOv8 model. The application is built with FastAPI and containerized using Docker, allowing for deployment and integration into various projects.

Project Overview

This project implements a RESTful API that accepts image uploads and returns object detection results using a YOLOv8 model trained to detect bikes and related objects.

Features

- Inference endpoint built with FastAPI
- Support for image uploads and predictions via POST requests
- Uses a custom-trained YOLOv8 model
- Dockerized for consistent cross-platform deployment
- Swagger UI documentation available for testing

Setup Instructions

Clone the Repository

git clone https://github.com/<your-username>/yolo-fastapi.git  
cd yolo-fastapi

Build the Docker Image

docker build -t yolo-fastapi-app .

Run the Docker Container

docker run -it --rm -p 8000:8000 yolo-fastapi-app

Access the API at:  
http://localhost:8000

Interactive API documentation available at:  
http://localhost:8000/docs

API Usage

Endpoint: POST /predict/  
Description: Accepts an image file and returns detected objects with bounding boxes and confidence scores.

Request

- Method: POST  
- Content-Type: multipart/form-data  
- Field: file (image file)

Directory Structure

yolo-fastapi/  
├── app/  
│   ├── infer_api.py            FastAPI application logic  
│   ├── utils.py                Utility functions  
│   └── yolov8_model/  
│       └── best.pt             Trained YOLOv8 model weights  
├── Dockerfile                  Docker image build file  
├── requirements.txt            Python dependencies  
├── requirements-cuda.txt       Optional: GPU dependencies  
├── .gitignore  
└── README.md

Requirements:

To install dependencies locally:

pip install -r requirements.txt

For GPU support:

pip install -r requirements-cuda.txt

Model Details

- Model: YOLOv8s  
- Format: PyTorch (.pt)  
- Detection Classes: Bike, Person, Truck (modifiable)

Author

Ajinkya Patil  
B.Tech in Artificial Intelligence and Robotics  
Dayananda Sagar University  
GitHub: https://github.com/Ajinkya-001
