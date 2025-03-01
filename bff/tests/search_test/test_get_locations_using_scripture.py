from unittest.mock import MagicMock, AsyncMock, patch

import pytest

from bff.src.services.search.search_for_location_by_scripture import request_locations_using_scripture
from shared.src.ServiceBus.producer import KombuProducer
from shared.src.models.scripture_result import BibleStructure, ResponseModel, Scripture, Place, ScriptureRequest


@pytest.mark.asyncio
async def test_request_locations_using_scripture_sends_request_with_good_scripture():
    # Arrange
    mock_scripture = Scripture(book="book1", chapter=1, verse={1: "verse1"})
    mock_scripture_request = ScriptureRequest(clientId= "test-1",data=mock_scripture)
    mock_producer_service = MagicMock(spec=KombuProducer)  # ✅ Properly mock KombuProducer
    mock_producer_service.send_message = AsyncMock()  # ✅ Mock async method
    mock_producer_service.get_channel = MagicMock(return_value="mock_channel")  # ✅ Mock get_channel


    # Act
    publish_scripture = await request_locations_using_scripture(mock_scripture_request, mock_producer_service)

    # Assert
    assert publish_scripture is True

    # ✅ Verify producer was called correctly
    mock_producer_service.send_message.assert_awaited_once_with(mock_scripture_request.model_dump(),
                                                                routing_key="ai_consuming.bff.requests")
    mock_producer_service.get_channel.assert_called_once()


@pytest.mark.asyncio
async def test_request_locations_using_scripture_returns_warning_with_empty_scripture():
    # Arrange
    verse = ""
    mock_producer_service = MagicMock(spec=KombuProducer)  # ✅ Properly mock KombuProducer
    mock_producer_service.send_message = AsyncMock()  # ✅ Mock async method
    mock_producer_service.get_channel = MagicMock(return_value="mock_channel")  # ✅ Mock get_channel

    # Act
    publish_scripture = await request_locations_using_scripture(verse, mock_producer_service)

    # Assert
    assert publish_scripture is False
    mock_producer_service.send_message.assert_not_awaited()
    mock_producer_service.get_channel.assert_not_called()
