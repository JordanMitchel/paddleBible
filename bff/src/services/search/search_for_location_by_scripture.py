from bff.src.services.service_bus.producer_service import ProducerService
from shared.src.ServiceBus.publish_message import push_text
from shared.src.models.response import ResponseModel
from shared.src.models.scripture_result import BibleStructure, Place


async def get_locations_using_scripture(verse: str, producer_service: ProducerService) -> ResponseModel:
    if not verse:
        return ResponseModel(success=False,
                             data=BibleStructure(),
                             warnings="Empty verse no location found")

    queue_name = "locations_queue"
    producer_service.send_message(queue_name,verse)
    print(f"Verse pushed to {queue_name}: {verse}")
    # result = await push_text(verse)
    try:
        result = await get_result_from_consumer(queue_name, verse)
        if result.warnings != '':
            return ResponseModel(success=True, data=result.data)
        return ResponseModel(success=False, warnings=result.warnings)
    except TimeoutError:
        return ResponseModel(success=False, warnings="Timeout: No response from consumer")



