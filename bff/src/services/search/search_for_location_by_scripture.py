

from shared.src.ServiceBus.ConsumerService import process_message, ConsumerService
from shared.src.ServiceBus.ProducerService import ProducerService
from shared.src.models.response import ResponseModel
from shared.src.models.scripture_result import BibleStructure


async def get_locations_using_scripture(verse: str, producer_service: ProducerService, consumer_service: ConsumerService) -> ResponseModel:
    if not verse:
        return ResponseModel(success=False,
                             data=BibleStructure(),
                             warnings="Empty verse no location found")

    #put queue_name in env file
    queue_name = "locations_queue"
    producer_service.send_message(queue_name,verse)
    print(f"Verse pushed to {queue_name}: {verse}")
    # result = await push_text(verse)
    try:
        result = await consumer_service.start_consuming(queue_name, process_message)
        if result.warnings != '':
            return ResponseModel(success=True, data=result.data)
        return ResponseModel(success=False, warnings=result.warnings)
    except TimeoutError:
        return ResponseModel(success=False, warnings="Timeout: No response from consumer")



