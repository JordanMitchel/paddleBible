from shared.src.ServiceBus.producer import KombuProducer

from shared.src.models.scripture_result import BibleStructure, ResponseModel


async def request_locations_using_scripture(verse: str, producer_service: KombuProducer) -> ResponseModel:
    if not verse:
        return ResponseModel(success=False,
                             data=BibleStructure(),
                             warnings="Empty verse no location found")

    # Send the message to the producer service
    await producer_service.send_message(verse, routing_key="ai_consuming.bff.requests")
    print(f"Verse {verse}, pushed to Channel {producer_service.get_channel()}")


