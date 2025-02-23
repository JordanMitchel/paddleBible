from enum import Enum
from typing import Dict, Optional, Any, List

from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    Lat: float = 0.0
    Lon: float = 0.0


class Place(BaseModel):
    location: Optional[str] = ""
    coordinates: Optional[Coordinates] = Field(default_factory=Coordinates)
    warning: str | None = None
    Passages: str | None = None
    Comment: str | None = None


class Scripture(BaseModel):
    book: str = ""
    chapter: int = 0
    verse: Dict[int, str] = Field(default={})


class BibleStructure(BaseModel):
    scripture: Scripture = Field(default_factory=Scripture)
    locations: list[Place] | None = None
    location_count: int = 0


class SearchResult(BaseModel):
    ResultFound: bool = False
    Location: Place = Field(default={})


class BibleVersion(str, Enum):
    ASV = "Bible_ASV"
    NIV = "Bible_NIV"
    NLT = "Bible_NLT"
    KJV = "Bible_KJV"


class BibleBook(int, Enum):
    GENESIS = 1
    EXODUS = 2
    LEVITICUS = 3
    NUMBERS = 4
    DEUTERONOMY = 5
    JOSHUA = 6
    JUDGES = 7


class DataModel(BaseModel):
    scripture: Scripture
    locations: List[Place]
    location_count: int


class ScriptureResponse(BaseModel):
    success: bool
    data: BibleStructure = Field(default_factory=BibleStructure)
    warnings: Optional[str] = None


class ResponseModel(BaseModel):
    success: bool
    data: Any | None = None
    warnings: Optional[str] = None


class VerseRequest(BaseModel):
    bible_version: BibleVersion
    book_num: int
    chapter: int
    verse_num: int
