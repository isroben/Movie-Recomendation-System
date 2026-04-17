import logging
import os
from datetime import datetime

# Creating logs directory
LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        return logger
    
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(logging.INFO)

    consolse_handler = logging.StreamHandler()
    consolse_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

    formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")

    file_handler.setFormatter(formatter)
    consolse_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(consolse_handler)

    return logger