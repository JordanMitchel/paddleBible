import asyncio
import json
import threading

from bff.src.services.service_bus.BFFKombuConsumer import BFFKombuConsumer
from domain.src.db.add_bible_to_mongo import insert_bible_store
from domain.src.db.add_coordinates_to_mongo import update_coordinates_collection_using_file
from shared.log.send_logs import log_producer
from shared.src.models.FileType import FileTypeEnum
from shared.src.models.scripture_result import LogLevel


async def run_kombu_tasks(app):
    print("✅ Starting Kombu consumer...")

    def start_kombu():
        """Run Kombu in a separate thread to avoid blocking FastAPI."""
        bff_consumer_service = BFFKombuConsumer()
        app.state.bff_consumer_service = bff_consumer_service
        bff_consumer_service.run()  # Blocking call

    thread = threading.Thread(target=start_kombu, daemon=True)
    thread.start()

    print("✅ Kombu consumer thread started!")


async def run_db_tasks():
    try:

        await log_producer.send_bff_log(LogLevel.INFO, "Seeding LonLats collection...")
        await update_coordinates_collection_using_file("domain/data/csv/biblical_coords.csv", "LonLats")

        await log_producer.send_bff_log(LogLevel.INFO, "Seeding Bible_ASV collection...")
        await insert_bible_store("domain/data/json/asv.json", FileTypeEnum.JSON, "Bible_ASV")
        await log_producer.send_bff_log(LogLevel.INFO, "Seeding successful")

    except FileNotFoundError as e:
        await log_producer.send_bff_log(LogLevel.ERROR,"File not found",e)
    except json.JSONDecodeError as e:
        await log_producer.send_bff_log(LogLevel.ERROR,"Error decoding JSON",e)


async def run_tasks(app):
    print("🚀 Running background tasks...")  # Debug print
    try:
        await asyncio.gather(run_db_tasks(), run_kombu_tasks(app))
        await log_producer.send_bff_log(LogLevel.INFO,"✅ Background tasks started successfully!")

    except Exception as e:
        await log_producer.send_bff_log(LogLevel.ERROR,"🔥 Error in background tasks",e)



async def shutdown_tasks(app):
    print("🔄 Shutting down Kombu consumer...")
    bff_consumer_service = getattr(app.state, "bff_consumer_service", None)

    if bff_consumer_service:
        bff_consumer_service.should_stop = True
        bff_consumer_service.connection.close()
        print("✅ Kombu consumer stopped cleanly.")
        await log_producer.send_bff_log(LogLevel.INFO,"✅ Kombu consumer stopped cleanly.")
    await log_producer.shutdown_logging()
