import multiprocessing
import subprocess

from log_service.src.LogKombuConsumer import LogKombuConsumer
from shared.log.logger import get_logger

logger = get_logger()


def start_celery_worker():
    """Start Celery worker using subprocess."""
    print("🚀 Starting Celery worker...")
    subprocess.Popen(["celery", "-A", "log_service.src.celery_app", "worker", "--loglevel=info"])


def start_kombu_consumer():
    """Start Kombu consumer for message queue consumption."""
    print("🚀 Starting Kombu Consumer...")
    consumer = LogKombuConsumer()
    consumer.start_consuming()


def start_services():
    """Starts both Celery worker and Kombu consumer in parallel processes."""
    celery_process = multiprocessing.Process(target=start_celery_worker)
    kombu_process = multiprocessing.Process(target=start_kombu_consumer)

    celery_process.start()
    kombu_process.start()

    print("✅ Services started successfully!")

    celery_process.join()
    kombu_process.join()


if __name__ == "__main__":
    start_services()
