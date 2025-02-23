from shared.src.ServiceBus.producer import KombuProducer


async def request_locations_using_scripture(verse: str, producer_service: KombuProducer) -> bool:
    if not verse:
        print("Received empty verse.")
        return False

    try:
        await producer_service.send_message(verse, routing_key="ai_consuming.bff.requests")
        print(f"Verse '{verse}' pushed to Channel {producer_service.get_channel()}")
        return True
    except Exception as e:  # ✅ Catch specific exceptions
        print(f"Failed to send message: {e}")
        return False


