import pytest
from unittest.mock import AsyncMock

from bff.src.services.search.search_scripture import get_scripture_using_book_and_verse
from shared.src.models.scripture_result import ResponseModel, Scripture

@pytest.mark.asyncio
async def test_get_scripture_using_book_and_verse(mocker):
    # Setup test response
    test_doc = {
        "book_name": "John",
        "chapter": 1,
        "verse": 1,
        "text": "In the beginning was the Word, and the Word was with God, and the Word was God."
    }

    # Create mock collection
    mock_collection = AsyncMock()
    mock_cursor = AsyncMock()
    mock_cursor.to_list.return_value = [test_doc]
    mock_collection.find.return_value = mock_cursor

    # Mock get_collection
    mocker.patch('domain.src.services.db_connector.get_collection', return_value=mock_collection)

    # Test data
    bible_version = "KJV"
    book_num = 40  # John
    chapter = 1
    verse_num = 1

    # Execute function
    response = await get_scripture_using_book_and_verse(bible_version, book_num, chapter, verse_num)

    # Assert results
    assert response.success is True
    assert response.data == ResponseModel(
        success=True,
        data=Scripture(
            book="John",
            chapter=1,
            verse={1: "In the beginning was the Word, and the Word was with God, and the Word was God."}
        )
    )