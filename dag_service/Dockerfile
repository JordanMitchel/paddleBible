FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your app files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir apache-airflow==2.8.1

# Expose the web UI port
EXPOSE 8080

# Set environment variables (you can also use an .env file)
ENV AIRFLOW_HOME=/app/airflow

# Set the default command
CMD ["python", "main.py"]
