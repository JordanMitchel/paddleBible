from unittest.mock import AsyncMock, patch, MagicMock
import pytest
from pymongo.errors import PyMongoError

from bff.src.services.search.search_bible_books_list import get_all_bible_books
from shared.tests.test_data.mock_data import mock_bible_books


class AsyncIteratorMock:
    def __init__(self, data):
        self.data = data

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self.data:
            raise StopAsyncIteration
        return self.data.pop(0)


@pytest.mark.asyncio
@patch("bff.src.services.search.search_bible_books_list.get_database")
async def test_get_all_bible_books(mock_get_database):
    # Mock data returned by the aggregate query
    mock_aggregate_data = [
        {'_id': {'book': 1, 'book_name': 'Genesis'}},
        {'_id': {'book': 2, 'book_name': 'Exodus'}},
        {'_id': {'book': 3, 'book_name': 'Leviticus'}},
    ]

    # Expected sorted response
    expected_response = mock_bible_books

    # Create mock collection
    mock_collection = AsyncMock()

    # Instead of returning a coroutine, directly set the return value to our AsyncIteratorMock
    mock_collection.aggregate = MagicMock(
        return_value=AsyncIteratorMock(mock_aggregate_data.copy())
    )

    # Create mock database
    mock_db = AsyncMock()
    mock_db.__getitem__.return_value = mock_collection

    # Set up the database mock
    mock_get_database.return_value = mock_db

    # Call the function
    response = await get_all_bible_books()

    # Assert the response matches the expected value
    assert response.success == expected_response.success
    assert response.data == expected_response.data

    # Assert the aggregate method was called once with the correct arguments
    mock_collection.aggregate.assert_called_once_with(
        [
            {'$group': {'_id': {'book': '$book', 'book_name': '$book_name'}}}
        ]
    )


@pytest.mark.asyncio
@patch("bff.src.services.search.search_bible_books_list.get_database")  # Make sure to patch the correct path
async def test_get_all_bible_books_error_handling(mock_get_database):
    mock_get_database.side_effect = PyMongoError("An error occurred with MongoDB")

    # Act
    _response = await get_all_bible_books()

    # Assertions
    # assert response.success is False
    assert "An error occurred with MongoDB" in _response.warnings
