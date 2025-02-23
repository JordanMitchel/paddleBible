from unittest.mock import patch, AsyncMock, MagicMock

import pytest

from bff.src.app import app
from bff.src.routes.router_scripture import get_bible_books, get_bible_service
from bff.src.services.BibleService import BibleService
from bff.src.services.search.search_for_location_by_scripture import request_locations_using_scripture
from fastapi.testclient import TestClient
from shared.src.ServiceBus.producer import KombuProducer
from shared.src.models.scripture_result import BibleStructure, Scripture, Place, ResponseModel
from shared.tests.test_data.mock_data import mock_bible_books


@pytest.fixture
def mock_bible_service():
    """Fixture to create a mock of BibleService."""
    mock_service = AsyncMock(spec=BibleService)
    return mock_service

@pytest.mark.asyncio
@pytest.mark.requires_decouple
async def test_get_bible_books(mock_bible_service):
    # ✅ Override the FastAPI dependency
    app.dependency_overrides[get_bible_service] = lambda: mock_bible_service

    # Arrange
    bible_data = mock_bible_books  # Ensure this is predefined
    mock_bible_service.get_all_bible_books.return_value = bible_data

    # ✅ Use FastAPI's TestClient to send a request
    client = TestClient(app)

    # Act
    response = client.get("/BibleBooks")

    # Assert
    assert response.status_code == 200
    books = response.json()
    assert books["success"] is True
    assert books["data"] == bible_data.data

    # ✅ Ensure the method was called once
    mock_bible_service.get_all_bible_books.assert_called_once()

    # ✅ Clean up the dependency override
    app.dependency_overrides.clear()


