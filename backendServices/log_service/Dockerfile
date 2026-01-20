FROM python:3.11
WORKDIR /app

RUN addgroup --system celery && adduser --system --ingroup celery celery

# requirements live inside log_service/
COPY log_service/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# context = backendServices/, so just copy everything directly
COPY . /app/backendServices

ENV PYTHONPATH="/app"
RUN chown -R celery:celery /app

EXPOSE 5555
USER celery

CMD ["python", "-u", "backendServices/log_service/src/app.py"]
