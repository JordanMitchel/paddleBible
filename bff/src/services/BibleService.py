import asyncio

from bff.src.services.ServiceBus.BFFKombuConsumer import BFFKombuConsumer
from shared.src.ServiceBus.producer import KombuProducer
from bff.src.services.search.search_bible_books_list import get_all_bible_books
from bff.src.services.search.search_for_location_by_scripture import request_locations_using_scripture
from bff.src.services.search.search_locations import get_coordinates_by_location
from bff.src.services.search.search_scripture import get_scripture_using_book_and_verse
from shared.src.models.scripture_result import ResponseModel


# noinspection PyMethodMayBeStatic


class BibleService:
    async def get_all_bible_books(self) -> ResponseModel:
        """Fetch all Bible books."""
        return await get_all_bible_books()

    async def get_locations_by_scripture(self, verse: str,
                                         producer_service: KombuProducer,
                                         ) -> bool:
        """Fetch locations for a given verse."""
        return await request_locations_using_scripture(verse, producer_service)

    async def get_scripture_and_coordinates(self,
                                            bible_version, book_num, chapter, verse_num,
                                            producer_service: KombuProducer, consumer_service: BFFKombuConsumer
                                            ) -> ResponseModel:
        """Fetch scripture data and calculate coordinates."""
        scripture_result: ResponseModel = await get_scripture_using_book_and_verse(
            bible_version, book_num, chapter, verse_num
        )

        if scripture_result.success:
            scripture = scripture_result.data
            await request_locations_using_scripture(scripture.verse[verse_num], producer_service)

            results = consumer_service.processor
            asyncio.create_task(asyncio.to_thread(consumer_service.run))  # Run the consumer in a background thread

            verse_result = await results.wait_for_message()  # Wait until the message is received
            verse_result.data.scripture = scripture_result

            if len(verse_result.data.locations) > 0:
                list_of_bible_versions = ["ESV Name", "KMZ Name"]
                coordinates = await get_coordinates_by_location(
                    verse_result.data.locations, "ESV Name", list_of_bible_versions
                )
                verse_result.data.locations = coordinates

            response = ResponseModel(success=True, data=verse_result.data, warnings=verse_result.warnings)
            return response

        return ResponseModel(success=False, data={}, warnings="Scripture not found")
