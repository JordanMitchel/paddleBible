from shared.src.ServiceBus.consumer_service import ConsumerService
from shared.src.ServiceBus.producer_service import ProducerService
from shared.src.models.response import ResponseModel
from shared.src.models.scripture_result import BibleVersion
from bff.src.services.search.search_bible_books_list import get_all_bible_books
from bff.src.services.search.search_for_location_by_scripture import get_locations_using_scripture
from bff.src.services.search.search_locations import get_coordinates_by_location
from bff.src.services.search.search_scripture import get_scripture_using_book_and_verse


class BibleService:
    async def get_all_bible_books(self) -> ResponseModel:
        """Fetch all Bible books."""
        return await get_all_bible_books()

    async def get_locations_by_scripture(self, verse: str,
                 producer_service: ProducerService,
                 consumer_service: ConsumerService) -> ResponseModel:
        """Fetch locations for a given verse."""
        return await get_locations_using_scripture(verse, producer_service, consumer_service)

    async def get_scripture_and_coordinates(
        self, bible_version: BibleVersion, book_num: int, chapter: int, verse_num: int,
            producer_service: ProducerService, consumer_service: ConsumerService
    ) -> ResponseModel:
        """Fetch scripture data and calculate coordinates."""
        scripture_result = await get_scripture_using_book_and_verse(
            bible_version, book_num, chapter, verse_num
        )
        if not scripture_result.success:
            verse_result = await get_locations_using_scripture(scripture_result.verse[verse_num], producer_service, consumer_service)
            verse_result.data.scripture = scripture_result

            if len(verse_result.data.locations) > 0:
                list_of_bible_versions = ["ESV Name", "KMZ Name"]
                coordinates = await get_coordinates_by_location(
                    verse_result.locations, "ESV Name", list_of_bible_versions
                )
                verse_result.locations = coordinates

            return verse_result

        return ResponseModel(success=False, data={}, warnings="Scripture not found")
