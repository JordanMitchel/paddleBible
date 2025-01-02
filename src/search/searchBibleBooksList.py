from src.db.config import get_database
from src.models.response import ResponseModel


async def get_all_bible_books(collection="Bible_ASV")-> ResponseModel:

    try:

        db = await get_database()
        coll = db[collection]

        bible_books = []
        async for record in coll.aggregate(
                [
                    {'$group':
                         {'_id':
                              {'book': '$book', 'book_name': '$book_name'}
                          }
                     }
                ]
        ):
            bible_books.append(record["_id"])
            # print(record)

        sorted_bible_list = sorted(bible_books, key=lambda d: d['book'])
        response = ResponseModel(success= True, data= sorted_bible_list)
        return response

    except Exception as e:
        return ResponseModel(success=False, warnings=f"Error fetching bible books: {str(e)}")

