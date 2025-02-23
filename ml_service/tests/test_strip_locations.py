import pytest

from ml_service.src.services.service_bus.ProcessService import ProcessService

@pytest.fixture(scope="module")
def process_service():
    return ProcessService()


def test_strip_locations_of_unnecessary_words(process_service):
    # Arrange
    stub_locations = ['hello', 'west', 'North', 'bye']

    # Act
    response = process_service.strip_locations_of_unnecessary_words(stub_locations)

    # Assert
    assert len(response) == 2


def test_strip_locations_of_unnecessary_words_no_words(process_service):
    # Arrange
    stub_locations = []

    # Act
    response = process_service.strip_locations_of_unnecessary_words(stub_locations)

    # Assert
    assert len(response) == 0


def test_strip_locations_of_unnecessary_words_no_unnecessary_words(process_service):
    # Arrange
    stub_locations = ['west-bank', 'london', 'Spain']

    # Act
    response = process_service.strip_locations_of_unnecessary_words(stub_locations)

    # Assert
    assert len(response) == 3
