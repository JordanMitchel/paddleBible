from shared.src.ServiceBus.ConsumerService import ConsumerService
from shared.src.ServiceBus.ProducerService import ProducerService
from shared.src.ServiceBus.RabbitMQ import RabbitMQ


def get_producer_service() -> ProducerService:
    rabbitmq = RabbitMQ()
    return ProducerService(rabbitmq)

def get_consumer_service() -> ConsumerService:
    rabbitmq = RabbitMQ()
    return ConsumerService(rabbitmq)