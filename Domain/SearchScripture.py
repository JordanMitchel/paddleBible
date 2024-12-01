from pymongo import MongoClient

from Models.ScriptureResult import Scripture
from Domain.db import DB

def search_scripture(bible_version,book_num,chapter,verse_num) -> Scripture:
    coll = DB[bible_version]

    query = {"book": book_num, "chapter": chapter, "verse": verse_num}
    doc = coll.find_one(query)
    scripture: Scripture = Scripture(book=doc["book_name"], chapter=chapter, verse={verse_num:doc['text']})
    return scripture
