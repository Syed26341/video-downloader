# config.py

import os
from datetime import datetime

class Config:
    # Base project directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Folder to store all downloaded videos
    DOWNLOAD_DIR = os.path.join(BASE_DIR, 'downloads')

    # Folder to store logs
    LOG_DIR = os.path.join(BASE_DIR, 'logs')

    # Cleanup config
    DELETE_AFTER_DAYS = 1  # Auto-delete files older than this

    @staticmethod
    def get_today_download_path():
        """Return today's download folder path like downloads/2025-07-14"""
        today = datetime.now().strftime("%Y-%m-%d")
        path = os.path.join(Config.DOWNLOAD_DIR, today)
        os.makedirs(path, exist_ok=True)
        return path
