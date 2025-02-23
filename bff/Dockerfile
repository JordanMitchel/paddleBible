# Use an official lightweight Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (for caching)
COPY bff/requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY bff/ /app/bff
COPY shared /app/shared
COPY scripts /app/scripts
COPY domain /app/domain

# Set the Python path to include shared modules
ENV PYTHONPATH="/app:/bff:/app/shared:/app/scripts:/app/domain"
# Expose the application port
EXPOSE 8002

# Start the FastAPI application

# Command to run the FastAPI app with Uvicorn
CMD ["python", "-u", "bff/src/app.py"]
