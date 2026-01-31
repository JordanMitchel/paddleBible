# Use an official Python image
FROM python:3.12-slim

# Install uv (single binary, very fast)
RUN pip install "uv>=0.9.21"

# Set the working directory inside the container
WORKDIR /app

# Create a non-root user before doing anything
RUN addgroup --system celery && adduser --system --ingroup celery celery

# Copy only dependency files first (for caching)
COPY pyproject.toml uv.lock ./

# Install dependencies (system-wide, no venv in Docker)
RUN UV_NO_VENV=1 uv sync --frozen --no-dev

# Copy the source code and shared utilities
COPY ../backendServices/log_service/ /app/log_service
COPY ../backendServices/scripts /app/scripts
COPY ../backendServices/shared /app/shared
COPY ../backendServices/domain /app/domain

# Set the Python path to include shared modules
ENV PYTHONPATH="/app:/app/log_service:/app/shared:/app/scripts:/app/domain"

# Change ownership to celery user
RUN chown -R celery:celery /app

# Expose port for Flower UI
EXPOSE 5555

# Switch to the non-root user
USER celery

# Start the Celery worker when the container runs
CMD ["python", "-u", "log_service/src/app.py"]
