# Use an official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Create a non-root user before doing anything
RUN addgroup --system celery && adduser --system --ingroup celery celery

# Copy the requirements and install dependencies as non-root
COPY log_service/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code and shared utilities
COPY log_service/ /app/log_service
COPY ./scripts /app/scripts
COPY ./shared /app/shared
COPY domain /app/domain

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
