import os

from decouple import UndefinedValueError, RepositoryEnv, Config
from kombu import Exchange

env_name = os.getenv('ENVIRONMENT', 'local')
# ENV_FILE_CONFIG = f'env.{env_name}'  # Fixed path
ENV_FILE_CONFIG = f'./env.{env_name}'  # Fixed path
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
# env_file2 = os.path.join(BASE_DIR, ".env")

BROKER_URL = "amqp://guest:guest@rabbitmq:5672//"
# local
# BROKER_URL = "amqp://guest:guest@localhost:5672//"
# Define a shared exchange
EXCHANGE = Exchange("bible_exchange", type="direct")


def get_env_variable(key, default=None, cast_type=str, env_file=ENV_FILE_CONFIG):
    """Fetches environment variables with optional casting and a default fallback."""
    if env_file and os.path.exists(env_file):
        env_repo = RepositoryEnv(env_file)
        config = Config(env_repo)
    else:
        config = Config(repository=os.environ)

    try:
        return config(key, default=default, cast=cast_type)
    except UndefinedValueError as exc:
        raise EnvironmentError(f"The required environment variable '{key}' is not set.") from exc


def load_mongo_config() -> {}:
    """Loads MongoDB configuration from environment variables."""
    return {
        "url": get_env_variable("MONGO_DB_URL", "mongodb_container"),
        "mongo_port": get_env_variable("MONGO_PORT", 27017, int),  # Fixed casting
        "db_collection": get_env_variable("DATABASE_NAME", "bibleData"),
        "db_username": get_env_variable("USER_NAME", "root"),  # Handled optional values
        "db_password": get_env_variable("DB_PASSWORD", "rootPassword"),
    }


def load_logging_config():
    """Loads logging configuration from environment variables."""
    return {
        "level": get_env_variable("LOG_LEVEL", "INFO"),
    }


def is_debug_mode():
    """Checks if the application is running in debug mode."""
    return get_env_variable("DEBUG_MODE", False, bool)  # Fixed casting
