# Function to send logs to Loki
import json
from datetime import datetime

import requests

from domain.src.services.db_connector import get_mongo_client
from log_service.src.celery_tasks import LOKI_URL


def send_logs_to_loki():
    client = get_mongo_client()
    db = client["logs"]
    log_collection = db["log_entries"]
    logs = log_collection.find({'sent_to_loki': False})  # Fetch logs that are not yet sent to Loki
    for log in logs:
        log_message = log['message']
        log_level = log['level']
        timestamp = log['timestamp']

        # Prepare Loki log format (nanosecond timestamp required)
        log_entry = {
            'streams': [
                {
                    'stream': {
                        'level': log_level
                    },
                    'values': [
                        [str(int(datetime.timestamp(timestamp) * 1000000000)), log_message]  # Loki expects nanosecond timestamp
                    ]
                }
            ]
        }

        # Send log entry to Loki directly
        response = requests.post(LOKI_URL, data=json.dumps(log_entry), headers={'Content-Type': 'application/json'})

        if response.status_code == 204:  # Loki accepted the log
            # Mark log as sent to Loki
            log_collection.update_one({'_id': log['_id']}, {'$set': {'sent_to_loki': True}})
        else:
            print(f"Failed to send log {log['_id']} to Loki. Status code: {response.status_code}")
