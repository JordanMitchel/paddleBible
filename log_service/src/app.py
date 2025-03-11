import multiprocessing
import subprocess
import time

from log_service.src.LogKombuConsumer import LogKombuConsumer
from shared.log.logger import get_logger

logger = get_logger()


def start_celery_worker():
    """Start Celery worker using subprocess."""
    print("🚀 Starting Celery worker...")
    subprocess.Popen(["celery", "-A", "log_service.src.celery_app", "worker", "--loglevel=info"])


def start_flower():
    """Start Flower for Celery monitoring."""
    print("🌼 Starting Flower UI...")
    time.sleep(5)  # Give some time for Celery to start
    subprocess.Popen(["celery", "-A", "log_service.src.celery_app", "flower", "--port=5555"])


def start_kombu_consumer():
    """Start Kombu consumer for message queue consumption."""
    print("🚀 Starting Kombu Consumer...")
    consumer = LogKombuConsumer()
    consumer.start_consuming()


def start_services():
    """Starts Celery worker, Flower, and Kombu consumer in parallel processes."""
    celery_process = multiprocessing.Process(target=start_celery_worker)
    flower_process = multiprocessing.Process(target=start_flower)
    kombu_process = multiprocessing.Process(target=start_kombu_consumer)

    celery_process.start()
    kombu_process.start()
    flower_process.start()

    print("✅ Services started successfully!")

    celery_process.join()
    kombu_process.join()
    flower_process.join()


if __name__ == "__main__":
    start_services()
