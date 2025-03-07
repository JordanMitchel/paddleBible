from celery import Celery
from shared.utils.config import BROKER_URL

celery_app = Celery("log_service", broker=BROKER_URL)

# If needed, you can configure Celery further
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_backend="rpc://",  # Or use MongoDB, Redis, or other backends
)
