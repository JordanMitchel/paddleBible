import os
from typing import Type

from decouple import UndefinedValueError, RepositoryEnv, Config

env_name = os.getenv('ENVIRONMENT','local')
ENV_FILE_CONFIG = f'.///env.{env_name}'

def get_env_variable(key, default=None, cast_type=str, env_file=ENV_FILE_CONFIG):
    if env_file and os.path.exists(env_file):
        env_repo = RepositoryEnv(env_file)
        config = Config(env_repo)
    else:
        config = Config(repository=os.environ)

    try:
        # Fetch the key with optional casting and default fallback
        return config(key, default=default, cast=cast_type)
    except UndefinedValueError as exc:
        # Explicitly re-raise the exception with context
        raise EnvironmentError(f"The required environment variable '{key}' is not set.") from exc


def load_mongo_config():
    return {
        "url": get_env_variable("MONGO_DB_URL", "localhost"),
        "mongo_port": get_env_variable("MONGO_PORT", "27018",Type[int]),
        "db_collection": get_env_variable("DATABASE_NAME", "bibleData"),
        "db_username": get_env_variable("USER_NAME"),
        "db_password": get_env_variable("DB_PASSWORD"),
    }


def load_logging_config():
    return {
        "level": get_env_variable("LOG_LEVEL", "INFO"),
    }


def is_debug_mode():
    return get_env_variable("DEBUG_MODE", False, cast_type=Type[bool])
