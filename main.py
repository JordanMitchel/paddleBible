# This is a sample Python script.

import uvicorn

from Data.ScriptureResult import BibleStructure, bibleVersion
from fastapi import FastAPI, Response

from Domain.AddBibleToMongo import insert_bible_to_mongo
from Domain.AddCoordinatesStore import importCoordinatesStore
from Domain.SearchScripture import search_scripture
from Domain.searchLocations import search_coordinates
from DirectAnalysis.cityScraping import search_for_location

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


@app.get("/Scripture/{verse}")
async def get_coordinates_from_verse(verse: str) -> BibleStructure:
    verse_result: BibleStructure = search_for_location(verse)
    return verse_result

@app.get("/Scripture/label/{bible_version, book_number,chapter,verse_num}")
async def get_coordinates_from_verse_label(bible_version:bibleVersion, book_num: int, chapter: int, verse_num: int) \
        -> Response:
    scripture = search_scripture("bibleData", bible_version, book_num, chapter, verse_num)
    verse_result: BibleStructure = search_for_location(scripture.verse[verse_num])

    coordinates = search_coordinates(verse_result.locations)
    verse_result.locations = coordinates
    verse_result.scripture = scripture
    # return json.loads(verse_result.model_dump_json())
    # verse_result.locations = [{"jo":{"hi":142}}]
    # json_compatible_item_data = jsonable_encoder(verse_result)

    print(verse_result)
    # return JSONResponse(content=json_compatible_item_data)
    # # [3, 1.34,True,"hello",{"hi"},{"age":40}]

    return verse_result

    # return verse_result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    uvicorn.run(app)
    totalCount = importCoordinatesStore("Data/biblicalLonLat2_formatted.csv", "bibleData", "LonLats")
    totalCountBible = insert_bible_to_mongo("Data/asv.json", "bibleData", "Bible_ASV")
    print(totalCountBible)
    print(totalCount)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
