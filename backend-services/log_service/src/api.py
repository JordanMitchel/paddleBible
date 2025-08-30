from fastapi import FastAPI
from pymongo import MongoClient
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
            print(f"[DEBUG] Found {len(new_logs)} new logs since {last_pushed_ts}")
            streams = []

            for log in new_logs:
                try:
                    ts_ns = str(int(log["timestamp"].timestamp() * 1e9))
                    level = log.get("level", "INFO")
                    stream_entry = {
                        "stream": {
                            "service": log["service"],
                            "level": level
                        },
                        "values": [[ts_ns, log["message"]]]
                    }
                    streams.append(stream_entry)

                    # Print each stream entry for inspection
                    print(f"[DEBUG] Prepared stream entry: {stream_entry}")

                except Exception as e:
                    print("[ERROR] Failed to process log:", log)
                    print(e)

            async with httpx.AsyncClient() as client:
                try:
                    res = await client.post(LOKI_URL, json={"streams": streams})
                    print(f"[DEBUG] Loki response status: {res.status_code}")
                    print(f"[DEBUG] Loki response body: {res.text}")
                    res.raise_for_status()
                except Exception as e:
                    print("Failed to push logs to Loki:", e)

            last_pushed_ts = new_logs[-1]["timestamp"]
            print(f"[DEBUG] Updated last_pushed_ts to {last_pushed_ts}")

        else:
            print("[DEBUG] No new logs to push.")

        await asyncio.sleep(10)

