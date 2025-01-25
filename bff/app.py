import asyncio
import uvicorn
from fastapi import FastAPI
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

from bff.src.services.service_bus.consumer_service import ConsumerService
from bff.src.services.service_bus.producer_service import ProducerService
from scripts.background_tasks.start_up_tasks import run_tasks
from bff.src.routes import router_scripture
from shared.src.ServiceBus.rabbitmq import RabbitMQ

if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="PaddleBible", version="1.0.0", debug=True)
app.include_router(router_scripture.router, prefix="/scripture")

rabbitmq = RabbitMQ()

def create_app():
    rabbitmq = RabbitMQ()

    consumer_service = ConsumerService(rabbitmq)
    producer_service = ProducerService(rabbitmq)

    return {
        "rabbitmq": rabbitmq,
        "consumer_service": consumer_service,
        "producer_service": producer_service,
    }


@app.on_event("startup")
async def startup_event():
    print("Starting database seeding...")
    try:
        await run_tasks()
        print("Database seeding completed.")

        # Start consumer after database seeding
        consumer_service = ConsumerService(rabbitmq)
        consumer_service.start_consuming("postprocess_queue")

    except OperationFailure as op_failure:
        print(f"Operation failure message: {str(op_failure)}")

    except ServerSelectionTimeoutError as timeout_error:
        print(f"Timeout error message: {str(timeout_error)}")


# Run the event loop properly
if __name__ == '__main__':
    uvicorn.run("app:app", host="localhost", port=8000, log_level="debug")
