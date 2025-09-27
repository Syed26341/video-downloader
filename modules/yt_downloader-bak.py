# modules/yt_downloader.py

import os
import subprocess
import uuid
import re
from datetime import datetime
from config import Config
from utils.logger import setup_logger

logger = setup_logger()

def sanitize_filename(title):
    """Make the video title filesystem-safe."""
    return re.sub(r'[^a-zA-Z0-9_\-]', '-', title).strip("-").lower()

def download_video(url, format="mp4"):
    try:
        # Prepare output path
        today_folder = Config.get_today_download_path()
        unique_id = datetime.now().strftime("%H-%M-%S") + "-" + str(uuid.uuid4())[:6]

        # Prepare output template
        output_template = os.path.join(today_folder, f"%(title).80s-{unique_id}.%(ext)s")

        # Format-specific options
        ytdlp_format = "bestvideo+bestaudio" if format == "mp4" else "bestaudio"
        postprocessor_args = []

        if format == "mp3":
            postprocessor_args = [
                "-x", "--audio-format", "mp3", "--audio-quality", "192K"
            ]

        command = [
            "yt-dlp",
            "-f", ytdlp_format,
            *postprocessor_args,
            "-o", output_template,
            url
        ]

        logger.info(f"Downloading from URL: {url}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        logger.info(f"Download complete: {result.stdout}")

        # Extract final filename from yt-dlp output
        downloaded_files = [
            f for f in os.listdir(today_folder)
            if os.path.isfile(os.path.join(today_folder, f)) and unique_id in f
        ]
        if not downloaded_files:
            raise Exception("Download succeeded but no file found.")

        downloaded_filename = downloaded_files[0]
        full_path = os.path.join(today_folder, downloaded_filename)

        return {
            "title": downloaded_filename,
            "format": format,
            "file_path": full_path,
            "url": url
        }

    except subprocess.CalledProcessError as e:
        logger.error(f"yt-dlp error: {e.stderr}")
        raise Exception("Video download failed.")
    except Exception as ex:
        logger.error(f"Unexpected error: {str(ex)}")
        raise
