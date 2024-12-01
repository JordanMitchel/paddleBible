from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient


DB_URL = config("MONGO_DB_URL")
DB_PORT = config("MONGO_PORT", cast=int)
DB_NAME = config("DATABASE_NAME")
DB_USERNAME = config("USER_NAME")
DB_PASSWORD = config("DB_PASSWORD")

MONGO_CLIENT = AsyncIOMotorClient(DB_URL, DB_PORT, username=DB_USERNAME, password=DB_PASSWORD)
DB = MONGO_CLIENT[DB_NAME]
