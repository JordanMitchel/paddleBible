import json

from src.db.add_bible_to_mongo import insert_bible_store
from src.db.add_coordinates_store import insert_coordinates_store


async def run_tasks():
    try:
        print("Seeding LonLats collection...")
        await insert_coordinates_store("Data/csv/biblicalLonLat2_formatted.csv", "LonLats")
        print("Seeding Bible_ASV collection...")
        await insert_bible_store("Data/json/asv.json", "Bible_ASV")
        print("Seeding completed successfully.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
