# Use lightweight Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies for Pillow/scikit-learn
RUN apt-get update && apt-get install -y gcc libjpeg-dev zlib1g-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose port for Flask
EXPOSE 5000

# Start Gunicorn web server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "2"]
