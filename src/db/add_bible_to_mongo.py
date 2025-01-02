import json
import aiofiles
from src.db.config import get_database


async def insert_bible_store(json_path, coll_name):
    async with aiofiles.open(json_path) as file:
        data = await file.read()
        json_data = json.loads(data)

        data = json_data["verses"]

        await insert_to_mongo(data,coll_name)


async def insert_to_mongo(data, coll_name):
    db =await  get_database()
    collection = db[coll_name]
    collist = await db.list_collection_names()

    if coll_name in collist:
        print(f"The collection {coll_name} exists. Dropping it...")
        await collection.drop()  # Drop the collection asynchronously

    # Insert data based on whether it's a list or a single entry
    if isinstance(data, list):
        # Insert multiple documents asynchronously
        result = await collection.insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} documents.")
    else:
        # Insert a single document asynchronously
        await collection.insert_one(data)
        print("Inserted 1 document.")
    count = await collection.count_documents({})
    print(f"Current document count in {coll_name}: {count}")
