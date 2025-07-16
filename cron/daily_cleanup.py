# cron/daily_cleanup.py

import os
import shutil
import time
from datetime import datetime, timedelta
from config import Config
from utils.logger import setup_logger

logger = setup_logger()

def delete_old_downloads():
    base_dir = Config.DOWNLOAD_DIR
    now = datetime.now()
    cutoff = now - timedelta(days=Config.DELETE_AFTER_DAYS)

    if not os.path.exists(base_dir):
        logger.info(f"No download directory found at {base_dir}")
        return

    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            try:
                folder_date = datetime.strptime(folder, "%Y-%m-%d")
                if folder_date < cutoff:
                    shutil.rmtree(folder_path)
                    logger.info(f"Deleted old folder: {folder_path}")
            except ValueError:
                logger.warning(f"Skipping folder with invalid date format: {folder_path}")

if __name__ == "__main__":
    logger.info("Starting daily cleanup...")
    delete_old_downloads()
    logger.info("Cleanup complete.")
