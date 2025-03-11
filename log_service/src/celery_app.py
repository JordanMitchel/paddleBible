from celery import Celery

from shared.utils.config import BROKER_URL

celery_app = Celery("log_service", broker=BROKER_URL,
                    backend="mongodb://root:rootPassword@mongodb:27018/celery_results")

# If needed, you can configure Celery further
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    enable_utc=True,
)
