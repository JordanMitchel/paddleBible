from src.db.config import get_database
from src.models.ScriptureResult import Scripture


async def get_scripture_using_book_and_verse(bible_version, book_num, chapter, verse_num) -> Scripture:

    db = await get_database()
    coll = db[bible_version]

    query = {"book": book_num, "chapter": chapter, "verse": verse_num}
    doc = await coll.find_one(query)
    if doc is not None:
        return Scripture(book=doc["book_name"], chapter=chapter, verse={verse_num: doc['text']})

    else:
        return Scripture(book="N/A", chapter=chapter, verse={verse_num: "N/A"})
