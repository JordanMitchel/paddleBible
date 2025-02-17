import asyncio
from kombu import Connection, Producer
from shared.src.ServiceBus.kombu_config import BROKER_URL, exchange


class KombuProducer:
    def __init__(self):
        """Initialize Kombu producer with a RabbitMQ connection."""
        print("🔄 Initializing Kombu Producer...")
        self.connection = Connection(BROKER_URL)
        self.connection.ensure_connection(max_retries=5)  # Ensure connection is established
        print("✅ Connection established.")

    def get_channel(self):
        """Get a fresh channel each time to avoid stale channels."""
        return self.connection.channel()

    async def send_message(self, body, routing_key):
        """Send a message to RabbitMQ asynchronously."""
        try:
            await asyncio.to_thread(self._send, body, routing_key)
        except Exception as e:
            print(f"❌ Failed to send message: {e}")

    def _send(self, body, routing_key):
        """Helper method to send a message (Runs in a thread)."""
        with self.get_channel() as channel:
            producer = Producer(channel, exchange=exchange)
            producer.publish(body, routing_key=routing_key)
            print(f"✅ Sent: {body} to {routing_key}")

    async def stop(self):
        """Gracefully close the connection asynchronously."""
        if self.connection:
            await asyncio.to_thread(self.connection.release)
            print("🛑 Kombu producer connection closed.")
