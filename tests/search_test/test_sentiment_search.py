from src.search.search_for_location_by_scripture import sentiment_search


def test_sentiment_search_works():
    # arrange
    stub_str: str = "The Lord said to Moses in the Desert of Sinai"
    stub_sentiment: str = "xx_ent_wiki_sm"

    # act
    response = sentiment_search(stub_sentiment, stub_str)

    # assert
    assert len(response) == 1
    assert response[0] == 'Desert of Sinai'


def test_sentiment_search_empty_verse():
    # arrange
    stub_str: str = ""
    stub_sentiment: str = "xx_ent_wiki_sm"

    # act
    response = sentiment_search(stub_sentiment, stub_str)

    # assert
    assert len(response) == 0


def test_sentiment_search_empty_sentiment():
    # arrange
    stub_str: str = "Desert of Sinai"
    stub_sentiment: str = ""

    # act
    response = sentiment_search(stub_sentiment, stub_str)

    # assert
    assert len(response) == 0
