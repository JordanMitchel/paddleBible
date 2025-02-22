from unittest.mock import patch, AsyncMock
import pytest

from bff.src.services.search.search_for_location_by_scripture import request_locations_using_scripture
from shared.src.models.scripture_result import BibleStructure, Scripture, Place, ResponseModel
from bff.src.routes.router_scripture import get_bible_books
from shared.tests.test_data.mock_data import mock_bible_books


@pytest.mark.asyncio
@patch("bff.src.routes.router_scripture.get_all_bible_books", new_callable=AsyncMock)
@pytest.mark.requires_decouple
async def test_get_bible_books(mock_get_all_bible_books):
    # Arrange
    bible_data = mock_bible_books
    mock_get_all_bible_books.return_value = bible_data

    # Act
    books = await get_bible_books()

    # Assert
    assert books.success is True
    assert books.data == bible_data.data


@pytest.mark.asyncio
@patch("bff.src.routes.router_scripture.get_locations_using_scripture", new_callable=AsyncMock)
async def test_get_coordinates_from_verse_returns_location_with_good_scripture(mock_get_locations):
    # Arrange
    verse = (
        "Yet to his son I will give one tribe,"
        " that David my servant may always have a lamp"
        " before me in Jerusalem, the city where I have chosen to put my name."
    )

    mock_scripture = Scripture(book="book1", chapter=1, verse={1: "verse1"})
    mock_bible_data = BibleStructure(
        scripture=mock_scripture,
        locations=[Place()],
        location_count=1
    )
    coordinate_response_model = ResponseModel(success=True, data=mock_bible_data)
    mock_get_locations.return_value = coordinate_response_model

    # Act
    verse_result = await request_locations_using_scripture(verse)

    # Assert
    assert verse_result.success is True
    assert verse_result.data.location_count == 1
    assert len(verse_result.data.locations) == 1

    # Verify mock was called
    assert isinstance(verse_result.data, BibleStructure)


@pytest.mark.asyncio
async def test_get_coordinates_from_verse_returns_warning_with_empty_scripture():
    # Arrange
    verse = ""

    # Act
    verse_result = await request_locations_using_scripture(verse)

    # Assert
    assert verse_result.success is False
    assert verse_result.warnings == "Empty verse no location found"
    assert isinstance(verse_result.data, BibleStructure)
