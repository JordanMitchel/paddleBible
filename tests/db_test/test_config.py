import pytest
from src.db.config import get_mongo_client
from unittest.mock import AsyncMock, patch
from src.db.config import get_database

@pytest.mark.asyncio
@patch("src.db.config.load_mongo_config")  # Fully qualified path for `load_mongo_config`
@patch("src.db.config.AsyncIOMotorClient")  # Fully qualified path for `AsyncIOMotorClient`
async def test_get_mongo_client_success(mock_motor_client, mock_load_config):
    # Mock the configuration
    mock_load_config.return_value = {
        "url": "mongodb://localhost",
        "mongo_port": 27018,
        "db_username": "test_user",
        "db_password": "test_password",
    }

    # Mock the MongoDB client
    mock_motor_client.return_value = AsyncMock()

    # Call the function
    client = await get_mongo_client()

    # Assertions
    mock_motor_client.assert_called_once_with(
        "mongodb://localhost", username="test_user", password="test_password"
    )
    assert client == mock_motor_client.return_value

@pytest.mark.asyncio
@patch("src.db.config.load_mongo_config")  # Fully qualified path for `load_mongo_config`
@patch("src.db.config.AsyncIOMotorClient")
async def test_get_mongo_client_failure(mock_load_config, mock_motor_client):
    # Mock the configuration
    mock_load_config.return_value = {
        "url": "mongodb://localhost",
        "db_username": "test_user",
        "db_password": "test_password",
    }

    # Simulate a connection error
    mock_motor_client.side_effect = Exception("Connection error")

    # Call the function and assert it raises an exception
    with pytest.raises(Exception, match="Connection error"):
        await get_mongo_client()


@pytest.mark.asyncio
@patch("src.db.config.load_mongo_config")  # Mocking the load_mongo_config function
@patch("src.db.config.AsyncIOMotorClient")  # Mocking the MongoDB client
async def test_get_database_success(mock_get_client, mock_load_config):
    # Mock the configuration returned by load_mongo_config
    mock_load_config.return_value = {
        "url": "mongodb://localhost",
        "mongo_port": 27018,
        "db_username": "test_user",
        "db_password": "test_password",
        "db_collection": "test_db"  # Add db_collection key
    }

    # Mock the MongoDB client
    mock_client = AsyncMock()
    mock_get_client.return_value = mock_client

    # Call the function
    db = await get_database()

    # Assertions
    mock_get_client.assert_called_once()  # Ensure the client was created
    assert db == mock_client["test_db"]   # Ensure the correct db is returned

@pytest.mark.asyncio
@patch("src.db.config.load_mongo_config")
@patch("src.db.config.get_mongo_client")
async def test_get_database_failure(mock_load_config, mock_get_client):
    # Mock the configuration
    mock_load_config.return_value = {
        "db_collection": "test_db",
    }

    # Simulate a client creation error
    mock_get_client.side_effect = Exception("Client creation failed")

    # Call the function and assert it raises an exception
    with pytest.raises(Exception, match="Client creation failed"):
        await get_database()