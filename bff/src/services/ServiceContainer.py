from fastapi import Depends

from bff.src.services.BibleService import BibleService
from bff.src.services.ServiceBus.BFFKombuConsumer import BFFKombuConsumer
from shared.src.ServiceBus.producer import KombuProducer


class ServiceContainer:
    def __init__(self, bible_service: BibleService, producer_service: KombuProducer, consumer_service: BFFKombuConsumer):
        self.bible_service = bible_service
        self.producer_service = producer_service
        self.consumer_service = consumer_service

async def get_bible_service() -> BibleService:
    return BibleService()

def get_producer_service() -> KombuProducer:
    """Returns a producer service, allowing an optional connection injection."""
    return KombuProducer()

def get_consumer_service() -> BFFKombuConsumer:
    """Returns a consumer service instance."""
    return BFFKombuConsumer()

async def get_services(
    bible_service: BibleService = Depends(get_bible_service),
    producer_service: KombuProducer = Depends(get_producer_service),
    consumer_service: BFFKombuConsumer = Depends(get_consumer_service)  # ✅ Corrected
) -> ServiceContainer:
    return ServiceContainer(bible_service, producer_service, consumer_service)
