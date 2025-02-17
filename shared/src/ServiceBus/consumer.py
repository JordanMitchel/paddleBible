import asyncio
from kombu import Connection, Consumer
from shared.src.ServiceBus.kombu_config import BROKER_URL


class KombuConsumer:
    def __init__(self, queue, callback):
        self.connection = Connection(BROKER_URL)
        self.channel = self.connection.channel()
        self.consumer = Consumer(self.channel, queue, callbacks=[callback])
        self.is_consuming = False  # Flag to track if the consumer is running
        self.consumer_task = None  # Task for async consumption

    async def start(self):
        """Start consuming messages asynchronously"""
        if self.is_consuming:
            print("Consumer is already running.")
            return

        self.is_consuming = True

        async def consume():
            """Async wrapper to consume messages in a non-blocking way"""
            with self.consumer:
                print(f"✅ Consumer started for queue: {self.consumer.queues}")
                while self.is_consuming:
                    await asyncio.to_thread(self.connection.drain_events)  # Run drain_events in a thread

        self.consumer_task = asyncio.create_task(consume())

    async def stop(self):
        """Stop consuming messages asynchronously"""
        if not self.is_consuming:
            print("Consumer is not running.")
            return

        self.is_consuming = False
        if self.consumer_task:
            await self.consumer_task  # Ensure the task stops cleanly
            self.consumer_task = None

        await asyncio.to_thread(self.connection.release)  # Release connection in a thread
        print("🛑 Consumer stopped.")

