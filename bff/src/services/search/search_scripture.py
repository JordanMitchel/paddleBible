from pymongo.errors import ServerSelectionTimeoutError, OperationFailure, PyMongoError

from domain.src.services.db_connector import get_collection
from shared.src.models.scripture_result import Scripture, ResponseModel, ScriptureRequest


async def get_scripture_using_book_and_verse(clientId,
                                             bible_version,
                                             book_num,
                                             chapter,
                                             verse_num) -> ScriptureRequest:
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
            return ScriptureRequest(clientId=clientId, data=scripture)

        print("❌ No scripture found for query.")
        return ScriptureRequest(clientId=clientId)

    except ServerSelectionTimeoutError:
        print("MongoDB server could not be reached. Please check your connection.")
        return ScriptureRequest(clientId=clientId)

    except OperationFailure as e:
        print(f"Error fetching scripture: {str(e)}")
        return ScriptureRequest(clientId=clientId)

    except PyMongoError as e:
        print(f"An error occurred with MongoDB: {str(e)}")
        return ScriptureRequest(clientId=clientId)


async def get_scripture_using_verse(clientId, bible_version,verse)->ScriptureRequest:
    try:
        coll = await get_collection(bible_version)

        print(coll)
        query = {"text": {"$regex": verse, "$options": "i"}}  # Case-insensitive search
        print(query)

        doc = await coll.find_one(query)  # Find the first matching document
        print(f"📄 Fetched Document: {doc}")

        if doc:
            scripture = Scripture(
                book=doc["book_name"],
                chapter=doc["chapter"],
                verse={doc["verse"]: doc["text"]}
            )
            print(f"✅ Found Scripture: {scripture}")
            return ScriptureRequest(clientId=clientId, data=scripture)

        print("❌ No scripture found for query.")
        return ScriptureRequest(clientId=clientId)

    except ServerSelectionTimeoutError:
        print("MongoDB server could not be reached. Please check your connection.")
        return ScriptureRequest(clientId=clientId)

    except OperationFailure as e:
        print(f"Error fetching scripture: {str(e)}")
        return ScriptureRequest(clientId=clientId)

    except PyMongoError as e:
        print(f"An error occurred with MongoDB: {str(e)}")
        return ScriptureRequest(clientId=clientId)
