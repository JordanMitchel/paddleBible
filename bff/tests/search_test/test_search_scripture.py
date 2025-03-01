from unittest.mock import AsyncMock, patch

import pytest
from pymongo.errors import PyMongoError

from bff.src.services.search.search_scripture import get_scripture_using_book_and_verse
from shared.src.models.scripture_result import Scripture


@pytest.mark.asyncio
@patch("bff.src.services.search.search_scripture.get_collection")  # Mocking the get_database function
@pytest.mark.requires_decouple
async def test_get_scripture_found(mock_get_collection):
    # Mock the database and collection
    mock_coll = AsyncMock()
    mock_coll.find_one.return_value = {
        "book_name": "Genesis",
        "book": 1,
        "chapter": 1,
        "verse": 1,
        "text": "In the beginning, God created the heavens and the earth."
    }
    mock_get_collection.return_value = mock_coll

    # Call the function
    response = await get_scripture_using_book_and_verse("test-1","test_version", 1, 1, 1)

    # Assertions
    assert response.warnings is None
    assert (response.data ==
            Scripture(book='Genesis',
                      chapter=1,
                      verse={1: 'In the beginning, God created the heavens and the earth.'}))


@pytest.mark.asyncio
@patch("bff.src.services.search.search_scripture.get_collection")  # Mocking the get_database function
@pytest.mark.requires_decouple
async def test_get_scripture_not_found(mock_get_collection):
    # Mock the database and collection
    mock_coll = AsyncMock()
    mock_coll.find_one.return_value = None
    mock_get_collection.return_value = mock_coll

    # Call the function
    _response = await get_scripture_using_book_and_verse("test_version", "bible_version",1, 1, 1)

    # Assertions
    assert _response.data == Scripture(book='',chapter=0, verse={})
    assert _response.warnings == "No scripture found for query."


@pytest.mark.asyncio
@patch("bff.src.services.search.search_scripture.get_collection")  # Mocking the get_database function
async def test_get_scripture_error_handling(mock_get_collection):
    # Simulate an exception in the database call
    mock_get_collection.side_effect = PyMongoError("An error occurred with MongoDB")

    # Call the function
    _response = await get_scripture_using_book_and_verse("test-1","test_version", 1, 1, 1)

    # Assertions
    assert _response.data == Scripture(book='',chapter=0, verse={})
    assert "An error occurred with MongoDB" in _response.warnings
