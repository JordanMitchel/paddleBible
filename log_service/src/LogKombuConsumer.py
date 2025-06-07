import asyncio

from kombu import Connection, Queue
from kombu.mixins import ConsumerProducerMixin
from loguru import logger

from log_service.src.celery_tasks import process_log
from log_service.src.metrics import info_counter, warn_counter, error_counter
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
            logger.info(f"📩 Received message: {body}")
            process_log(body)

            # Extract log level, source, and environment
            level = body.get("level", "").upper()
            service = body.get("service", "unknown")

            # Update appropriate counter with labels
            if level == "INFO":
                info_counter.labels(service=service).inc()
            elif level == "WARNING":
                warn_counter.labels(source=service).inc()
            elif level == "ERROR":
                error_counter.labels(source=service).inc()

            message.ack()
            logger.info("✅ Message acknowledged")
        except Exception as e:
            logger.error(f"❌ Error processing message: {e}")

    def start_consuming(self):
        """Start the consumer and process messages."""

        self.run()  # This is where the actual consuming happens
