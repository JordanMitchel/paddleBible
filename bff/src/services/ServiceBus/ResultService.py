import asyncio

from bff.src.services.search.search_locations import get_coordinates_by_location
from shared.src.models.scripture_result import ScriptureResponse


# noinspection PyMethodMayBeStatic
class ResultService:
    def __init__(self):
        self.received = False
        self.body: ScriptureResponse = ScriptureResponse(success=False)
        self.event = asyncio.Event()  # Create an asyncio event

    async def process_message(self, message:ScriptureResponse)-> ScriptureResponse:
        if message.data.locations:
            list_of_bible_versions = ["ESV Name", "KMZ Name"]
            coordinates = await get_coordinates_by_location(
                message.data.locations, "ESV Name", list_of_bible_versions
            )
            message.data.locations = coordinates

            return message
        message.warnings = "location not found"
        return message