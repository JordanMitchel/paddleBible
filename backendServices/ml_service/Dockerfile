FROM python:3.12-slim

# Install uv
RUN pip install "uv>=0.9.21"


WORKDIR /app

# Copy dependency metadata
COPY pyproject.toml uv.lock ./

# ✅ INSTALL deps (this was missing)
RUN UV_NO_VENV=1 uv sync --frozen --no-dev

# Copy application code
COPY ../backendServices/ml_service/ /app/ml_service
COPY ../backendServices/scripts /app/scripts
COPY ../backendServices/shared /app/shared

ENV PYTHONPATH="/app:/app/ml_service:/app/shared:/app/scripts"

EXPOSE 8000

CMD ["python", "-u", "ml_service/src/app.py"]
