from fastapi import APIRouter, Depends, HTTPException

from bff.src.services.BibleService import BibleService
from bff.src.services.ProducerServiceContainer import get_bible_service
from shared.src.models.scripture_result import ResponseModel, VerseRequest

# Instantiate router
router = APIRouter()


@router.get("/BibleBooks")
async def get_bible_books(bible_service: BibleService = Depends(get_bible_service)) -> ResponseModel:
    """Retrieve a list of all Bible books."""
    return await bible_service.get_all_bible_books()


@router.get("/GetCoordinates/{verse}")
async def get_coordinates_from_verse(
        verse: str,
        services: BibleService = Depends(get_bible_service)
) -> bool:
    """Retrieve locations based on a scripture verse."""
    verse_result = await services.get_locations_by_scripture(
        verse
    )
    if not verse_result:
        raise HTTPException(status_code=404, detail="Locations not found for the given verse.")
    return verse_result


@router.post("/GetVerseData/")
async def get_locations_and_coordinates_from_verse_label(
        client_id: str,
        request: VerseRequest,
        services: BibleService = Depends(get_bible_service)
) -> ResponseModel:
    """Retrieve scripture data and corresponding coordinates for a specific verse."""
    result = await services.get_scripture_and_coordinates(
        client_id,
        request.bible_version,
        request.book_num,
        request.chapter,
        request.verse_num,
    )
    if not result.success:
        raise HTTPException(status_code=404, detail=result.warnings)
    return result
