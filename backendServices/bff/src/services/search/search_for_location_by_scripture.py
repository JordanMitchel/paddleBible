import logging

from kombu.exceptions import OperationalError, EncodeError

from backendServices.shared.src.ServiceBus.producer import KombuProducer
from backendServices.shared.src.models.scripture_result import ScriptureRequest
from backendServices.shared.utils.config import ML_ROUTING_KEY


async def request_locations_using_scripture(request: ScriptureRequest, producer_service: KombuProducer) -> bool:
    if not request:
        print("Received empty request.")
        return False

    try:
        await producer_service.send_message(request.model_dump(), routing_key=ML_ROUTING_KEY)
        logging.info(f"Verse: %s' pushed to Channel %s", request.model_dump(), producer_service.get_channel())
        return True
    except OperationalError as e:  # Broker connection issues
        logging.error("Message broker unavailable: %s",e)
    except EncodeError as e:  # Serialization issues
        logging.error("Failed to encode message: %s", e)
    except Exception as e:  # Catch-all for unexpected errors
        logging.error("Unexpected error while sending message: %s, e")

    return False
