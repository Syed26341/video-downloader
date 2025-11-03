import subprocess
from flask import Flask, request
from utils.logger import setup_logger
from utils.response import success_response, error_response

app = Flask(__name__)
logger = setup_logger()


def get_download_url(url, format="mp4"):
    """
    Returns the direct download URL without downloading the video.
    """
    try:
        # Select format
        if format == "mp3":
            ytdlp_format = "bestaudio/best"
        else:
            ytdlp_format = "best[ext=mp4]/best"

        command = [
            "/home/swxygjejiu/virtualenv/af.wradid.com/3.10/bin/yt-dlp",
            "--cookies", "/home/swxygjejiu/af.wradid.com/cookies.txt",
            "-f", ytdlp_format,
            "--get-url",
            url
        ]

        # Capture yt-dlp output safely
        result = subprocess.check_output(
            command,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace"  # Replace undecodable chars instead of crashing
        )

        direct_url = result.strip()

        if not direct_url:
            raise Exception("No downloadable URL found. The video might be restricted or private.")

        return {
            "original_url": url,
            "download_url": direct_url,
            "format": format
        }

    except subprocess.CalledProcessError as e:
        output = e.output if hasattr(e, "output") else str(e)
        logger.error(f"yt-dlp command failed: {output}")
        raise Exception("Failed to fetch download URL. Please check the video link or try again later.")
    except Exception as ex:
        logger.error(f"Unexpected error: {str(ex)}")
        raise


@app.route('/')
def home():
    return success_response(message="🎬 YouTube Video Downloader API is running smoothly 🚀")


@app.route('/download', methods=['POST'])
def download():
    """
    Accepts JSON { "url": "<video_url>", "format": "mp4|mp3" }
    and returns the direct downloadable link.
    """
    try:
        data = request.get_json(force=True)
        url = data.get('url')
        fmt = data.get('format', 'mp4').lower()

        if not url:
            return error_response("URL is required", 400)

        if fmt not in ['mp4', 'mp3']:
            return error_response("Invalid format. Use 'mp4' or 'mp3'", 400)

        video_data = get_download_url(url, format=fmt)
        return success_response(video_data, message="✅ Downloadable URL fetched successfully")

    except Exception as ex:
        logger.error(f"Download failed: {str(ex)}")
        return error_response(str(ex), 500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
