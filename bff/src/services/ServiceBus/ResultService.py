import asyncio

from shared.src.models.scripture_result import ScriptureResponse


class ResultService:
    def __init__(self):
        self.received = False
        self.body: ScriptureResponse = ScriptureResponse(success=False)
        self.event = asyncio.Event()  # Create an asyncio event

    def set_message(self, body):
        self.body = body
        self.received = True
        self.event.set()  # Signal that the message has been received

    async def wait_for_message(self) -> ScriptureResponse:
        """Wait until a message is received."""
        await self.event.wait()  # Blocks until event is set
        return self.body

    async def process_message(self, body: ScriptureResponse):
        self.set_message(body)
        print(f"✅ Result data stored: {self.body}")
