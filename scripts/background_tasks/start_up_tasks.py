import asyncio
import json
import threading

from bff.src.services.ServiceBus.BFFKombuConsumer import BFFKombuConsumer
from domain.src.db.add_bible_to_mongo import insert_bible_store
from domain.src.db.add_coordinates_to_mongo import update_coordinates_collection_using_file
from shared.src.models.FileType import FileTypeEnum


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
        print("Seeding LonLats collection...")
        await update_coordinates_collection_using_file("domain/data/csv/biblicalLonLat2_formatted.csv", "LonLats")

        print("Seeding Bible_ASV collection...")
        await insert_bible_store("domain/data/json/asv.json", FileTypeEnum.JSON, "Bible_ASV")
        print("Seeding completed successfully.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")


async def run_tasks(app):
    print("🚀 Running background tasks...")  # Debug print
    try:
        await asyncio.gather(run_db_tasks(), run_kombu_tasks(app))
        print("✅ Background tasks started successfully!")
    except Exception as e:
        print(f"🔥 Error in background tasks: {e}")


async def shutdown_tasks(app):
    print("🔄 Shutting down Kombu consumer...")
    bff_consumer_service = getattr(app.state, "bff_consumer_service", None)

    if bff_consumer_service:
        bff_consumer_service.should_stop = True
        bff_consumer_service.connection.close()
        print("✅ Kombu consumer stopped cleanly.")
