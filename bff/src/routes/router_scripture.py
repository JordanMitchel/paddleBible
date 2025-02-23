from fastapi import APIRouter, Depends, HTTPException

from bff.src.services.ServiceContainer import ServiceContainer, get_services
from shared.src.models.scripture_result import BibleVersion, ResponseModel, VerseRequest

# Instantiate router
router = APIRouter()

# Dependency injection for services using ServiceContainer
@router.get("/BibleBooks")
async def get_bible_books(services: ServiceContainer = Depends(get_services)) -> ResponseModel:
    """Retrieve a list of all Bible books."""
    books = await services.bible_service.get_all_bible_books()
    return books

@router.get("/GetCoordinates/{verse}")
async def get_coordinates_from_verse(
    verse: str,
    services: ServiceContainer = Depends(get_services)
) -> bool:
    """Retrieve locations based on a scripture verse."""
    verse_result = await services.bible_service.get_locations_by_scripture(
        verse, services.producer_service
    )
    if not verse_result:
        raise HTTPException(status_code=404, detail="Locations not found for the given verse.")
    return verse_result

@router.post("/GetVerseData/")
async def get_locations_and_coordinates_from_verse_label(
    request: VerseRequest,
    services: ServiceContainer = Depends(get_services)
) -> ResponseModel:
    """Retrieve scripture data and corresponding coordinates for a specific verse."""
    result = await services.bible_service.get_scripture_and_coordinates(
        request.bible_version,
        request.book_num,
        request.chapter,
        request.verse_num,
        services.producer_service,  # ✅ Use ServiceContainer attributes
        services.consumer_service,
    )
    if not result.success:
        raise HTTPException(status_code=404, detail=result.warnings)
    return result
