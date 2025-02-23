import uvicorn
from fastapi import FastAPI

app = FastAPI(title="PaddleBible Suite")

@app.get("/")
def read_root():
    return {"message": "Welcome to PaddleBible Suite"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug")
