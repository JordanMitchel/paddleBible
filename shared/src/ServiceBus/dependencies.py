from shared.src.ServiceBus.producer import KombuProducer


def get_producer_service() -> KombuProducer:
    """Returns a producer service, allowing an optional connection injection."""
    return  KombuProducer()



