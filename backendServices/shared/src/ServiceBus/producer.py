import asyncio

from kombu import Connection, Producer
from kombu.exceptions import KombuError

from backendServices.shared.utils.config import BROKER_URL, EXCHANGE


class KombuProducer:
    def __init__(self):
        """Initialize Kombu producer with a persistent connection and producer."""
        try:
            print("🔄 Initializing Kombu Producer...")
            self.connection = Connection(BROKER_URL)
            self.connection.ensure_connection(max_retries=5)
            self.channel = self.connection.channel()  # ✅ Get a persistent channel
            self.producer = Producer(self.channel, exchange=EXCHANGE)  # ✅ Persistent producer
            print("✅ Kombu Producer initialized successfully.")
        except KombuError as e:
            print(f"❌ Failed to initialize Kombu Producer: {e}")
            self.connection = None
            self.producer = None

    async def send_message(self, body, routing_key):
        """Send a message to RabbitMQ asynchronously."""
        if not self.producer:
            print("❌ Cannot send message: Producer not initialized.")
            return

        try:
            print(f"📤 Sending message to {routing_key}: {body}")
            await asyncio.to_thread(self._send, body, routing_key)  # Run sync method in thread
        except Exception as e:
            print(f"❌ Failed to send message: {e}")

    def _send(self, body, routing_key):
        """Helper method to send a message (runs in a separate thread)."""
        try:
            self.producer.publish(body, routing_key=routing_key)
            print(f"✅ Successfully sent message to {routing_key}")
        except KombuError as e:
            print(f"❌ Kombu publish failed: {e}")

    async def stop(self):
        """Gracefully close the connection asynchronously."""
        if self.connection:
            await asyncio.to_thread(self.connection.release)  # Release the connection in a thread
            print("🛑 Kombu producer connection closed.")

    def get_channel(self):
        return self.channel
