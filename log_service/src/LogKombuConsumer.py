import asyncio

from kombu import Connection, Queue
from kombu.mixins import ConsumerProducerMixin

from log_service.src.celery_tasks import process_log
from shared.src.models.scripture_result import LogResponse
from shared.utils.config import BROKER_URL, EXCHANGE, LOG_ROUTING_KEY


class LogKombuConsumer(ConsumerProducerMixin):
    def __init__(self):
        """Initialize Kombu consumer with a queue and message callback."""
        self.connection = Connection(BROKER_URL)
        self.queue = Queue("log_consuming.all_results", EXCHANGE, routing_key=LOG_ROUTING_KEY)
        self.callback = self.custom_message_callback
        self.result_data = None  # Store extracted data
        self.result_event = asyncio.Event()  # Event for signaling when the result is available

    def get_consumers(self, Consumer, channel):
        """Set up Kombu consumer with the queue and callback."""
        print(f"Setting up consumer for queue: {LOG_ROUTING_KEY}")
        return [Consumer(queues=[self.queue], callbacks=[self.custom_message_callback])]

    def custom_message_callback(self, body, message):
        """Custom processing logic for messages and storing result_data."""
        print(f"📩 Custom Consumer Received: {body}")
        self._process_message(body)

        message.ack()  # Acknowledge the message

    def start_consuming(self):
        """Start the consumer and process messages."""
        try:
            print("Starting to consume messages...")
            self.run()  # This is where the actual consuming happens
            print("Finished consuming messages.")
        except ValueError as e:
            print(f"Value error: {str(e)}")
        except TimeoutError as e:
            print(f"Timeout error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error while consuming messages: {str(e)}")

    def _process_message(self, body):
        """Async wrapper to run the processing service in an event loop."""
        process_log(body)
        print("✅ Processed message successfully.")
        # Convert `LogResponse` object to dictionary before sending to Celery
