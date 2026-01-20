FROM python:3.11
WORKDIR /app

RUN addgroup --system celery && adduser --system --ingroup celery celery

COPY ml_service/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/backendServices

ENV PYTHONPATH="/app"
RUN chown -R celery:celery /app

EXPOSE 8000
USER celery

CMD ["python", "-u", "backendServices/ml_service/src/app.py"]
