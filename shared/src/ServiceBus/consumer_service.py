from shared.src.ServiceBus.rabbitmq import RabbitMQ


def process_message(ch, method, properties, body):
    print(f"Processing message: {body.decode()}")
    # Add business logic here


class ConsumerService:
    def __init__(self, rabbitmq: RabbitMQ):
        self.rabbitmq = rabbitmq

    def start_consuming(self, queue_name, message):
        self.rabbitmq.consume(queue_name, process_message)
