from src.db.config import get_database
from src.models.Response import ResponseModel
from src.models.ScriptureResult import Scripture


async def get_scripture_using_book_and_verse(bible_version, book_num, chapter, verse_num) -> ResponseModel:

    db = await get_database()
    coll = db[bible_version]

    query = {"book": book_num, "chapter": chapter, "verse": verse_num}
    doc = await coll.find_one(query)
    if doc is not None:
        scripture = Scripture(book=doc["book_name"], chapter=chapter, verse={verse_num: doc['text']})
        return ResponseModel(success=True,data=scripture)

    else:
        scripture = Scripture(book="N/A", chapter=chapter, verse={verse_num: "N/A"})
        return ResponseModel(success= False, data=scripture, warnings="No scripture found")
