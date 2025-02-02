from shared.src.ServiceBus.RabbitMQ import RabbitMQ


class ProducerService:
    def __init__(self, rabbitmq: RabbitMQ):
        self.rabbitmq = rabbitmq

    def send_message(self, queue_name, message):
        self.rabbitmq.publish(queue_name, message)
