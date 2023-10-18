from typing import List

import spacy
from spacy.tokens import Span

from Data.ScriptureResult import BibleStructure, Place


def search_for_location(verse: str) -> BibleStructure:
    location_list_en_core = sentiment_search('en_core_web_sm', verse)
    location_list_wiki = sentiment_search('xx_ent_wiki_sm', verse)
    location_lists = location_list_en_core + location_list_wiki

    bible_struct: BibleStructure = BibleStructure()
    # bible_struct.verse = verse
    locationsArr = []
    if len(location_lists) > 0:
        location_lists_stripped = strip_locations(location_lists)

        for spot in location_lists_stripped:
            place_obj = Place()
            place_obj.location = spot
            locationsArr.append(place_obj)
        bible_struct.location_count = len(location_lists_stripped)

    else:
        bible_struct.warning = "No location found"

    bible_struct.locations = locationsArr
    return bible_struct


def sentiment_search(sentiment: str, verse: str):
    nlp = spacy.load(sentiment)
    doc = nlp(verse)
    gpe = []
    loc = []

    for entry in doc.ents:
        if entry.label_ == 'GPE':
            gpe.append(entry.text)
        elif entry.label_ == 'LOC':
            loc.append(entry.text)
    return gpe + loc


def strip_locations(locations: List[str]) -> []:
    ignore_places = ["north", "east", "south", "west","earth"]
    return set([place for place in locations if place.lower() not in ignore_places])
