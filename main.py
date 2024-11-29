# This is a sample Python script.

import uvicorn

from Domain.searchBibleBooksList import get_all_bible_books
from Models.ScriptureResult import BibleStructure, bibleVersion
from fastapi import FastAPI, Response

from Domain.AddBibleToMongo import insert_bible_to_mongo
from Domain.AddCoordinatesStore import insert_coordinates_store
from Domain.SearchScripture import search_scripture
from Domain.searchLocations import search_coordinates
from DirectAnalysis.searchForLocationByScripture import search_for_location_by_scripture

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/BibleBooks")
async def get_bible_books():
    return get_all_bible_books()
@app.get("/Scripture/{verse}")
async def get_coordinates_from_verse(verse: str) -> BibleStructure:
    verse_result: BibleStructure = search_for_location_by_scripture(verse)
    return verse_result


@app.get("/Scripture/label/{bible_version, book_number,chapter,verse_num}")
async def get_coordinates_from_verse_label(bible_version: bibleVersion, book_num: int, chapter: int, verse_num: int) \
        -> Response:
    scripture = search_scripture("bibleData", bible_version, book_num, chapter, verse_num)
    verse_result: BibleStructure = search_for_location_by_scripture(scripture.verse[verse_num])

    list_of_bible_versions = ["ESV Name", "KMZ Name"]
    coordinates = search_coordinates(verse_result.locations, "ESV Name",list_of_bible_versions)
    verse_result.locations = coordinates
    verse_result.scripture = scripture


    return verse_result

    # return verse_result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app)
    totalCount = insert_coordinates_store("Data/biblicalLonLat2_formatted.csv", "bibleData", "LonLats")
    totalCountBible = insert_bible_to_mongo("Data/asv.json", "bibleData", "Bible_ASV")
    print(totalCountBible)
    print(totalCount)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
