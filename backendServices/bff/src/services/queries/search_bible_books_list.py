import asyncio

from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure, PyMongoError

from backendServices.domain.src.services.db_connector import get_database
from backendServices.shared.src.models.scripture_result import ResponseModel

class BibleQuery:
    def __init__(self, bible_version="Bible_ASV"):
        self.bible_version = bible_version
        self.collection = None

    async def _get_collection(self):
        if self.collection is None:
            db = await get_database()
            self.collection = db[self.bible_version]
        return self.collection

    async def get_all_bible_books(self) -> ResponseModel:
        try:
            collection = await self._get_collection()
            bible_books = []
            async for record in collection.aggregate(
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

    async def get_chapters_by_book(self, book:int)-> ResponseModel:
        try:
            # Run aggregation
            collection = await self._get_collection()

            pipeline = [
                {'$match': {'book': book}},
                {'$group': {'_id': "$chapter"}},
                {'$sort': {'_id': 1}}
            ]

            # Convert cursor to list
            chapter_cursor = collection.aggregate(pipeline)
            chapter_list = await chapter_cursor.to_list(length=None)

            # Optional: flatten _id into "chapter" field
            chapters = [doc["_id"] for doc in chapter_list]

            return ResponseModel(success=True, data=chapters)

        except ServerSelectionTimeoutError:
            return ResponseModel(success=False, warnings="MongoDB server could not be reached."
                                                     " Please check your connection.")

        except OperationFailure as e:
            return ResponseModel(success=False, warnings=f"MongoDB operation failed: {str(e)}")

        except PyMongoError as e:
            return ResponseModel(success=False, warnings=f"An error occurred with MongoDB: {str(e)}")

    async def get_verses_by_chapter_and_book(self, book:int, chapter:int)-> ResponseModel:
        try:
            collection = await self._get_collection()


            pipeline = []

            verse_curse = collection.aggregate(pipeline)
            verse_list  = None

            verses =[doc["_id"] for doc in verse_list]

            return  ResponseModel(success=True, data=verses)

        except ServerSelectionTimeoutError:
            return ResponseModel(success=False, warnings="MongoDB server could not be reached."
                                                         " Please check your connection.")

        except OperationFailure as e:
            return ResponseModel(success=False, warnings=f"MongoDB operation failed: {str(e)}")

        except PyMongoError as e:
            return ResponseModel(success=False, warnings=f"An error occurred with MongoDB: {str(e)}")
