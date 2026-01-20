from fastapi import APIRouter, Depends, HTTPException, Query

from backendServices.shared.log.logger import get_logger

from backendServices.bff.src.services import BibleService
from backendServices.bff.src.services.ProducerServiceContainer import get_bible_service
from backendServices.shared.src.models.scripture_result import VerseRequest, ResponseModel

# Instantiate router
router = APIRouter()
logger = get_logger()


@router.get("/BibleBooks")
async def get_bible_books(bible_service: BibleService = Depends(get_bible_service)) -> ResponseModel:
    """Retrieve a list of all Bible books."""
    logger.info("querying bible books")
    return await bible_service.get_all_bible_books()

@router.get("/Chapters", response_model=ResponseModel)
async def get_chapters_by_book(
        book: int = Query(..., description="Book number to fetch chapter for"),
        bible_service: BibleService = Depends(get_bible_service)) -> ResponseModel:
    logger.info(f"querying chapters for book: {book}")
    return await bible_service.get_chapters_by_book(book)

@router.get("/VersesForChapter", response_model=ResponseModel)
async def get_all_verses_for_chapter_and_book(
        book: int = Query(..., description="Book number to fetch chapter for"),
        chapter: int = Query(..., description="Chapter number to fetch verses for"),
        bible_serivce: BibleService = Depends(get_bible_service)) -> ResponseModel:
    logger.info(f"querying verse by chapter and book {book}:{chapter}")
    return await bible_serivce.get_verses_by_chapter_and_book(book,chapter)



@router.get("/GetCoordinates/{verse}")
async def get_coordinates_from_verse(
        verse: str,
        services: BibleService = Depends(get_bible_service)
) -> bool:
    """Retrieve locations based on a scripture verse."""
    logger.info(f"get coordinattes for verse {verse}")
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
    logger.info("verse returned successful")
    return result
