from kombu import Exchange, Queue
#docker
BROKER_URL = "amqp://guest:guest@rabbitmq:5672//"
#local
# BROKER_URL = "amqp://guest:guest@localhost:5672//"


# Define a shared exchange
exchange = Exchange("bible_exchange", type="direct")

# Define queues with clear and structured names
ai_consuming_bff_requests = Queue("ai_consuming.bff.requests", exchange, routing_key="ai_consuming.bff.requests")
bff_consuming_ai_results = Queue("bff_consuming.ai.results", exchange, routing_key="bff_consuming.ai.results")
