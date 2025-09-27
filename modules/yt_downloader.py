import yt_dlp

def get_download_url(url, format="mp4"):
    ydl_opts = {"quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)  # <--- no download
        if format == "mp3":
            # pick best audio
            audio_formats = [f for f in info['formats'] if f.get('acodec') != 'none']
            best_audio = max(audio_formats, key=lambda f: f.get('abr', 0))
            return {"title": info["title"], "url": best_audio["url"], "format": "mp3"}
        else:
            # pick best video
            video_formats = [f for f in info['formats'] if f.get('vcodec') != 'none']
            best_video = max(video_formats, key=lambda f: f.get('height', 0))
            return {"title": info["title"], "url": best_video["url"], "format": "mp4"}
