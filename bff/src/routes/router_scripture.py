from fastapi import APIRouter, Depends, HTTPException

from shared.src.ServiceBus.consumer_service import ConsumerService
from shared.src.ServiceBus.producer_service import ProducerService
from shared.src.dependencies import get_producer_service, get_consumer_service
from bff.src.services.BibleService import BibleService
from shared.src.models.response import ResponseModel
from shared.src.models.scripture_result import BibleVersion

# Instantiate router
router = APIRouter()


# Dependency injection for services
def get_bible_service() -> BibleService:
    return BibleService()


@router.get("/BibleBooks")
async def get_bible_books(bible_service: BibleService = Depends(get_bible_service)) -> ResponseModel:
    """Retrieve a list of all Bible books."""
    books = await bible_service.get_all_bible_books()
    return books


@router.get("/GetCoordinates/{verse}")
async def get_coordinates_from_verse(
    verse: str,
    bible_service: BibleService = Depends(get_bible_service),
    producer_service: ProducerService = Depends(get_producer_service),
    consumer_service: ConsumerService = Depends(get_consumer_service)
) -> ResponseModel:
    """Retrieve locations based on a scripture verse."""
    verse_result = await bible_service.get_locations_by_scripture(verse, producer_service, consumer_service)
    if not verse_result.success:
        raise HTTPException(status_code=404, detail="Locations not found for the given verse.")
    return verse_result


@router.get("/GetVerseData/{bible_version}/{book_num}/{chapter}/{verse_num}")
async def get_locations_and_coordinates_from_verse_label(
    bible_version: BibleVersion,
    book_num: int,
    chapter: int,
    verse_num: int,
    bible_service: BibleService = Depends(get_bible_service),
    producer_service: ProducerService = Depends(get_producer_service),
    consumer_service: ConsumerService = Depends(get_consumer_service)
) -> ResponseModel:
    """Retrieve scripture data and corresponding coordinates for a specific verse."""
    result = await bible_service.get_scripture_and_coordinates(
        bible_version, book_num, chapter, verse_num, producer_service, consumer_service
    )
    if not result.success:
        raise HTTPException(status_code=404, detail=result.warnings)
    return result
