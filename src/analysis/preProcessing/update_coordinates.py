from geopy.geocoders import Nominatim
from pymongo import MongoClient
import re
from opencage.geocoder import OpenCageGeocode
from requests import RequestException

KEY = '0c12b649ffd54558846bde5342c92be4'
geocoder = OpenCageGeocode(KEY)


def update_null_coordinates_using_location_name():
    client = MongoClient("mongodb://localhost:27018/")
    mydb = client["bibleLocations"]
    lat_long_collection = mydb["LonLats"]

    myquery = {"Lat": None}
    pattern = r'[0-9]'
    docs = lat_long_collection.find(myquery)
    geolocator = Nominatim(user_agent="MyApp")
    for doc in docs:
        if doc['ESV Name'] is None:
            name = clean_substring_in_lat_and_longs(doc['KMZ Name'], pattern)
            location = geolocator.geocode(name)

            print(doc)
            if location is not None:
                insert_new_lat_lon(lat_long_collection, doc, location)
            else:
                name = clean_substring_in_lat_and_longs(doc['ESV Name'], pattern)
                location = geolocator.geocode(name)
                if location is not None:
                    insert_new_lat_lon(lat_long_collection, doc, location)

        else:
            name = clean_substring_in_lat_and_longs(doc['ESV Name'], pattern)
            location = geolocator.geocode(name)
            if location is not None:
                insert_new_lat_lon(lat_long_collection, doc, location)
            else:
                name = clean_substring_in_lat_and_longs(doc['KMZ Name'], pattern)
                location = geolocator.geocode(name)
                if location is not None:
                    insert_new_lat_lon(lat_long_collection, doc, location)

        print("----------")


def is_in_biblical_geo_square(lat, long):
    if lat > 39 or lat < 10:
        return False
    if long > 45 or long < -3:
        return False
    return True


def insert_new_lat_lon(collection, doc, location):
    is_relevant_location = is_in_biblical_geo_square(location.latitude, location.longitude)
    if is_relevant_location:
        print("The latitude of the location is: ", location.latitude)
        print("The longitude of the location is: ", location.longitude)

        collection \
            .update_one({"_id": doc["_id"]},
                        {"$set": {"Lat": location.latitude,
                                  "Lon": location.longitude}})

        try:
            results = geocoder.reverse_geocode(location.latitude,
                                               location.longitude,
                                               language='en', no_annotations='1')
            if results and len(results):
                print(results[0]['formatted'])
        except (IndexError, KeyError):
            print("Error processing results: missing or invalid data.")
        except RequestException:
            print("Network error occurred during geocoding.")
        except Exception as e:  # Catch-all for any other unexpected exceptions
            print(f"An unexpected error occurred: {e}")

    else:
        print("out of area")


def clean_substring_in_lat_and_longs(doc_col, pattern):
    if any(each_chr.isdigit() for each_chr in doc_col):
        new_string = re.sub(pattern, '', doc_col)
        return new_string
