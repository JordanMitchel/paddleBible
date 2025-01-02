from src.models.Response import ResponseModel
from src.models.ScriptureResult import BibleStructure, Place


async def get_locations_using_scripture(verse: str) -> ResponseModel:
    if not verse:
        return ResponseModel(success=False,data=BibleStructure(),warnings="Empty verse no location found")
    location_list_en_core = sentiment_search('en_core_web_sm', verse)
    location_list_wiki = sentiment_search('xx_ent_wiki_sm', verse)
    location_lists = location_list_en_core + location_list_wiki

    bible_struct: BibleStructure = BibleStructure()
    # bible_struct.verse = verse
    locations_arr = []
    warnings = ""
    if len(location_lists) > 0:
        location_lists_stripped = strip_locations_of_unneccesary_words(location_lists)

        for spot in location_lists_stripped:
            place_obj = Place()
            place_obj.location = spot
            locations_arr.append(place_obj)
        bible_struct.location_count = len(location_lists_stripped)

    else:
        warnings = "No location found"

    bible_struct.locations = locations_arr
    if len(locations_arr)==0:
        response = ResponseModel(success=True, data=bible_struct, warnings=warnings)
        return response
    return ResponseModel(success=True, data=bible_struct)


from typing import List
import spacy

def sentiment_search(sentiment: str, verse: str) -> List[str]:
    if not sentiment or not verse:
        return []

    try:
        # Load the specified SpaCy model
        nlp = spacy.load(sentiment)
        doc = nlp(verse)
        gpe = []
        loc = []

        # Extract entities labeled as GPE or LOC
        for entry in doc.ents:
            if entry.label_ == 'GPE':
                gpe.append(entry.text)
            elif entry.label_ == 'LOC':
                loc.append(entry.text)
        return gpe + loc
    except OSError as e:
        # Handle missing or invalid SpaCy models
        print(f"Error loading SpaCy model '{sentiment}': {e}")
        return []



def strip_locations_of_unneccesary_words(locations: List[str]) -> set[str]:
    ignore_places = ["north", "east", "south", "west", "earth"]
    return set([place for place in locations if place.lower() not in ignore_places])
