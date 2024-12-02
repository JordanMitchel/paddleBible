import os

from decouple import  Config, RepositoryEnv
from motor.motor_asyncio import AsyncIOMotorClient

env_name = os.getenv('ENVIRONMENT','local')
env_file = f'.env.{env_name}'

# print(f"Using .env file: {env_file}")
# with open(env_file) as file:
#     print(file.read())
config = Config(RepositoryEnv(env_file))
# config = Config('.env.local')

DB_URL = config("MONGO_DB_URL")
DB_PORT = config("MONGO_PORT", cast=int)
DB_NAME = config("DATABASE_NAME")
DB_USERNAME = config("USER_NAME")
DB_PASSWORD = config("DB_PASSWORD")

MONGO_CLIENT = AsyncIOMotorClient(DB_URL, DB_PORT, username=DB_USERNAME, password=DB_PASSWORD)
DB = MONGO_CLIENT[DB_NAME]
