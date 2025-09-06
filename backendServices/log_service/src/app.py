import multiprocessing
import subprocess
import signal
import sys
from loguru import logger
from LogKombuConsumer import LogKombuConsumer

# Configure Loguru for local logging (Separate from MongoDB logs)
logger.remove()  # Remove default Loguru handler
logger.add(sys.stdout, format="{time} | {level} | {message}", level="INFO")

def start_celery_worker():
    """Start Celery worker using subprocess."""
    logger.info("🚀 Starting Celery worker...")
    process = subprocess.Popen(
        ["celery", "-A", "log_service.src.celery_app", "worker", "--loglevel=info"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    process.wait()


def start_fastapi_server():
    """Start FastAPI server from api.py."""
    logger.info("🌀 Starting FastAPI server...")
    process = subprocess.Popen(
        ["uvicorn", "log_service.src.api:app", "--host", "0.0.0.0", "--port", "5555"]
    )

    process.wait()


def start_kombu_consumer():
    """Start Kombu consumer for message queue consumption."""
    logger.info("🚀 Starting Kombu Consumer...")
    consumer = LogKombuConsumer()
    consumer.start_consuming()

def start_services():
    """Starts Celery Worker, Airflow Scheduler, Airflow Webserver, and Kombu Consumer in parallel processes."""
    processes = {}

    processes["fastapi_server"] = multiprocessing.Process(target=start_fastapi_server)
    processes["fastapi_server"].start()

    processes["celery_worker"] = multiprocessing.Process(target=start_celery_worker)
    processes["celery_worker"].start()

    processes["kombu_consumer"] = multiprocessing.Process(target=start_kombu_consumer)
    processes["kombu_consumer"].start()

    logger.success("✅ Services started successfully!")

    def shutdown_handler(signum, frame):
        """Gracefully stop all processes on exit."""
        logger.warning("⚠️ Shutting down all services...")
        for name, process in processes.items():
            if process.is_alive():
                logger.warning(f"🔴 Terminating {name}...")
                process.terminate()
                process.join()
        logger.success("✅ All services shut down cleanly.")
        sys.exit(0)

    # Handle termination signals (Ctrl+C or Docker stop)
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)

    for process in processes.values():
        process.join()

if __name__ == "__main__":
    start_services()
