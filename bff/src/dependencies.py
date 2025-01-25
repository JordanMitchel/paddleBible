from bff.src.services.service_bus.consumer_service import ConsumerService
from bff.src.services.service_bus.producer_service import ProducerService
from shared.src.ServiceBus.rabbitmq import RabbitMQ

def get_producer_service() -> ProducerService:
    rabbitmq = RabbitMQ()
    return ProducerService(rabbitmq)

def get_consumer_service() -> ConsumerService:
    rabbitmq = RabbitMQ()
    return ConsumerService(rabbitmq)