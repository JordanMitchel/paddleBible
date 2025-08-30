from pymongo.errors import ServerSelectionTimeoutError, OperationFailure, PyMongoError

from domain.src.db import get_database
from shared.src.models.scripture_result import ResponseModel


async def get_all_bible_books(collection="Bible_ASV") -> ResponseModel:
    try:
        db = await get_database()
        coll = db[collection]

        bible_books = []
        async for record in coll.aggregate(
                [
                    {
                        '$group': {
                            '_id': {
                                'book': '$book',
                                'book_name': '$book_name'
                            }
                        }
                    }
                ]
        ):
            bible_books.append(record["_id"])

        sorted_bible_list = sorted(bible_books, key=lambda d: d['book'])
        return ResponseModel(success=True, data=sorted_bible_list)

    except ServerSelectionTimeoutError:
        return ResponseModel(success=False, warnings="MongoDB server could not be reached."
                                                     " Please check your connection.")

    except OperationFailure as e:
        return ResponseModel(success=False, warnings=f"MongoDB operation failed: {str(e)}")

    except PyMongoError as e:
        return ResponseModel(success=False, warnings=f"An error occurred with MongoDB: {str(e)}")
