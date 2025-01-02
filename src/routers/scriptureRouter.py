from fastapi import APIRouter

from src.models.Response import ResponseModel
from src.models.ScriptureResult import BibleVersion
from src.search.SearchScripture import get_scripture_using_book_and_verse
from src.search.searchBibleBooksList import get_all_bible_books
from src.search.searchForLocationByScripture import get_locations_using_scripture
from src.search.searchLocations import get_coordinates_by_location

router = APIRouter()
@router.get("/BibleBooks")
async def get_bible_books() -> ResponseModel:
    books = await get_all_bible_books()
    print(books.data)
    return books

@router.get("/Scripture/{verse}")
async def get_coordinates_from_verse(verse: str) -> ResponseModel:
    verse_result: ResponseModel = await get_locations_using_scripture(verse)
    return verse_result

@router.get("/Scripture/label/{bible_version}/{book_num}/{chapter}/{verse_num}")
async def get_locations_and_coordinates__from_verse_label(bible_version: BibleVersion, book_num: int, chapter: int, verse_num: int) -> ResponseModel:
    scripture_result = await get_scripture_using_book_and_verse(bible_version, book_num, chapter, verse_num)
    if not scripture_result.success:
        verse_result: ResponseModel = await get_locations_using_scripture(scripture_result.verse[verse_num])
        verse_result.data.scripture = scripture_result
        list_of_bible_versions = ["ESV Name", "KMZ Name"]
        if len(verse_result.data.locations) > 0:
            coordinates = await get_coordinates_by_location(verse_result.locations, "ESV Name", list_of_bible_versions)
            verse_result.locations = coordinates

        return verse_result
    else:
        return ResponseModel(success=False,data={},warnings="Scripture not found")