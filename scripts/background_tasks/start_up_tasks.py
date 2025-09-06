import json
import threading

from backendServices.bff.src.services.service_bus.BFFKombuConsumer import BFFKombuConsumer
from backendServices.domain.src.db.add_bible_to_mongo import insert_bible_store
from backendServices.domain.src.db.add_coordinates_to_mongo import update_coordinates_collection_using_file
from backendServices.shared.src.models.FileType import FileTypeEnum


# logger = get_logger()

async def run_kombu_tasks(app, logger):
    logger.info("✅ Starting Kombu consumer...")

    def start_kombu():
        """Run Kombu in a separate thread to avoid blocking FastAPI."""
        bff_consumer_service = BFFKombuConsumer()
        app.state.bff_consumer_service = bff_consumer_service
        bff_consumer_service.run()  # Blocking call

    thread = threading.Thread(target=start_kombu, daemon=True)
    thread.start()

    logger.info("✅ Kombu consumer thread started!")


async def run_db_tasks(logger):
    try:

        logger.info("Seeding LonLats collection...")
        await update_coordinates_collection_using_file("domain/data/csv/biblical_coordinates.csv", "LonLats")

        logger.info("Seeding Bible_ASV collection...")
        await insert_bible_store("domain/data/json/asv.json", FileTypeEnum.JSON, "Bible_ASV")
        logger.info("Seeding successful")

    except FileNotFoundError as e:
        logger.error("File not found", e)
    except json.JSONDecodeError as e:
        logger.error("Error decoding JSON", e)


async def run_tasks(app, logger):
    logger.info("🚀 Running background tasks...")  # Debug print
    try:
        await run_kombu_tasks(app, logger)
        await run_db_tasks(logger)

    except Exception as e:
        logger.error("🔥 Error in background tasks", e)


async def shutdown_tasks(app, logger):
    logger.info("🔄 Shutting down Kombu consumer...")
    bff_consumer_service = getattr(app.state, "bff_consumer_service", None)

    if bff_consumer_service:
        bff_consumer_service.should_stop = True
        bff_consumer_service.connection.close()
        logger.info("✅ Kombu consumer stopped cleanly.")
        logger.info("✅ Kombu consumer stopped cleanly.")
