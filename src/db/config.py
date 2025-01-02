from motor.motor_asyncio import AsyncIOMotorClient
from src.utils.config import load_mongo_config

async def get_mongo_client():
    try:
        config = load_mongo_config()
        # client = AsyncIOMotorClient(
        #     config["url"],
        #     username=config.get("db_username"),
        #     password=config.get("db_password"),)
        username = config.get("db_username")
        password = config.get("db_password")
        url = config.get("url")
        port = config.get("mongo_port")
        client = AsyncIOMotorClient(
            f"mongodb://{username}:{password}@{url}:{port}"
        )
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
