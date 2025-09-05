from datetime import datetime

from kombu import Connection, Queue, Producer
from pytz import  UTC
from backendServices.shared.utils.config import BROKER_URL, LOG_QUEUE, LOG_EXCHANGE, LOG_ROUTING_KEY


class LogProducer:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.kombu_producer = None
        self.exchange = LOG_EXCHANGE
        self.queue = Queue(LOG_QUEUE, exchange=self.exchange, routing_key=LOG_ROUTING_KEY)

    async def setup(self):
        """Initializes the Kombu connection and producer."""
        if self.kombu_producer is None:  # Avoid re-initializing
            try:
                self.connection = Connection(BROKER_URL)
                self.connection.ensure_connection(max_retries=3)
                self.channel = self.connection.channel()
                self.kombu_producer = Producer(self.channel, exchange=self.exchange, routing_key=LOG_ROUTING_KEY)
                print("✅ LogProducer setup complete")
            except Exception as e:
                print(f"❌ Failed to initialize LogProducer: {e}")

    async def send_log(self, service, level, message):
        """Sends a log message to RabbitMQ."""
        if self.kombu_producer is None:
            await self.setup()  # Ensure setup is completed before sending logs

        log_message = {"service": service,
                       "level": level,
                       "message": message,
                       "timestamp":datetime.now(UTC)
                       }
        try:
            self.kombu_producer.publish(log_message, exchange=self.exchange.name, routing_key=LOG_ROUTING_KEY,
                                        serializer="json")
            print(f"📤 Log sent: {log_message}")
        except Exception as e:
            print(f"❌ Failed to send log: {e}")
