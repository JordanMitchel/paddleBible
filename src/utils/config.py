import os
from email.policy import default

from decouple import UndefinedValueError, RepositoryEnv, Config

env_name = os.getenv('ENVIRONMENT','local')
ENV_FILE_CONFIG = f'.env.{env_name}'

def get_env_variable(key, default=None, cast_type=str, env_file=ENV_FILE_CONFIG):
    """
    Retrieves an environment variable and casts it to the desired type.
    Raises an error if the variable is not defined and no default is provided.

    Args:
        key (str): The environment variable key.
        default (Any): The default value if the key is not found.
        cast_type (type): The type to cast the variable to.

    Returns:
        Any: The value of the environment variable, cast to the specified type.
    """
    if env_file and os.path.exists(env_file):
        env_repo = RepositoryEnv(env_file)
        config = Config(env_repo)
    else:
        config = Config()

    try:
        # Fetch the key with optional casting and default fallback
        return config(key, default=default, cast=cast_type)
    except UndefinedValueError:
        raise EnvironmentError(f"The required environment variable '{key}' is not set.")


def load_mongo_config():
    """
    Loads MongoDB configuration from environment variables.

    Returns:
        dict: A dictionary containing MongoDB connection details.
    """
    return {
        "url": get_env_variable("MONGO_DB_URL", "localhost"),
        "mongo_port": get_env_variable("MONGO_PORT", "27018",int),
        "db_collection": get_env_variable("DATABASE_NAME", "bibleData"),
        "db_username": get_env_variable("USER_NAME"),
        "db_password": get_env_variable("DB_PASSWORD"),
    }


def load_logging_config():
    """
    Loads logging configuration from environment variables.

    Returns:
        dict: A dictionary containing logging configuration details.
    """
    return {
        "level": get_env_variable("LOG_LEVEL", "INFO"),
    }


def is_debug_mode():
    """
    Checks if the application is running in debug mode.

    Returns:
        bool: True if debug mode is enabled, otherwise False.
    """
    return get_env_variable("DEBUG_MODE", False, cast_type=bool)
