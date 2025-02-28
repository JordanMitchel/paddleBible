import asyncio
import json
import threading

from bff.src.services.ServiceBus.BFFKombuConsumer import BFFKombuConsumer
from domain.src.db.add_bible_to_mongo import insert_bible_store
from domain.src.db.add_coordinates_to_mongo import update_coordinates_collection_using_file
from shared.src.models.FileType import FileTypeEnum


async def run_kombu_tasks(app):
    print("✅ Connected to RabbitMQ")

    bff_consumer_service = BFFKombuConsumer()
    app.state.bff_consumer_service = bff_consumer_service  # Store in app state

    def start_consumer():
        """Run Kombu consumer in a separate thread."""
        bff_consumer_service.run()  # This must be a blocking method

    # Run consumer in a separate thread
    consumer_thread = threading.Thread(target=start_consumer, daemon=True)
    consumer_thread.start()

    print(f"✅ Kombu consumer listening on queue: {bff_consumer_service.queue.name}")


async def run_db_tasks():
    try:
        print("Seeding LonLats collection...")
        await update_coordinates_collection_using_file("domain/data/csv/biblicalLonLat2_formatted.csv", "LonLats")

        # await update_coordinates_collection_using_file("domain/data/csv/biblicalLonLat2_formatted.csv", "LonLats")
        print("Seeding Bible_ASV collection...")
        await insert_bible_store("domain/data/json/asv.json", FileTypeEnum.JSON, "Bible_ASV")
        print("Seeding completed successfully.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")


async def run_tasks(app):
    await run_kombu_tasks(app)
    await run_db_tasks()


