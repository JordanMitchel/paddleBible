from src.db.config import get_database

async def bibles_list():

    db = await get_database()
    collections = db.list_collection_names()
    bible_versions = []
    for coll in collections:
        if coll[0] == "B":
            version = coll.split("_")[1]
            bible_versions.append(version)

    return bible_versions


bibles_list()
