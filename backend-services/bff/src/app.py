import asyncio

import uvicorn
from fastapi import FastAPI
from kombu import Connection

from backend.bff.src.routes import router_ws
from backend.bff.src.routes import router_logger, router_scripture
from scripts.background_tasks.start_up_tasks import shutdown_tasks, run_tasks
from shared.log.logger import get_logger, setup_logger, log_queue, log_thread
from shared.utils.config import BROKER_URL

if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="PaddleBible", version="1.0.0", debug=True)
app.include_router(router_scripture.router, prefix="/scripture")
app.include_router(router_logger.router, prefix="/logs")
app.include_router(router_ws.ws_router, prefix="/ws-test")
logger = get_logger()


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
                # logger.info("✅ RabbitMQ is reachable.")
                return True

        # Run the blocking operation in a separate thread
        return await asyncio.to_thread(sync_check)

    except Exception as e:
        logger.info(f"❌ RabbitMQ check failed: {e}")
        return False


@app.on_event("startup")
async def startup_event():
    await setup_logger()  # ✅ Ensure log_producer is ready at startup
    await run_tasks(app, logger)


@app.on_event("shutdown")
async def shutdown():
    """Shutdown event to perform cleanup tasks."""
    log_queue.put(None)  # Signal the thread to exit
    log_thread.join()

    await shutdown_tasks(app, logger)


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="debug")
