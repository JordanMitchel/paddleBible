from kombu.exceptions import OperationalError, EncodeError

from shared.src.ServiceBus.producer import KombuProducer
from shared.src.models.scripture_result import ScriptureRequest


async def request_locations_using_scripture(request: ScriptureRequest, producer_service: KombuProducer) -> bool:
    if not request:
        print("Received empty request.")
        return False

    try:
        await producer_service.send_message(request.model_dump(), routing_key="ai_consuming.bff.requests")
        print(f"Verse: '{request.model_dump()}' pushed to Channel {producer_service.get_channel()}")
        return True
    except OperationalError as e:  # Broker connection issues
        print(f"Message broker unavailable: {e}")
    except EncodeError as e:  # Serialization issues
        print(f"Failed to encode message: {e}")
    except Exception as e:  # Catch-all for unexpected errors
        print(f"Unexpected error while sending message: {e}")

    return False
