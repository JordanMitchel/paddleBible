from shared.src.dependencies import ConsumerService
from shared.src.ServiceBus.RabbitMQ import RabbitMQ
from src.services.ProcessService import ProcessService
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    rabbitmq = RabbitMQ()
    consumer_service = ConsumerService(rabbitmq)
    # Start consuming messages
    await consumer_service.start_consuming("your_queue_name", process_message)

async def process_message(message):

    # Process the message with ProcessService
    process_service = ProcessService()
    response = await process_service.process_text(message)
    # # Handle the response as needed
    print(response)
