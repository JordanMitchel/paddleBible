FROM python:3.11-slim-buster

WORKDIR /pytonProject

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .