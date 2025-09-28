# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first for better caching
COPY requirements.txt .

# Install Python dependencies (requests + pytest for testing)
RUN pip install --no-cache-dir -r requirements.txt pytest

# Copy the rest of your application code into the container
COPY . .

# Default command: run your script
CMD ["python", "main.py"]
