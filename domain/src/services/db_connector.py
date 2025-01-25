from motor.motor_asyncio import AsyncIOMotorClient
from shared.utils.config import load_mongo_config


async def get_mongo_client():
    try:
        config = load_mongo_config()
        client = AsyncIOMotorClient(
            config["url"],
            username=config.get("db_username"),
            password=config.get("db_password"),)

        print(f"Connected to MongoDB at {config['url']}")
        return client
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise


async def get_database(client=None):
    try:
        config = load_mongo_config()
        if client is None:
            client = await get_mongo_client()
        db_name = config.get("db_collection", "default_db")
        return client[db_name]
    except Exception as e:
        print(f"Failed to get database: {e}")
        raise

async  def get_collection(collection_name: str, db_name: str = ""):
    try:
        config = load_mongo_config()
        if db_name == "":
            db_name = config.get("db_collection","default_db")
        db = await get_database(db_name)
        return db[collection_name]
    except Exception as e:
        print(f"Failed to get collection: {e}")
        raise

async def coll_is_populated(collection_name, db):
    collist = await db.list_collection_names()

    if collection_name in collist:
        print(f"The collection {collection_name} exists.")
        return True


async def insert_to_mongo(data, coll_name):
    db = await get_database()
    collection = await get_collection(coll_name)

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