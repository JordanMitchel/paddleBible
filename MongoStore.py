from typing import List

import pandas as pd
from pymongo import MongoClient
import json

from Data.ScriptureResult import Place, Coordinates, Scripture


def mongoimport(csv_path, db_name, coll_name, db_url='localhost', db_port=27018):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    client = MongoClient(host=db_url, port=db_port, username="root",password="rootpassword")
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


def search_coordinates(locations: List[Place], db_name="bibleData", collection="LonLats", ):
    db_url = 'localhost'
    db_port = 27018
    username = "root"
    password = "rootpassword"
    client = MongoClient(host=db_url, port=db_port, username=username,password=password)
    db = client[db_name]
    coll = db[collection]
    count = 0
    for area in locations:
        place = area.location
        docESV = coll.find_one({"ESV Name": place})
        if docESV is None:
            docKMZ = coll.find_one({"KMZ Name": place})
            if docKMZ is None:
                locations[count].warning = "No co-ordinates found"
                return locations
            locations[count].coordinates= Coordinates(Lat=docKMZ['Lat'], Lon = docKMZ['Lon'])

            # locations[count].coordinates.Lat = docKMZ['Lat']
            # locations[count].coordinates.Lon = docKMZ['Lon']
            # locations[count][place] = {"Lat": docKMZ['Lat'], "Lon": docKMZ['Lon']}
        else:
            locations[count].coordinates= Coordinates(Lat=docESV['Lat'], Lon = docESV['Lon'])
            # locations[count].coordinates.Lon = docESV['Lon']
        count += 1

    return locations


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


totalCount = mongoimport("Data/biblicalLonLat2_formatted.csv", "bibleData", "LonLats")

totalCountBible = insert_bible_to_mongo("Data/asv.json", "bibleData", "Bible_ASV")
print(totalCountBible)
print(totalCount)
