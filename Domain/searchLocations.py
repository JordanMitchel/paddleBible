from typing import List, Any

from pymongo import MongoClient

from Models.ScriptureResult import Coordinates, Place, SearchResult


def search_coordinates(locations: List[Place], bibleVersion: str, extra_bible_versions: List[str], db_name="bibleData",
                       collection="LonLats"):
    db_url = 'localhost'
    db_port = 27018
    username = "root"
    password = "rootpassword"
    client = MongoClient(host=db_url, port=db_port, username=username, password=password)
    db = client[db_name]
    coll = db[collection]
    count = 0
    for area in locations:
        place = area.location
        print(area)
        # docESV = coll.find_one({"ESV Name": place})
        # if docESV is None:
        #     docKMZ = coll.find_one({"KMZ Name": place})
        #     if docKMZ is None:
        #         locations[count].warning = "No co-ordinates initially found found"
        #         return locations
        #     locations[count].coordinates = Coordinates(Lat=docKMZ['Lat'], Lon=docKMZ['Lon'])
        #
        # else:
        #     locations[count].coordinates = Coordinates(Lat=docESV['Lat'], Lon=docESV['Lon'])
        initial_result = search_single_bible_version(bibleVersion, coll, place)
        if initial_result.ResultFound:
            locations[count].coordinates = initial_result.Location.coordinates
        else:
            deep_search_result = search_across_bible_versions(bibleVersion, extra_bible_versions, coll, place)
            if deep_search_result.ResultFound:
                locations[count].coordinates = deep_search_result.Location.coordinates
            else:
                locations[count].warning = f"No co-ordinates found for {area}"

        count += 1

    return locations


def search_single_bible_version(bible_version, collection, place) -> SearchResult:
    bible_location = light_search(place, collection, bible_version)
    return bible_location


def search_across_bible_versions(intial_version, list_of_versions, collection, place):
    for bible_version in list_of_versions:
        bible_location_result: SearchResult = light_search(place, collection, bible_version)
        if bible_location_result.ResultFound:
            return bible_location_result
    bible_location_deep_result: SearchResult = deep_search_and_update(place, collection, intial_version, list_of_versions)
    return bible_location_deep_result


def light_search(place, collection, bible_version) -> SearchResult:
    location_in_bible = collection.find_one({bible_version: place})
    if location_in_bible is not None:
        coordinates = Coordinates(Lat=location_in_bible['Lat'] or 0, Lon=location_in_bible['Lon'] or 0)
        location = Place(location = place, coordinates=coordinates, Passages=location_in_bible["Passages"],
                         Comment=location_in_bible["Comment"])
        return SearchResult(ResultFound=True, Location=location)
    else:
        return SearchResult()


def deep_search_and_update(area, collection, bible_version, extra_versions) -> SearchResult:
    # If multiple words in area
    if area.strip().count(' ') > 0:
        areas_list = area.split()
        for location in areas_list:
            if location[0].isupper():
                #             search bible for word if found insert the word back into mongo to avoid deep search
                result = light_search(location, collection, bible_version)
                update_bible_with_location(result, extra_versions, area, collection)
                return result
        return SearchResult(False)
    else:
        # cant find any places sorry
        return SearchResult(False)


def update_bible_with_location(identified_location, bible_versions, original_location, collection):
    if identified_location.ResultFound:
        result_json={}
        for version in bible_versions:
            result_json[version] = original_location

        result_json["Lat"] = identified_location.Location.coordinates.Lat
        result_json["Lon"] = identified_location.Location.coordinates.Lat
        result_json["Passages"] = identified_location.Location.Passages
        result_json["Comment"] = identified_location.Location.Comment

        collection.insert_one(result_json)
