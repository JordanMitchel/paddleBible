from kombu import Queue
from shared.src.ServiceBus.consumer import KombuConsumer
from shared.src.ServiceBus.producer import KombuProducer


def get_producer_service() -> KombuProducer:
    """Returns a producer service, allowing an optional connection injection."""
    return  KombuProducer()


def get_consumer_factory(queue: Queue):
    """Returns a consumer factory function that can instantiate a consumer for a given queue."""

    def get_consumer(callback=None):
        """Instantiates a consumer with the provided callback function."""

        def default_callback(body, message):
            """Default message processing callback."""
            print(f"Received message in {queue.name}: {body}")
            message.ack()
        return KombuConsumer(queue, callback or default_callback)

    return get_consumer  # Return the function itself
