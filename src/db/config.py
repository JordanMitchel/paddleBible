from motor.motor_asyncio import AsyncIOMotorClient
from src.utils.config import load_mongo_config


async def get_mongo_client():
    """
    Creates and returns a MongoDB client instance.
    """
    try:
        config = load_mongo_config()
        client =  await AsyncIOMotorClient(config['url'], config['mongo_port'], username=config['db_username'], password=config['db_password'])
        print(f"Connected to MongoDB at {client.address()}")
        return client
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise


async def get_database(client=None):
    """
    Returns the specified MongoDB database.
    If no client is provided, a new one is created.
    """
    try:
        config = load_mongo_config()
        if client is None:
            client = await get_mongo_client()
        return client[config['db_collection']]
    except Exception as e:
        print(f"Failed to get database: {e}")
        raise

# Example Usage
if __name__ == "__main__":
    client = get_mongo_client()
    db = get_database(client)
    print(f"Using database: {db.name}")
