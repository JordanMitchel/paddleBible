from datetime import datetime

from shared.src.ServiceBus.producer import KombuProducer
from shared.src.models.scripture_result import LogResponse
from shared.utils.config import LOG_ROUTING_KEY, BFF_SERVICE, ML_SERVICE


class SendLogsKombuProducer:
    """Encapsulates Kombu producer for log messages."""

    def __init__(self):
        """Initialize Kombu producer for logs."""
        self.kombu_producer = None

    async def setup(self):
        """Asynchronous initialization."""
        self.kombu_producer = KombuProducer()

    async def send_log(self, service, level, message, extra=None):
        """Send log message asynchronously using Kombu."""
        if not self.kombu_producer:
            raise ValueError("Producer not initialized.")

        log_entry = LogResponse(logService=service,logLevel=level,logMessage=message,error=extra)
        await self.kombu_producer.send_message(log_entry.model_dump(), LOG_ROUTING_KEY)

    async def send_bff_log(self, level, message, extra=None):
        await self.send_log(BFF_SERVICE, level, message, extra)

    async def send_ml_service_log(self, level, message, extra=None):
        await self.send_log(ML_SERVICE, level, message, extra)

    async def shutdown_logging(self):
        """Gracefully close the Kombu producer connection."""
        if self.kombu_producer:
            await self.kombu_producer.stop()

# Singleton instance (Optional: If you want to reuse it globally)
log_producer = SendLogsKombuProducer()

# Example usage

