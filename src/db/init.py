from config import get_mongo_client, get_database

# Expose these utilities at the package level
__all__ = ["get_mongo_client", "get_database"]
