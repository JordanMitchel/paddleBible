# Use an official lightweight Python image
FROM python:3.12-slim

# Install uv (single binary, very fast)
RUN pip install "uv>=0.9.21"

# Set the working directory inside the container
WORKDIR /app

# Copy only dependency files first (for caching)
COPY pyproject.toml uv.lock ./

# Install dependencies (system-wide, no venv in Docker)
RUN UV_NO_VENV=1 uv sync --frozen --no-dev

# Copy the rest of the application code
COPY ../backendServices/bff/ /app/bff
COPY ../backendServices/shared /app/shared
COPY ../backendServices/scripts /app/scripts
COPY ../backendServices/domain /app/domain

# Set the Python path to include shared modules
ENV PYTHONPATH="/app:/app/bff:/app/shared:/app/scripts:/app/domain"

# Expose the application port
EXPOSE 8000

# Start the FastAPI application

# Command to run the FastAPI app with Uvicorn
CMD ["python", "-u", "bff/src/app.py"]