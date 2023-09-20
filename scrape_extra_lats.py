# Import the required library
from geopy.geocoders import Nominatim
from pymongo import MongoClient
import re
from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError

key = '0c12b649ffd54558846bde5342c92be4'
geocoder = OpenCageGeocode(key)


def location_square(lat,long):
    if lat> 39 or lat<10:
        return False
    if long>45 or long<-3:
        return False
    return True

def insert_new_lat_lon(collection,doc,location):
    relevant = location_square(location.latitude, location.longitude)
    if relevant:
        print("The latitude of the location is: ", location.latitude)
        print("The longitude of the location is: ", location.longitude)

        collection \
            .update_one({"_id": doc["_id"]}, {"$set": {"Lat": location.latitude, "Lon": location.longitude}})

        try:
            results = geocoder.reverse_geocode(location.latitude, location.longitude, language='en', no_annotations='1')
            if results and len(results):
                print(results[0]['formatted'])
        except:
            print("error geocoding location")


    else:
        print("out of area")

def clean_search_column(doc_col,pattern):
    if any(chr.isdigit() for chr in doc_col):
        new_string = re.sub(pattern, '', doc_col)
        return new_string
def query_null_lats():
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["bibleLocations"]
    Lat_long_collection = mydb["LonLats"]

    myquery = {"Lat": None}
    pattern = r'[0-9]'
    docs = Lat_long_collection.find(myquery)
    geolocator = Nominatim(user_agent="MyApp")
    for doc in docs:

        name = None
        if doc['ESV Name'] is None:
            name = clean_search_column(doc['KMZ Name'], pattern)
            location = geolocator.geocode(name)

            print(doc)
            if location is not None:
                insert_new_lat_lon(Lat_long_collection,doc,location)
            else:
                name = clean_search_column(doc['ESV Name'], pattern)
                location = geolocator.geocode(name)
                if location is not None:
                    insert_new_lat_lon(Lat_long_collection, doc, location)


        else:
            name = clean_search_column(doc['ESV Name'], pattern)
            location = geolocator.geocode(name)
            if location is not None:
                insert_new_lat_lon(Lat_long_collection, doc, location)
            else:
                name = clean_search_column(doc['KMZ Name'], pattern)
                location = geolocator.geocode(name)
                if location is not None:
                    insert_new_lat_lon(Lat_long_collection, doc, location)



        print("----------")

# query_null_lats()



def queryOneLat(name):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(name)
    relevant = location_square(location.latitude, location.longitude)
    if location is not None and relevant:
        print("The latitude of the location is: ", location.latitude)
        print("The longitude of the location is: ", location.longitude)

queryOneLat("Aphek")



