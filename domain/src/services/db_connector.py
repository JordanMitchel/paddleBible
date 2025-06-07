from collections.abc import Mapping

from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

from shared.utils.config import load_mongo_config


async def get_mongo_client() -> AsyncIOMotorClient[Mapping[str, any]]:
    try:
        config = load_mongo_config()
        client = AsyncIOMotorClient(
            config["url"],
            username=config.get("db_username"),
            password=config.get("db_password"), )

        logger.info(f"Connected to MongoDB at {config['url']}")
        return client
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise

def get_sync_mongo_client():
    try:
        config = load_mongo_config()
        client = MongoClient(
            config["url"],
            username=config.get("db_username"),
            password=config.get("db_password"))
        logger.debug(f"Connected to MongoDB at {config['url']}")
        return client
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise

async def get_database(db_name="db_collection",client=None):
    try:
        config = load_mongo_config()
        logger.debug(f"MongoDB Config: {config}")  # Debugging line

        if client is None:
            client = await get_mongo_client()
        config_db_name = str(config.get(db_name, "default_db"))
        return client[config_db_name]
    except Exception as e:
        logger.error(f"Failed to get db: {e}")

        raise


async def get_collection(collection_name: str, db_name="db_collection"):
    try:

        db = await get_database(db_name)
        return db[collection_name]
    except Exception as e:
        logger.error(f"Failed to get collection: {e}")

        raise


async def coll_is_populated(collection_name, db):
    collist = await db.list_collection_names()

    if collection_name in collist:
        return True


async def insert_to_mongo_if_coll_empty(data, coll_name):
    collection = await get_collection(coll_name)

    count = await collection.count_documents({})
    if count > 0:
        logger.debug(f"Collection '{coll_name}' is not empty. Skipping insert.")
        return

    if isinstance(data, list):
        # Insert multiple documents asynchronously
        result = await collection.insert_many(data)
        logger.info(f"Inserted {len(result.inserted_ids)} documents.")
    else:
        # Insert a single document asynchronously
        await collection.insert_one(data)
    count = await collection.count_documents({})
    logger.debug(f"Current document count in {coll_name}: {count}")
