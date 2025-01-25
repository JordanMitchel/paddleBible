
from rabbitmq import RabbitMQ

def callback(ch, method, properties, body):
    print(f"Received {body}")



async  def consume_text():
    rabbitmq = RabbitMQ()
    rabbitmq.consume(callback)