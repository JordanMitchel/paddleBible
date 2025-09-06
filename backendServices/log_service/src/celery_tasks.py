from backendServices.domain.src.services.db_connector import get_sync_mongo_client
from celery_app import celery_app  # Import the centralized Celery instance

def get_mongo_client():
    return get_sync_mongo_client()

@celery_app.task
def process_log(log_entry):
    client = get_mongo_client()
    db = client["logs"]
    log_collection = db["log_entries"]

    result = log_collection.insert_one(log_entry)
    client.close()
    return str(result.inserted_id)

LOKI_URL = "http://localhost:3100/loki/api/v1/push"

@celery_app.task
def test_task():
    print("sending hi go jog :)")
