import asyncio

from shared.src.models.scripture_result import ResponseModel


class ProcessorService:

    async def get_response_location(self, consumer_service):
        # Create an asyncio event to notify when the result is available
        result_event = asyncio.Event()  # This event will be set once the result is ready
        consumer_service.result_event = result_event  # Pass the event to the consumer

        # Run the consumer in the background
        await asyncio.create_task(consumer_service.start_consuming())  # Run the consumer asynchronously
        await result_event.wait()
        result = consumer_service.result_data

        if result is None:
            return ResponseModel(success=False, warnings="No data received after consuming message")

        print(f"result --> {result}")
        if result.warnings != '':
            return ResponseModel(success=True, data=result.data)
        return ResponseModel(success=False, warnings=result.warnings)