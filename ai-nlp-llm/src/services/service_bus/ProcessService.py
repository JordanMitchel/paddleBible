from typing import List

import spacy

from shared.src.models.response import ResponseModel
from shared.src.models.scripture_result import BibleStructure, Place


# noinspection PyMethodMayBeStatic
class ProcessService:

    async def message_callback(self,body, message):
        """Callback function for processing messages."""
        response = await self.process_text(body)
        print(f"✅ Processed message: {response}")
        message.ack()


    async def process_text(self,verse: str) -> ResponseModel:
        location_list_en_core = self.sentiment_search('en_core_web_sm', verse)
        location_list_wiki = self.sentiment_search('xx_ent_wiki_sm', verse)
        location_lists = location_list_en_core + location_list_wiki

        locations_arr = []
        for spot in location_lists:
            place_obj = Place()
            place_obj.location = spot
            locations_arr.append(place_obj)
        bible_struct = BibleStructure(locations=locations_arr, location_count=len(locations_arr))
        return ResponseModel(success=True, data=bible_struct)


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
        ignore_words = {"north", "east", "south", "west", "earth", "christ", "jesus", "christ jesus"}
        return {place for place in locations if place.lower() not in ignore_words}