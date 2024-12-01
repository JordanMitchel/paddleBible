from Domain.db import DB


def bibles_list():

    collections = DB.list_collection_names()
    bible_versions = []
    for coll in collections:
        if coll[0] == "B":
            version = coll.split("_")[1]
            bible_versions.append(version)

    return bible_versions


bibles_list()
