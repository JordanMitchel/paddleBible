import os
from email.policy import default

from decouple import config, UndefinedValueError, RepositoryEnv
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
    try:
        if env_file:
            env_repo = RepositoryEnv(env_file)
            return config(key, default=default, cast=cast_type, repository=env_repo)
        else:
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
        "url": get_env_variable("DB_URL", "localhost"),
        "mongo_port": get_env_variable("MONGO_PORT", "27018"),
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
