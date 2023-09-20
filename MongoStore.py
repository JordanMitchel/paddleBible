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


totalCount =mongoimport("Data/biblicalLonLat2_formatted.csv", "bibleLocations", "LonLats")
print(totalCount)
