from fastapi import Depends

from backendServices.bff.src.services.BibleService import BibleService
from backendServices.bff.src.services.queries.search_bible_books_list import BibleQuery
from backendServices.shared.src.ServiceBus.producer import KombuProducer


class ProducerServiceContainer:
    """Manages service dependencies except BibleService to avoid circular imports."""

    def __init__(self):
        self._producer_service = None
        self._bible_query_service = None  # ✅ add missing attribute

    def get_producer_service(self) -> KombuProducer:
        """Lazily initialize and return the KombuProducer."""
        if self._producer_service is None:
            self._producer_service = KombuProducer()
        return self._producer_service

    def get_bibleQuery_service(self) -> BibleQuery:
        """Lazily initialize and return the BibleQueryService."""
        if self._bible_query_service is None:
            self._bible_query_service = BibleQuery()
        return self._bible_query_service


# Dependency injection function
async def get_service_container() -> ProducerServiceContainer:
    return ProducerServiceContainer()


async def get_bible_service(
    services: ProducerServiceContainer = Depends(get_service_container),
) -> BibleService:
    """Initialize BibleService using explicit dependencies."""
    return BibleService(
        producer=services.get_producer_service(),
        bible_queryHandler=services.get_bibleQuery_service(),
    )
