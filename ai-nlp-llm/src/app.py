import asyncio
import uvicorn
from fastapi import FastAPI
from kombu import Connection
from services.service_bus.ProcessService import ProcessService
from shared.src.ServiceBus.consumer import KombuConsumer
from shared.src.ServiceBus.kombu_config import BROKER_URL, ai_consuming_bff_requests
from shared.src.ServiceBus.dependencies import get_producer_service, get_consumer_factory
from shared.src.ServiceBus.producer import KombuProducer

app = FastAPI()

# Global references for Kombu services
ai_producer_service: KombuProducer
ai_consumer_service: KombuConsumer


@app.on_event("startup")
async def startup_event():
    """Setup Kombu consumer and producer on startup."""
    global ai_producer_service, ai_consumer_service

    try:

        print("✅ Connected to RabbitMQ")

        # Initialize Producer
        ai_producer_service = get_producer_service()
        # Initialize Consumer with callback

        process_service = ProcessService()
        ai_consumer_service = get_consumer_factory(ai_consuming_bff_requests)()
        ai_consumer_service.callback = process_service.message_callback

        # Start consumer in the background
        asyncio.create_task(ai_consumer_service.start())
        print(f"✅ Kombu consumer listening on queue: {ai_consuming_bff_requests.name}")

    except Exception as e:
        print(f"❌ Failed to setup Kombu services: {e}")


@app.on_event("shutdown")
async def shutdown_event():
    """Gracefully shutdown Kombu producer & consumer."""
    global ai_consumer_service, ai_producer_service

    if ai_consumer_service:
        await ai_consumer_service.stop()
        print("🛑 Kombu consumer stopped,  RabbitMQ (Kombu) connection closed.")
        await ai_producer_service.stop()
        print("🛑 Kombu producer stopped,  RabbitMQ (Kombu) connection closed.")


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
