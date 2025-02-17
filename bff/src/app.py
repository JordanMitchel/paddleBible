import asyncio
import uvicorn
from fastapi import FastAPI
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure
from scripts.background_tasks.start_up_tasks import run_tasks
from bff.src.routes import router_scripture

if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="PaddleBible", version="1.0.0", debug=True)
app.include_router(router_scripture.router, prefix="/scripture")



@app.on_event("startup")
async def startup_event():
    print("Starting database seeding...")
    try:
        await run_tasks()
        print("Database seeding completed.")

    except OperationFailure as op_failure:
        print(f"Operation failure message: {str(op_failure)}")

    except ServerSelectionTimeoutError as timeout_error:
        print(f"Timeout error message: {str(timeout_error)}")


# Run the event loop properly
# if __name__ == '__main__':
#     uvicorn.run("app:app", host="localhost", port=8002, log_level="debug")
if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="debug")
