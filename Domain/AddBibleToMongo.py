import json
from Domain.db import DB


def insert_bible_to_mongo(json_path, coll_name):

    collection = DB[coll_name]

    # Loading or Opening the json file
    with open(json_path) as file:
        file_data = json.load(file)

    data = file_data["verses"]

    # Inserting the loaded data in the Collection
    # if JSON contains data more than one entry
    # insert_many is used else insert_one is used
    collist = DB.list_collection_names()
    if "Bible_ASV" in collist:
        print("The collection exists.")
        collection.drop()
    if isinstance(data, list):
        collection.insert_many(data)
        print(collection.count_documents({}))
    else:
        collection.insert_one(data)
        print(collection.count_documents({}))


# insert_bible_to_mongo

