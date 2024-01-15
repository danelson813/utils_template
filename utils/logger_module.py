# utils/logger_module.py

import logging


def setup_logger():
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("data/info.log", 'w')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(pathname)s - %(lineno)d | %(levelname)s: %(message)s",
                                  datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    return logger