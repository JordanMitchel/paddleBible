from unittest.mock import AsyncMock, patch, MagicMock
import pytest
from typing import AsyncIterator

from src.models.response import ResponseModel
from src.search.search_bible_books_list import get_all_bible_books


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
@patch("src.search.searchBibleBooksList.get_database")  # Make sure to patch the correct path
async def test_get_all_bible_books(mock_get_database):
    # Mock data returned by the aggregate query
    mock_aggregate_data = [
        {'_id': {'book': 1, 'book_name': 'Genesis'}},
        {'_id': {'book': 2, 'book_name': 'Exodus'}},
        {'_id': {'book': 3, 'book_name': 'Leviticus'}},
    ]

    # Expected sorted response
    expected_response = ResponseModel(
        success=True,
        data=[
            {'book': 1, 'book_name': 'Genesis'},
            {'book': 2, 'book_name': 'Exodus'},
            {'book': 3, 'book_name': 'Leviticus'},
        ]
    )

    # Create mock collection
    mock_collection = AsyncMock()

    # Instead of returning a coroutine, directly set the return value to our AsyncIteratorMock
    mock_collection.aggregate = MagicMock(return_value=AsyncIteratorMock(mock_aggregate_data.copy()))

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
@patch("src.search.searchBibleBooksList.get_database")  # Make sure to patch the correct path
async def test_get_all_bible_books_error_handling(mock_get_database):
    mock_get_database.side_effect = Exception("Database connection error")

    #Act
    _response = await get_all_bible_books()

    #Assertions
    assert _response.success is False
