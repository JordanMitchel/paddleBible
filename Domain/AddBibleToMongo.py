import json

from pymongo import MongoClient

def insert_bible_to_mongo(json_path, db_name, coll_name, db_url='localhost', db_port=27018):
    client = MongoClient(db_url, db_port, username="root",password="rootpassword")
    db = client[db_name]
    collection = db[coll_name]


    # Loading or Opening the json file
    with open(json_path) as file:
        file_data = json.load(file)

    data = file_data["verses"]

    # Inserting the loaded data in the Collection
    # if JSON contains data more than one entry
    # insert_many is used else insert_one is used
    collist = db.list_collection_names()
    if "Bible_ASV" in collist:
        print("The collection exists.")
        collection.drop()
    if isinstance(data, list):
        collection.insert_many(data)

    else:
        collection.insert_one(data)

    return collection.count_documents({})

totalCountBible = insert_bible_to_mongo("../Data/asv.json", "bibleData", "Bible_ASV")
print(totalCountBible)
