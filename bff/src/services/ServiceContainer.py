from bff.src.services.ServiceBus.BFFKombuConsumer import BFFKombuConsumer
from shared.src.ServiceBus.producer import KombuProducer


class ServiceContainer:
    """Manages service dependencies except BibleService to avoid circular imports."""

    def __init__(self):
        self._producer_service = None
        self._consumer_service = None

    def get_producer_service(self) -> KombuProducer:
        """Lazily initialize and return the producer service."""
        if self._producer_service is None:
            self._producer_service = KombuProducer()
        return self._producer_service

    def get_consumer_service(self) -> BFFKombuConsumer:
        """Lazily initialize and return the consumer service."""
        if self._consumer_service is None:
            self._consumer_service = BFFKombuConsumer()
        return self._consumer_service


# Dependency injection function
async def get_service_container() -> ServiceContainer:
    return ServiceContainer()
