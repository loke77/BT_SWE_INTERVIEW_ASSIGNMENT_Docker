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

#To keep the container running so we can connect and execute the script
ENTRYPOINT ["tail","-f","/dev/null"]

# Default command: run your script
CMD ["python", "main.py"]
