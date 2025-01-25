from pymongo.errors import ServerSelectionTimeoutError, OperationFailure, PyMongoError

from domain.src.services.db_connector import get_collection
from shared.src.models.response import ResponseModel
from shared.src.models.scripture_result import Scripture


async def get_scripture_using_book_and_verse(bible_version,
                                             book_num,
                                             chapter,
                                             verse_num) -> ResponseModel:
    try:
        coll = await get_collection(bible_version)

        query = {"book": book_num, "chapter": chapter, "verse": verse_num}
        doc = await coll.find_one(query)

        if doc:
            scripture = Scripture(book=doc["book_name"],
                                  chapter=chapter,
                                  verse={verse_num: doc["text"]})
            return ResponseModel(success=True, data=scripture)

        return ResponseModel(
            success=False,
            data=Scripture(book="N/A", chapter=chapter, verse={verse_num: "N/A"}),
            warnings="No scripture found"
        )

    except ServerSelectionTimeoutError:
        return ResponseModel(success=False, warnings="MongoDB server could not be reached."
                                                     " Please check your connection.")
    except OperationFailure as e:
        return ResponseModel(success=False, warnings=f"Error fetching scripture: {str(e)}")

    except PyMongoError as e:
        return ResponseModel(success=False, warnings=f"An error occurred with MongoDB: {str(e)}")
