import uvicorn

from fastapi import FastAPI

from src.models.Response import ResponseModel
from src.search.searchBibleBooksList import get_all_bible_books
from src.models.ScriptureResult import BibleVersion
from src.db.AddBibleToMongo import insert_bible_store
from src.db.AddCoordinatesStore import insert_coordinates_store
from src.search.SearchScripture import get_scripture_using_book_and_verse
from src.search.searchLocations import get_coordinates_by_location
from src.search.searchForLocationByScripture import get_locations_by_scripture
import asyncio

if hasattr(asyncio, "WindowsSelectorEventLoopPolicy"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(debug=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/BibleBooks")
async def get_bible_books() -> ResponseModel:
    books = await get_all_bible_books()
    print(books.data)
    return books

@app.get("/Scripture/{verse}")
async def get_coordinates_from_verse(verse: str) -> ResponseModel:
    verse_result: ResponseModel = await get_locations_by_scripture(verse)
    return verse_result

@app.get("/Scripture/label/{bible_version}/{book_num}/{chapter}/{verse_num}")
async def get_locations_and_coordinates__from_verse_label(bible_version: BibleVersion, book_num: int, chapter: int, verse_num: int) -> ResponseModel:
    scripture_result = await get_scripture_using_book_and_verse(bible_version, book_num, chapter, verse_num)
    if not scripture_result.success:
        verse_result: ResponseModel = await get_locations_by_scripture(scripture_result.verse[verse_num])
        verse_result.data.scripture = scripture_result
        list_of_bible_versions = ["ESV Name", "KMZ Name"]
        if len(verse_result.data.locations) > 0:
            coordinates = await get_coordinates_by_location(verse_result.locations, "ESV Name", list_of_bible_versions)
            verse_result.locations = coordinates

        return verse_result
    else:
        return ResponseModel(success=False,data={},warnings="Scripture not found")



@app.on_event("startup")
async def startup_event():
    print("Starting database seeding...")
    try:
        await run_tasks()  # Await directly for debugging
        print("Database seeding completed.")
    except Exception as e:
        print(f"Error during startup event: {e}")

async def run_tasks():
    try:
        print("Seeding LonLats collection...")
        await insert_coordinates_store("Data/csv/biblicalLonLat2_formatted.csv", "LonLats")
        print("Seeding Bible_ASV collection...")
        await insert_bible_store("Data/json/asv.json", "Bible_ASV")
        print("Seeding completed successfully.")
    except Exception as e:
        print(f"Error during run_tasks: {e}")

# Run the event loop properly
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug")
