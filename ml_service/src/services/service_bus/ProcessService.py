from typing import List

import spacy

from shared.src.models.scripture_result import BibleStructure, Place, ScriptureResponse, Scripture, ScriptureRequest


# noinspection PyMethodMayBeStatic
class ProcessService:

    async def process_text(self, request: ScriptureRequest) -> ScriptureResponse:
        verse = list(request.data.verse.values())[0]
        location_list_en_core = self.sentiment_search('en_core_web_sm',verse)
        location_list_wiki = self.sentiment_search('xx_ent_wiki_sm', verse)
        location_lists = location_list_en_core + location_list_wiki
        stripped_list = self.strip_locations_of_unnecessary_words(location_lists)
        locations_arr = []
        for spot in stripped_list:
            place_obj = Place()
            place_obj.location = spot
            locations_arr.append(place_obj)

        scripture = request.data
        bible_struct = BibleStructure(scripture=scripture, locations=locations_arr, location_count=len(locations_arr))
        return ScriptureResponse(clientId=request.clientId, success=True, data=bible_struct)

    def sentiment_search(self, sentiment: str, verse: str) -> List[str]:
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

    def strip_locations_of_unnecessary_words(self, locations: List[str]) -> set[str]:
        ignore_words = {"north", "east", "south", "west", "earth", "christ", "jesus", "christ jesus", "eden"}
        return {place for place in locations if place.lower() not in ignore_words}
