from shared.src.ServiceBus.consumer import KombuConsumer
from shared.src.ServiceBus.producer import KombuProducer
from shared.src.models.response import ResponseModel
from shared.src.models.scripture_result import BibleStructure


async def get_locations_using_scripture(verse: str, producer_service: KombuProducer, consumer_service: KombuConsumer) -> ResponseModel:
    if not verse:
        return ResponseModel(success=False,
                             data=BibleStructure(),
                             warnings="Empty verse no location found")

    #put queue_name in env file
    producer_service.send_message(verse, routing_key="bff_key")
    print(f"Verse {verse}, pushed to Channel {producer_service.channel}")
    # result = await push_text(verse)
    try:
        result = await consumer_service.start()
        if result.warnings != '':
            return ResponseModel(success=True, data=result.data)
        return ResponseModel(success=False, warnings=result.warnings)
    except TimeoutError:
        return ResponseModel(success=False, warnings="Timeout: No response from consumer")



