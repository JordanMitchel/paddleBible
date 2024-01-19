from typing import List

from pymongo import MongoClient

from Data.ScriptureResult import Coordinates, Place


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
