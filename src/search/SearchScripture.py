from src.db.config import get_database
from src.models.response import ResponseModel
from src.models.scripture_result import Scripture


async def get_scripture_using_book_and_verse(bible_version, book_num, chapter, verse_num) -> ResponseModel:
    try:
        db = await get_database()
        coll = db[bible_version]

        query = {"book": book_num, "chapter": chapter, "verse": verse_num}
        doc = await coll.find_one(query)

        if doc:
            scripture = Scripture(book=doc["book_name"], chapter=chapter, verse={verse_num: doc["text"]})
            return ResponseModel(success=True, data=scripture)

        return ResponseModel(
            success=False,
            data=Scripture(book="N/A", chapter=chapter, verse={verse_num: "N/A"}),
            warnings="No scripture found"
        )
    except Exception as e:
        # Log exception here
        return ResponseModel(success=False, warnings=f"Error fetching scripture: {str(e)}")
