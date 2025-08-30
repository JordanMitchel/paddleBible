import pytest

from ml_service.src.services.service_bus.ProcessService import ProcessService


@pytest.fixture(scope="module")
def process_service():
    return ProcessService()


def test_sentiment_search_works(process_service):
    # arrange
    stub_str: str = "The Lord said to Moses in the Desert of Sinai"
    stub_sentiment: str = "xx_ent_wiki_sm"

    # act
    response = process_service.sentiment_search(stub_sentiment, stub_str)

    # assert
    assert len(response) == 1
    assert response[0] == 'Desert of Sinai'


def test_sentiment_search_empty_verse(process_service):
    # arrange
    stub_str: str = ""
    stub_sentiment: str = "xx_ent_wiki_sm"

    # act
    response = process_service.sentiment_search(stub_sentiment, stub_str)

    # assert
    assert len(response) == 0


def test_sentiment_search_empty_sentiment(process_service):
    # arrange
    stub_str: str = "Desert of Sinai"
    stub_sentiment: str = ""

    # act
    response = process_service.sentiment_search(stub_sentiment, stub_str)

    # assert
    assert len(response) == 0
