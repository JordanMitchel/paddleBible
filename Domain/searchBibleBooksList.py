from pymongo import MongoClient


def get_all_bible_books(db_name="bibleData",
                       collection="Bible_ASV"):
    db_url = 'localhost'
    db_port = 27018
    username = "root"
    password = "rootpassword"
    client = MongoClient(host=db_url, port=db_port, username=username, password=password)
    db = client[db_name]
    coll = db[collection]

    bible_books = []
    for record in coll.aggregate(
            [
                {'$group':
                     {'_id':
                          {'book': '$book', 'book_name': '$book_name'}
                      }
                 }
            ]):
        bible_books.append(record["_id"])
        # print(record)

    sorted_bible_list = sorted(bible_books, key=lambda d: d['book'])
    return sorted_bible_list
