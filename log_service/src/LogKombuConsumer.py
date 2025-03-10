import asyncio

from kombu import Connection, Queue
from kombu.mixins import ConsumerProducerMixin

from log_service.src.celery_tasks import process_log
from shared.utils.config import BROKER_URL, LOG_ROUTING_KEY, LOG_QUEUE, LOG_EXCHANGE


class LogKombuConsumer(ConsumerProducerMixin):
    def __init__(self):
        """Initialize Kombu consumer with a queue and message callback."""
        self.connection = Connection(BROKER_URL)
        self.queue = Queue(LOG_QUEUE, LOG_EXCHANGE, routing_key=LOG_ROUTING_KEY)
        self.callback = self.custom_message_callback
        self.result_data = None  # Store extracted data
        self.result_event = asyncio.Event()  # Event for signaling when the result is available

    def get_consumers(self, Consumer, channel):
        """Set up Kombu consumer with the queue and callback."""
        return [Consumer(queues=[self.queue], callbacks=[self.custom_message_callback])]

    def custom_message_callback(self, body, message):
        try:
            print(f"📩 Received message: {body}")  # Debug print
            process_log(body)
            message.ack()
            print("✅ Message acknowledged")
        except Exception as e:
            print(f"❌ Error processing message: {e}")

    def start_consuming(self):
        """Start the consumer and process messages."""

        self.run()  # This is where the actual consuming happens
