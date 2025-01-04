import os

from decouple import Config, RepositoryEnv

env_name = os.getenv('ENVIRONMENT', 'local')
ENV_FILE = f'.env.{env_name}'
config = Config(RepositoryEnv(ENV_FILE))

DB_URL = config("MONGO_DB_URL")
DB_PORT = config("MONGO_PORT", cast=int)
DB_NAME = config("DATABASE_NAME")
DB_USERNAME = config("USER_NAME")
DB_PASSWORD = config("DB_PASSWORD")

# Sentiment Analysis Configuration
# SENTIMENT_API_KEY = config("SENTIMENT_API_KEY", default=None)

# Logging Configuration
LOG_LEVEL = config("LOG_LEVEL", default="INFO")

# Additional Configurations
DEBUG_MODE = config("DEBUG_MODE", default=False, cast=bool)
