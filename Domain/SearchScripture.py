from Models.ScriptureResult import Scripture
from Domain.db import DB


async def search_scripture(bible_version, book_num, chapter, verse_num) -> Scripture:
    coll = DB[bible_version]

    query = {"book": book_num, "chapter": chapter, "verse": verse_num}
    doc = await coll.find_one(query)
    if doc != None:
        return Scripture(book=doc["book_name"], chapter=chapter, verse={verse_num: doc['text']})

    else:
        return Scripture(book="N/A", chapter=chapter, verse={verse_num: "N/A"})
