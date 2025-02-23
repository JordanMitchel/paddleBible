from unittest.mock import AsyncMock, patch
import pytest
from pymongo.errors import PyMongoError

from bff.src.services.search.search_scripture import get_scripture_using_book_and_verse
from shared.src.models.scripture_result import Scripture


@pytest.mark.asyncio
@patch("bff.src.services.search.search_scripture.get_collection",  new_callable=AsyncMock)  # Mocking the get_database function
@pytest.mark.requires_decouple
async def test_get_scripture_found(mock_get_collection):
    # ✅ Mock the collection behavior
    mock_coll = AsyncMock()
    mock_cursor = AsyncMock()

    # ✅ Mock find().sort().to_list() chain properly
    mock_cursor.to_list.return_value = [
        {
            "book_name": "Genesis",
            "chapter": 1,
            "verse": 1,
            "text": "In the beginning, God created the heavens and the earth."
        }
    ]

    # ✅ Ensure mock find() returns a mock cursor
    mock_coll.find.return_value.sort.return_value = mock_cursor

    # ✅ Ensure `get_collection` returns `mock_coll` when awaited
    mock_get_collection.return_value = mock_coll

    # 🔥 Call the function
    response = await get_scripture_using_book_and_verse("test_version", 1, 1, 1)

    # ✅ Assertions
    assert response.success is True
    assert response.data == Scripture(
        book='Genesis',
        chapter=1,
        verse={1: 'In the beginning, God created the heavens and the earth.'}
    )

@pytest.mark.asyncio
@patch("bff.src.services.search.search_scripture.get_database")  # Mocking the get_database function
@pytest.mark.requires_decouple
async def test_get_scripture_not_found(mock_get_database):
    # Mock the database and collection
    mock_coll = AsyncMock()
    mock_coll.find_one.return_value = None
    mock_db = AsyncMock()
    mock_db.__getitem__.return_value = mock_coll
    mock_get_database.return_value = mock_db

    # Call the function
    response = await get_scripture_using_book_and_verse("test_version", 1, 1, 1)

    # Assertions
    assert response.success is False
    assert isinstance(response.data, Scripture)
    assert response.data.book == "N/A"
    assert response.data.verse[1] == "N/A"
    assert response.warnings == "No scripture found"


@pytest.mark.asyncio
@patch("bff.src.services.search.search_scripture.get_database")  # Mocking the get_database function
async def test_get_scripture_error_handling(mock_get_database):
    # Simulate an exception in the database call
    mock_get_database.side_effect = PyMongoError("An error occurred with MongoDB")

    # Call the function
    _response = await get_scripture_using_book_and_verse("test_version", 1, 1, 1)

    # Assertions
    assert _response.success is False
    assert "An error occurred with MongoDB" in _response.warnings
