import sys

from loguru import logger

logger.remove()  # Remove default Loguru handler
logger.add(sys.stdout, format="{time} | {level} | {message}", level="INFO")