from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Automatically instruments all routes and exposes /metrics
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with Prometheus!"}

@app.get("/hello")
def say_hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
