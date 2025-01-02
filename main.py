import uvicorn
from fastapi import FastAPI
from src.BackgroundTasks.startUpTasks import run_tasks
from src.routers import  scriptureRouter
import asyncio

if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="PaddleBible", version="1.0.0", debug=True)

app.include_router(scriptureRouter.router)
@app.on_event("startup")
async def startup_event():
    print("Starting database seeding...")
    try:
        await run_tasks()  # Await directly for debugging
        print("Database seeding completed.")
    except Exception as e:
        print(f"Error during startup event: {e}")


# Run the event loop properly
if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, log_level="debug")
