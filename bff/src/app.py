import asyncio
import uuid

import uvicorn
from fastapi import FastAPI
from kombu import Connection

from bff.src.routes import router_scripture, router_ws
from scripts.background_tasks.start_up_tasks import run_tasks, shutdown_tasks, run_kombu_tasks, run_db_tasks
from shared.utils.config import BROKER_URL

if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="PaddleBible", version="1.0.0", debug=True)
app.include_router(router_scripture.router, prefix="/scripture")
app.include_router(router_ws.ws_router, prefix="/ws-test")


@app.get("/health")
async def health_check():
    """Health check endpoint for FastAPI and RabbitMQ using Kombu."""
    rabbitmq_status = await check_rabbitmq()
    return {
        "status": "healthy" if rabbitmq_status else "unhealthy",
        "rabbitmq": "up" if rabbitmq_status else "down"
    }


async def check_rabbitmq():
    """Asynchronously checks RabbitMQ connectivity using Kombu."""
    try:
        def sync_check():
            with Connection(BROKER_URL) as conn:
                conn.ensure_connection(max_retries=3)
                print("✅ RabbitMQ is reachable.")
                return True

        # Run the blocking operation in a separate thread
        return await asyncio.to_thread(sync_check)

    except Exception as e:
        print(f"❌ RabbitMQ check failed: {e}")
        return False


@app.on_event("startup")
async def startup_event():
    try:
        print(" Running background tasks...")  # Debug print
        await run_kombu_tasks(app)
        await run_db_tasks()
    except Exception as e:
        print(f"🔥 Error in background tasks: {e}")

@app.on_event("shutdown")
async def shutdown():
    await shutdown_tasks(app)


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="debug")
