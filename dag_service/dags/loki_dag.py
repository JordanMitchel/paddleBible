# Define the DAG
from datetime import datetime

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

from shared.src.ServiceBus.producer import KombuProducer
from shared.utils.config import TASK_SCHEDULER_ROUTING_KEY

AIRFLOW_MESSAGE =   {
            'task': 'send_logs_to_loki',  # Task name
            'message': 'Fetch logs and send to Loki',
            'timestamp': datetime.utcnow().isoformat(),
        }
def send_logs_to_loki_via_kombu():
    producer = KombuProducer()
    producer.send_message(body=AIRFLOW_MESSAGE,routing_key=TASK_SCHEDULER_ROUTING_KEY)

with DAG(
    'send_logs_to_loki_dag',
    default_args={'owner': 'dag_service', 'retries': 3},
    schedule_interval='*/5 * * * *',  # Run every 5 minutes
    start_date=datetime(2025, 3, 15),
    catchup=False
) as dag:
    # Task to send logs to Loki
    send_logs_task = PythonOperator(
        task_id='send_logs_to_loki',
        python_callable= send_logs_to_loki_via_kombu
    )