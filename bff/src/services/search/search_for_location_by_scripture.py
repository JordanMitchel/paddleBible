from kombu.exceptions import OperationalError, EncodeError

from shared.src.ServiceBus.producer import KombuProducer
from shared.src.models.scripture_result import ResponseModel


async def request_locations_using_scripture(verse: str, producer_service: KombuProducer) -> ResponseModel:
    if not verse:
        print("Received empty verse.")
        return ResponseModel(success=False, warnings="Received empty verse")

    try:
        await producer_service.send_message(verse, routing_key="ai_consuming.bff.requests")
        print(f"Verse '{verse}' pushed to Channel {producer_service.get_channel()}")
        return ResponseModel(success=True,data="successfully sent data")
    except OperationalError as e:  # Broker connection issues
        print(f"Message broker unavailable: {e}")
    except EncodeError as e:  # Serialization issues
        print(f"Failed to encode message: {e}")
    except Exception as e:  # Catch-all for unexpected errors
        print(f"Unexpected error while sending message: {e}")

    return ResponseModel(success=False, warnings="Failed data send")
