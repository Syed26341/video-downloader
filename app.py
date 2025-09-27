# app.py

from flask import Flask, request
from utils.logger import setup_logger
from utils.response import success_response, error_response
from modules.yt_downloader import get_download_url  # renamed function

app = Flask(__name__)
logger = setup_logger()

@app.route('/')
def home():
    return success_response(message="Video Downloader API is running 🚀")

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.get_json()
        url = data.get('url')
        format = data.get('format', 'mp4').lower()

        if not url:
            return error_response("URL is required", 400)

        if format not in ['mp4', 'mp3']:
            return error_response("Invalid format. Use 'mp4' or 'mp3'", 400)

        video_data = get_download_url(url, format=format)

        return success_response({
            "title": video_data["title"],
            "format": video_data["format"],
            "download_url": video_data["url"]   # <-- direct temporary URL
        }, message="Direct download URL generated")

    except Exception as ex:
        logger.error(f"Failed to process download request: {str(ex)}")
        return error_response(str(ex), 500)

if __name__ == '__main__':
    app.run(debug=True)
