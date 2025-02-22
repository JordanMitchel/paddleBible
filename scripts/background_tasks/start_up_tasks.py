import json

from domain.src.db.add_bible_to_mongo import insert_bible_store
from domain.src.db.add_coordinates_to_mongo import update_coordinates_collection_using_file
from shared.src.models.FileType import FileTypeEnum


async def run_tasks():
    try:
        print("Seeding LonLats collection...")
        await update_coordinates_collection_using_file("domain/data/csv/biblicalLonLat2_formatted.csv", "LonLats")

        # await update_coordinates_collection_using_file("domain/data/csv/biblicalLonLat2_formatted.csv", "LonLats")
        print("Seeding Bible_ASV collection...")
        await insert_bible_store("domain/data/json/asv.json",FileTypeEnum.JSON, "Bible_ASV")
        print("Seeding completed successfully.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
