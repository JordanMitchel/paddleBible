import asyncio

from kombu import Connection, Queue
from kombu.mixins import ConsumerProducerMixin

from bff.src.services.ServiceBus.ResultService import ResultService
from shared.src.models.scripture_result import ScriptureResponse
from shared.utils.config import BROKER_URL, EXCHANGE


class BFFKombuConsumer(ConsumerProducerMixin):
    def __init__(self):
        """Initialize Kombu consumer with a queue and message callback."""
        self.connection = Connection(BROKER_URL)
        self.queue = Queue("bff_consuming.ai.results", EXCHANGE, routing_key="bff_consuming.ai.results")
        self.callback = self.custom_message_callback
        self.result_data = None  # Store extracted data
        self.result_event = asyncio.Event()  # Event for signaling when the result is available
        self.processor = ResultService()

    def get_consumers(self, Consumer, channel):
        """Set up Kombu consumer with the queue and callback."""
        print("Setting up consumer for queue: bff_consuming.ai.results")
        return [Consumer(queues=[self.queue], callbacks=[self.custom_message_callback])]

    def custom_message_callback(self, body, message):
        """Custom processing logic for messages and storing result_data."""
        print(f"📩 Custom Consumer Received: {body}")
        asyncio.run(self._async_process_message(ScriptureResponse(**body)))

        # self.result_data = ResponseModel.from_json(body)  # Store received message in result_data
        message.ack()  # Acknowledge the message

    def start_consuming(self):
        """Start the consumer and process messages."""
        try:
            print("Starting to consume messages...")
            self.run()  # This is where the actual consuming happens
            print("Finished consuming messages.")
        except Exception as e:
            print(f"Error while consuming messages: {str(e)}")

    async def _async_process_message(self, body):
        """Async wrapper to run the processing service in an event loop."""
        result = await self.processor.process_message(body)
        print("✅ Processed message successfully.")
        return result  # Return processed result
