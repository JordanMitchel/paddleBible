import uvicorn
import asyncio

from fastapi import FastAPI, Response
from watchfiles import awatch

from Domain.searchBibleBooksList import get_all_bible_books
from Models.ScriptureResult import BibleStructure, bibleVersion
from Domain.AddBibleToMongo import insert_bible_store
from Domain.AddCoordinatesStore import insert_coordinates_store
from Domain.SearchScripture import search_scripture
from Domain.searchLocations import search_coordinates
from DirectAnalysis.searchForLocationByScripture import search_for_location_by_scripture

app = FastAPI(debug=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/BibleBooks")
async def get_bible_books():
    books = await get_all_bible_books()
    print(books)
    return books

@app.get("/Scripture/{verse}")
async def get_coordinates_from_verse(verse: str) -> BibleStructure:
    verse_result: BibleStructure = await search_for_location_by_scripture(verse)
    return verse_result

@app.get("/Scripture/label/{bible_version}/{book_num}/{chapter}/{verse_num}")
async def get_coordinates_from_verse_label(bible_version: bibleVersion, book_num: int, chapter: int, verse_num: int) -> BibleStructure:
    scripture = await search_scripture(bible_version, book_num, chapter, verse_num)
    verse_result: BibleStructure = await search_for_location_by_scripture(scripture.verse[verse_num])

    list_of_bible_versions = ["ESV Name", "KMZ Name"]
    coordinates = await search_coordinates(verse_result.locations, "ESV Name", list_of_bible_versions)
    verse_result.locations = coordinates
    verse_result.scripture = scripture

    return verse_result

# FastAPI Startup Event
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
        await insert_coordinates_store("./Data/biblicalLonLat2_formatted.csv", "LonLats")
        print("Seeding Bible_ASV collection...")
        await insert_bible_store("./Data/asv.json", "Bible_ASV")
        print("Seeding completed successfully.")
    except Exception as e:
        print(f"Error during run_tasks: {e}")
# # Start the FastAPI app using uvicorn, and await the background tasks
# async def main():
#     # Run the background tasks before starting the FastAPI server
#     await run_tasks()
#     # Start the FastAPI app with Uvicorn
#     config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="debug")
#     server = uvicorn.Server(config)
#     await server.serve()

# Run the event loop properly
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug")
