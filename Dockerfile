# Use official Python image with CUDA support if you're using GPU
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install system dependencies (for OpenCV, image processing etc.)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "app.infer_api:app", "--host", "0.0.0.0", "--port", "8000"]
