import json
import threading
import os

from backendServices.bff.src.services.service_bus.BFFKombuConsumer import BFFKombuConsumer
from backendServices.domain.src.db.add_bible_to_mongo import insert_bible_store
from backendServices.domain.src.db.add_coordinates_to_mongo import update_coordinates_collection_using_file
from backendServices.shared.src.models.FileType import FileTypeEnum


# logger = get_logger()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_PATH = os.path.join(BASE_DIR, "../../domain/data/csv/biblical_coordinates.csv")
JSON_PATH = os.path.join(BASE_DIR, "../../domain/data/json/asv.json")

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
        await update_coordinates_collection_using_file(CSV_PATH, "LonLats")

        logger.info("Seeding Bible_ASV collection...")
        await insert_bible_store(JSON_PATH, FileTypeEnum.JSON, "Bible_ASV")
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
