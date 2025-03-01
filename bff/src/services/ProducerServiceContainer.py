from fastapi import Depends

from bff.src.services.BibleService import BibleService
from shared.src.ServiceBus.producer import KombuProducer


class ProducerServiceContainer:
    """Manages service dependencies except BibleService to avoid circular imports."""

    def __init__(self):
        self._producer_service = None

    def get_producer_service(self) -> KombuProducer:
        """Lazily initialize and return the producer service."""
        if self._producer_service is None:
            self._producer_service = KombuProducer()
        return self._producer_service


# Dependency injection function
async def get_service_container() -> ProducerServiceContainer:
    return ProducerServiceContainer()


async def get_bible_service(services=Depends(get_service_container)) -> BibleService:
    """Initialize BibleService using explicit dependencies."""
    return BibleService(
        producer=services.get_producer_service(),
    )
