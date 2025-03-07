import multiprocessing
import os
import subprocess

from log_service.src.LogKombuConsumer import LogKombuConsumer
from log_service.src.celery_app import celery_app  # Import Celery instance


def start_celery_worker():
    """Start Celery worker using subprocess."""
    subprocess.Popen(["celery", "-A", "log_service.src.celery_app", "worker", "--loglevel=info"])


def start_kombu_consumer():
    """Start Kombu consumer for message queue consumption."""
    consumer = LogKombuConsumer()
    consumer.start_consuming()


def start_services():
    """Starts both Celery worker and Kombu consumer in parallel processes."""

    # Create separate processes
    celery_process = multiprocessing.Process(target=start_celery_worker)
    kombu_process = multiprocessing.Process(target=start_kombu_consumer)

    celery_process.start()
    kombu_process.start()

    celery_process.join()
    kombu_process.join()


if __name__ == "__main__":
    start_services()
