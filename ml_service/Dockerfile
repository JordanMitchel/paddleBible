# Use a Python image with PyTorch and other AI dependencies
FROM python:3.11


# Set the working directory
WORKDIR /app

# Copy the requirements and install dependencies
COPY ml_service/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code and shared utilities
COPY ml_service/ /app/ml_service
COPY ./scripts /app/scripts
COPY ./shared /app/shared

# Set the Python path to include shared modules
ENV PYTHONPATH="/app:/app/ml_service:/app/shared:/app/scripts"
# Expose the service port
EXPOSE 8000

# Start the AI service

# Command to run the FastAPI app with Uvicorn
CMD ["python", "-u", "ml_service/src/app.py"]