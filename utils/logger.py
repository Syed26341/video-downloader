# utils/logger.py

import logging
import os
from config import Config

def setup_logger():
    os.makedirs(Config.LOG_DIR, exist_ok=True)

    log_file = os.path.join(Config.LOG_DIR, 'app.log')

    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger("video_downloader")
