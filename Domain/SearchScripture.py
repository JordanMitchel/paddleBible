from pymongo import MongoClient

from Models.ScriptureResult import Scripture


def search_scripture(db_name,bible_version,book_num,chapter,verse_num) -> Scripture:
    db_url = 'localhost'
    db_port = 27018
    username = "root"
    password = "rootpassword"
    client = MongoClient(host=db_url, port=db_port, username=username,password=password)
    db = client[db_name]
    coll = db[bible_version]

    query = {"book": book_num, "chapter": chapter, "verse": verse_num}
    doc = coll.find_one(query)
    scripture: Scripture = Scripture(book=doc["book_name"], chapter=chapter, verse={verse_num:doc['text']})
    return scripture
