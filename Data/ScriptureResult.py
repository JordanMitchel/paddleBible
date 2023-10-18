from enum import Enum
from typing import List, Dict, Optional
from typing_extensions import TypedDict

from pydantic import BaseModel


class Coordinates(BaseModel):
    Lat: float = 0.0
    Lon: float =0.0


class Place(BaseModel):
    location: Optional[str] =""
    coordinates: Optional[Coordinates] = {}
    warning: str | None = None

#
# class Verse(BaseModel):
#     verse: Optional[Dict[int,str]]


class Scripture(BaseModel):
    book: str = ""
    chapter: int = 0
    verse: Dict[int, str]


class BibleStructure(BaseModel):
    scripture: Scripture = {}
    locations: list[Place] | None = None
    location_count: int = 0


class bibleVersion(str, Enum):
    ASV = "Bible_ASV"
    NIV = "Bible_NIV"
    NLT = "Bible_NLT"
    KJV = "Bible_KJV"


class bibleBook(int, Enum):
    GENESIS = 1
    EXODUS = 2
    LEVITICUS = 3
    NUMBERS = 4
    DEUTERONOMY = 5
    JOSHUA = 6
    JUDGES  = 7
