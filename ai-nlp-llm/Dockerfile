# Use a Python image with PyTorch and other AI dependencies
FROM python:3.11


# Set the working directory
WORKDIR /app

# Copy the requirements and install dependencies
COPY ai-nlp-llm/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code and shared utilities
COPY ai-nlp-llm/ /app/ai-nlp-llm
COPY ./scripts /app/scripts
COPY ./shared /app/shared

# Set the Python path to include shared modules
ENV PYTHONPATH="/app:/app/ai-nlp-llm:/app/shared:/app/scripts"
# Expose the service port
EXPOSE 8000

# Start the AI service

# Command to run the FastAPI app with Uvicorn
CMD ["python", "-u", "ai-nlp-llm/src/app.py"]