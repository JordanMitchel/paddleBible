from rabbitmq import RabbitMQ


async def push_text(message: str):

    rabbitmq = RabbitMQ()
    rabbitmq.publish(message)
    print(f"Sent message: {message}")
    rabbitmq.close()