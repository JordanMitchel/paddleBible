import multiprocessing
import subprocess
import time
import signal
import sys
from loguru import logger
from log_service.src.LogKombuConsumer import LogKombuConsumer

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

def start_airflow_scheduler():
    """Start Airflow scheduler."""
    logger.info("🌾 Starting Airflow scheduler...")
    process = subprocess.Popen(
        ["dag_service", "scheduler"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    process.wait()

def start_airflow_webserver():
    """Start Airflow web server."""
    logger.info("🌐 Starting Airflow web server...")
    process = subprocess.Popen(
        ["dag_service", "webserver", "--port", "8080"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
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

    processes["celery_worker"] = multiprocessing.Process(target=start_celery_worker)
    processes["celery_worker"].start()

    # Start Airflow Scheduler and Web Server
    processes["airflow_scheduler"] = multiprocessing.Process(target=start_airflow_scheduler)
    processes["airflow_scheduler"].start()

    processes["airflow_webserver"] = multiprocessing.Process(target=start_airflow_webserver)
    processes["airflow_webserver"].start()

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
