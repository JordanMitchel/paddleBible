import asyncio
import uvicorn
from fastapi import FastAPI
from kombu import Connection

from ml_service.src.services.service_bus.MLKombuConsumer import MLKombuConsumer
from shared.utils.config import BROKER_URL

app = FastAPI()

# Global references for Kombu services
ai_consumer_service: MLKombuConsumer
consumer_task: asyncio.Task | None = None


@app.on_event("startup")
async def startup_event():
    """Setup Kombu consumer and producer on startup."""
    global ai_consumer_service

    try:
        print("✅ Connected to RabbitMQ")
        # Initialize Kombu Consumer
        ai_consumer_service = MLKombuConsumer()

        # Run Kombu consumer in a separate thread
        asyncio.create_task(asyncio.to_thread(ai_consumer_service.run))

        print(f"✅ Kombu consumer listening on queue: {ai_consumer_service.queue.name}")

    except Exception as e:
        print(f"❌ Failed to setup Kombu services: {e}")


@app.on_event("shutdown")
async def shutdown_event():
    """Gracefully shutdown Kombu producer & consumer."""
    global ai_consumer_service, consumer_task

    if consumer_task:
        consumer_task.cancel()
        try:
            await consumer_task  # Ensure the task stops cleanly
        except asyncio.CancelledError:
            print("🛑 Kombu consumer task cancelled.")
        consumer_task = None

    print("🛑 Kombu consumer stopped, RabbitMQ connection closed.")

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


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="debug")
