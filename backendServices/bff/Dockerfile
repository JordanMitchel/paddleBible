FROM python:3.11
WORKDIR /app

RUN addgroup --system bff && adduser --system --ingroup bff bff

COPY bff/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/backendServices

ENV PYTHONPATH="/app"
RUN chown -R bff:bff /app

EXPOSE 8000
USER bff

CMD ["python", "-u", "backendServices/bff/src/app.py"]
