from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime
from prometheus_fastapi_instrumentator import Instrumentator
import httpx
import asyncio

LOKI_URL = "http://loki:3100/loki/api/v1/push"

app = FastAPI()
Instrumentator().instrument(app).expose(app)

client = MongoClient("mongodb://root:rootPassword@mongodb:27017/")
log_collection = client.logs.log_entries

last_pushed_ts = None  # keep track of last log timestamp


@app.get("/")
def health():
    return {"status": "log_service running"}


@app.on_event("startup")
async def start_pushing_logs():
    asyncio.create_task(push_logs_to_loki())


async def push_logs_to_loki():
    global last_pushed_ts
    while True:
        query = {}
        if last_pushed_ts:
            query["timestamp"] = {"$gt": last_pushed_ts}

        new_logs = list(log_collection.find(query).sort("timestamp", 1))

        if new_logs:
            streams = []
            for log in new_logs:
                ts_ns = str(int(datetime.strptime(log["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ").timestamp() * 1e9))
                level = log.get("level", "INFO")
                streams.append({
                    "stream": {
                        "service": "log_service",
                        "level": level
                    },
                    "values": [[ts_ns, log["message"]]]
                })

            async with httpx.AsyncClient() as client:
                try:
                    res = await client.post(LOKI_URL, json={"streams": streams})
                    res.raise_for_status()
                except Exception as e:
                    print("Failed to push logs to Loki:", e)

            last_pushed_ts = new_logs[-1]["timestamp"]

        await asyncio.sleep(10)

