import pytest

from bff.src.services.search.search_for_location_by_scripture import get_locations_using_scripture
from shared.src.models.response import ResponseModel
from shared.src.models.scripture_result import BibleStructure


@pytest.mark.asyncio
async def test_get_locations_using_scripture_works():
    # arrange
    verse = ("Yet to his son I will give one tribe,"
             " that David my servant may always have a lamp"
             " before me in Jerusalem, the city where I have chosen to put my name.")

    # act
    response: ResponseModel = await get_locations_using_scripture(verse)

    # test
    assert response.success is True
    assert isinstance(response.data, BibleStructure)


@pytest.mark.asyncio
async def test_get_locations_using_scripture_without_location_produces_warning():
    # arrange
    verse = ("Therefore, there is now no condemnation for those who are in Christ Jesus,"
             "who do not walk according to the flesh, but according to the Spirit")

    # act
    response: ResponseModel = await get_locations_using_scripture(verse)

    # test
    assert response.success is True
    assert isinstance(response.data, BibleStructure)
    assert response.warnings == "No location found"
