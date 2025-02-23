from pymongo.errors import ServerSelectionTimeoutError, OperationFailure, PyMongoError

from domain.src.services.db_connector import get_collection
from shared.src.models.scripture_result import Scripture, ResponseModel


async def get_scripture_using_book_and_verse(bible_version,
                                             book_num,
                                             chapter,
                                             verse_num) -> ResponseModel:
    try:
        coll = await get_collection(bible_version)

        print(coll)
        query = {"book": book_num, "chapter": chapter, "verse": verse_num}
        print(query)
        doc = await coll.find_one(query)

        print(f"📄 Fetched Document: {doc}")

        if doc:
            scripture = Scripture(
                book=doc["book_name"],
                chapter=doc["chapter"],
                verse={doc["verse"]: doc["text"]}
            )
            print(f"✅ Found Scripture: {scripture}")
            return ResponseModel(success=True, data=scripture)

        print("❌ No scripture found for query.")
        return ResponseModel(success=False, warnings="No scripture found")

    except ServerSelectionTimeoutError:
        return ResponseModel(success=False, warnings="MongoDB server could not be reached."
                                                     " Please check your connection.")
    except OperationFailure as e:
        return ResponseModel(success=False, warnings=f"Error fetching scripture: {str(e)}")

    except PyMongoError as e:
        return ResponseModel(success=False, warnings=f"An error occurred with MongoDB: {str(e)}")
