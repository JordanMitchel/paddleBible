import pandas as pd
from pymongo import MongoClient
import json

def mongoimport(csv_path, db_name, coll_name, db_url='localhost', db_port=27017):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))

    collist = db.list_collection_names()
    if "LonLats" in collist:
        print("The collection exists.")
        coll.drop()
    coll.insert_many(payload)
    return coll.count_documents({})


def insert_bible_to_mongo(json_path, db_name, coll_name, db_url='localhost', db_port=27017):
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    collection = db[coll_name]


    # Loading or Opening the json file
    with open(json_path) as file:
        file_data = json.load(file)

    data = file_data["verses"]

# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

totalCount =mongoimport("Data/biblicalLonLat2_formatted.csv", "bibleLocations", "LonLats")

totalCountBible = insert_bible_to_mongo("Data/asv.json","bibleVersions","ASV")
print(totalCountBible)
print(totalCount)
