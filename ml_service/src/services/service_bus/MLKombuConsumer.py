import asyncio

from kombu import Connection, Queue
from kombu.mixins import ConsumerProducerMixin

from ml_service.src.services.service_bus.ProcessService import ProcessService
from shared.src.ServiceBus.producer import KombuProducer
from shared.src.models.scripture_result import ScriptureRequest, ScriptureResponse
from shared.utils.config import BROKER_URL, EXCHANGE


class MLKombuConsumer(ConsumerProducerMixin):
    def __init__(self):
        """Initialize Kombu consumer with a queue and message callback."""
        self.connection = Connection(BROKER_URL)
        self.queue = Queue("ai_consuming.bff.requests", EXCHANGE, routing_key="ai_consuming.bff.requests")
        self.process_service = ProcessService()

        # Initialize a producer for sending processed results
        self.publisher = KombuProducer()

    def get_consumers(self, Consumer, channel):
        """Set up Kombu consumer with the queue and callback."""
        return [Consumer(queues=[self.queue], callbacks=[self.custom_message_callback])]

    def custom_message_callback(self, body, message):
        """Process messages asynchronously inside Kombu's sync callback."""
        print(f"📩 Custom Consumer Received: {body}")

        # Process the message and produce the result
        result = asyncio.run(self._async_process_message(ScriptureRequest(**body)))
        self.publish_result(result)
        message.ack()  # Acknowledge the message

    async def _async_process_message(self, body:ScriptureRequest):
        """Async wrapper to run the processing service in an event loop."""
        result:ScriptureResponse = await self.process_service.process_text(body)
        print("✅ Processed message successfully.")
        return result  # Return processed result

    def publish_result(self, result):
        """Send processed result to another queue."""
        routing_key = "bff_consuming.ai.results"
        output_result = result.model_dump()
        print(f"🚀 Publishing result: {output_result} to {routing_key}")
        asyncio.run(self.publisher.send_message(output_result, routing_key=routing_key))
