import asyncio
import uvicorn
from fastapi import FastAPI
from src.background_tasks.start_up_tasks import run_tasks
from src.routers import  router_scripture
from pymongo.errors import  ServerSelectionTimeoutError, OperationFailure


if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="PaddleBible", version="1.0.0", debug=True)

app.include_router(router_scripture.router, prefix="/scripture")

@app.on_event("startup")
async def startup_event():
    print("Starting database seeding...")
    try:
        await run_tasks()  # Await directly for debugging
        print("Database seeding completed.")

    except OperationFailure as op_failure:
        # Handle errors specific to MongoDB operations
        print(f"Operation failure message: {str(op_failure)}")

    except ServerSelectionTimeoutError as timeout_error:
        # Handle server timeout errors
        print(f"Timeout error message: {str(timeout_error)}")

# Run the event loop properly
if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, log_level="debug")
