from Domain.db import DB


async def get_all_bible_books(collection="Bible_ASV"):

    coll = DB[collection]

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
    return sorted_bible_list

