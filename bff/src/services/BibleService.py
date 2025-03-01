
from bff.src.services.search.search_bible_books_list import get_all_bible_books
from bff.src.services.search.search_for_location_by_scripture import request_locations_using_scripture
from bff.src.services.search.search_scripture import get_scripture_using_book_and_verse, get_scripture_using_verse
from shared.src.ServiceBus.producer import KombuProducer
from shared.src.models.scripture_result import ResponseModel, ScriptureRequest


class BibleService:
    """Service to manage Bible-related queries."""

    def __init__(self, producer: KombuProducer):
        """Initialize BibleService with explicit dependencies."""
        self.producer = producer

    async def get_all_bible_books(self) -> ResponseModel:
        """Fetch all Bible books."""
        return await get_all_bible_books()

    async def get_locations_by_scripture(self, clientId,bible_version,  verse: str) -> bool:
        """Fetch locations for a given verse."""
        request: ScriptureRequest = await get_scripture_using_verse(clientId, bible_version, verse)
        return await request_locations_using_scripture(request, self.producer)

    async def get_scripture_and_coordinates(self, clientId, bible_version, book_num, chapter, verse_num) \
            -> ResponseModel:
        """Fetch scripture data and calculate coordinates."""
        scripture_result: ScriptureRequest = await get_scripture_using_book_and_verse(
            clientId, bible_version, book_num, chapter, verse_num
        )

        if not scripture_result.data:
            return ResponseModel(success=False, data={}, warnings="Scripture not found")

        scripture = scripture_result.data
        request = ScriptureRequest(clientId=clientId, data=scripture)
        await request_locations_using_scripture(request, self.producer)


        return ResponseModel(success=True, data=request, warnings="")
