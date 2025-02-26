import asyncio
import uvicorn
from fastapi import FastAPI
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure
from fastapi.websockets import WebSocket, WebSocketDisconnect

from bff.src.services.ServiceBus.BFFKombuConsumer import BFFKombuConsumer
from bff.src.services.ServiceContainer import ServiceContainer
from scripts.background_tasks.start_up_tasks import run_tasks
from bff.src.routes import router_scripture, router_ws

if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="PaddleBible", version="1.0.0", debug=True)

service_container = None
app.include_router(router_scripture.router, prefix="/scripture")
app.include_router(router_ws.ws_router, prefix="/ws-test")


@app.on_event("startup")
async def startup_event():
    global service_container

    print("Starting database seeding...")
    try:
        await run_tasks()
        print("Database seeding completed.")

        print("✅ Connected to RabbitMQ")
        bff_consumer_service = BFFKombuConsumer()
        app.state.bff_consumer_service = bff_consumer_service

        # ✅ Start Kombu consumer as a background task
        loop = asyncio.get_event_loop()
        loop.create_task(asyncio.to_thread(bff_consumer_service.run))


        print(f"✅ Kombu consumer listening on queue: {bff_consumer_service.queue.name}")
    except Exception as e:
        print(f"❌ Error during startup: {str(e)}")



if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="debug")