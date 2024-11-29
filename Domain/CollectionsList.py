from pymongo import MongoClient


def bibles_list(db_name="bibleData"):
    db_url = 'localhost'
    db_port = 27018
    username = "root"
    password = "rootpassword"
    client = MongoClient(host=db_url, port=db_port, username=username, password=password)
    db = client[db_name]
    collections = db.list_collection_names()
    bible_versions = []
    for coll in collections:
        if coll[0] == "B":
            version = coll.split("_")[1]
            bible_versions.append(version)

    return bible_versions
bibles_list()