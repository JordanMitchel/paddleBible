from src.db.AddBibleToMongo import insert_bible_store
from src.db.AddCoordinatesStore import insert_coordinates_store


async def run_tasks():
    try:
        print("Seeding LonLats collection...")
        await insert_coordinates_store("Data/csv/biblicalLonLat2_formatted.csv", "LonLats")
        print("Seeding Bible_ASV collection...")
        await insert_bible_store("Data/json/asv.json", "Bible_ASV")
        print("Seeding completed successfully.")
    except Exception as e:
        print(f"Error during run_tasks: {e}")