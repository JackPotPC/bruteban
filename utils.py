from pathlib import Path
import logging
import sys

_LOGGER_NAME = "bruteban"

def setup_logger(
    level=logging.INFO,
    fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
):
    logger = logging.getLogger(_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger  # уже настроен

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger

def get_logger(name=None):
    base = logging.getLogger(_LOGGER_NAME)
    return base if name is None else base.getChild(name)

def find_file_by_name(directory: str, filename: str) -> Path | None:
    path = Path(directory)

    for file in path.iterdir():
        if file.is_file() and file.name == filename:
            return file.resolve()

    return None