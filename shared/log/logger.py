import asyncio
import os
import queue
import sys
import threading

from loguru import logger

from shared.log.LogProducer import LogProducer

SERVICE_NAME = os.getenv("SERVICE_NAME", "UNKNOWN_SERVICE")

# Initialize LogProducer
log_producer = LogProducer()

# Thread-safe queue for logging
log_queue = queue.Queue()


def log_sink():
    """Background worker that sends logs asynchronously."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    while True:
        try:
            log_message = log_queue.get()
            if log_message is None:  # Exit signal
                break

            loop.run_until_complete(log_producer.send_log(
                service=log_message["service"],
                level=log_message["level"],
                message=log_message["message"]
            ))
        except Exception as e:
            print(f"Log sink error: {e}")


# Start the background logging thread
log_thread = threading.Thread(target=log_sink, daemon=True)
log_thread.start()


def enqueue_log(message):
    """Puts log message in the queue."""
    record = message.record
    log_message = {
        "service": SERVICE_NAME,
        "level": record["level"].name,
        "message": record["message"],
    }
    log_queue.put(log_message)


# Configure Loguru logger
logger.remove()
logger.add(enqueue_log, format="{time} {level} {message}", level="INFO")  # ✅ No async issue now
logger.add(sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {message}", level="INFO")


async def setup_logger():
    """Ensures log producer is initialized before logging"""
    await log_producer.setup()


def get_logger():
    return logger
