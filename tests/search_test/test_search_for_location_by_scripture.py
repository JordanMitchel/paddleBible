from src.search.search_for_location_by_scripture import strip_locations_of_unnecessary_words


def test_strip_locations_of_unnecessary_words():
    # Arrange
    stub_locations = ['hello', 'west', 'North', 'bye']

    # Act
    response = strip_locations_of_unnecessary_words(stub_locations)

    # Assert
    assert len(response) == 2


def test_strip_locations_of_unnecessary_words_no_words():
    # Arrange
    stub_locations = []

    # Act
    response = strip_locations_of_unnecessary_words(stub_locations)

    # Assert
    assert len(response) == 0


def test_strip_locations_of_unnecessary_words_no_unnecessary_words():
    # Arrange
    stub_locations = ['west-bank', 'london', 'Spain']

    # Act
    response = strip_locations_of_unnecessary_words(stub_locations)

    # Assert
    assert len(response) == 3
