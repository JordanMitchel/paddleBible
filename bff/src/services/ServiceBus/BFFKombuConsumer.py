import asyncio
from kombu import Connection, Queue
from kombu.mixins import ConsumerProducerMixin

from bff.src.routes.router_ws import connected_clients
from bff.src.services.ServiceBus.ResultService import ResultService
from shared.src.models.scripture_result import ScriptureResponse
from shared.utils.config import BROKER_URL, EXCHANGE


class BFFKombuConsumer(ConsumerProducerMixin):
    def __init__(self):
        """Initialize Kombu consumer with a queue and message callback."""
        self.connection = Connection(BROKER_URL)
        self.queue = Queue(
            "bff_consuming.ai.results",
            exchange=EXCHANGE,
            routing_key="bff_consuming.ai.results",
            durable=True  # Ensure queue is persistent
        )
        self.process_service = ResultService()
        self.loop = asyncio.get_event_loop()  # Get the FastAPI event loop

    def get_consumers(self, Consumer, channel):
        """Set up Kombu consumer with the queue and callback."""
        return [Consumer(queues=[self.queue], callbacks=[self.custom_message_callback])]

    def custom_message_callback(self, body, message):
        """Process incoming messages from the queue."""
        print(f"📩 Custom Consumer Received: {body}")
        scripture_response = ScriptureResponse(**body)

        # Process the message asynchronously
        future = asyncio.run_coroutine_threadsafe(
            self._async_process_and_push(scripture_response), self.loop
        )
        future.result()  # Ensure it runs properly without blocking

        message.ack()  # Acknowledge the message

    async def _async_process_and_push(self, scripture_response: ScriptureResponse):
        """Process message and push to WebSocket."""
        try:
            result = await self.process_service.process_message(scripture_response)
            print("✅ Processed message successfully.")

            # Extract client_id dynamically instead of hardcoding "client1"
            client_id = "client-1"
            # client_id = scripture_response.client_id
            await self._send_to_websocket(result.model_dump(), client_id)
        except Exception as e:
            print(f"❌ Error processing message: {str(e)}")

    async def _send_to_websocket(self, data, client_id):
        """Send processed result to WebSocket clients."""
        websocket = connected_clients.get(client_id)

        if websocket:
            try:
                await websocket.send_text(f"Result: {data}")
                print(f"✅ Sent result to client {client_id}: {data}")
            except Exception as e:
                print(f"❌ Error sending message to {client_id}: {str(e)}")
                connected_clients.pop(client_id, None)  # Remove if connection is broken
        else:
            print(f"❌ Client {client_id} not connected. Unable to send result.")
