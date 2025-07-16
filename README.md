# 🎥 Video Downloader Platform (Flask + yt-dlp)

This is a modular, secure, and extendable video downloader platform using Python (Flask) and `yt-dlp`.  
It allows users to download videos or audio from YouTube, Facebook, and Instagram Reels by pasting a link.

---

## 📁 Project Folder Structure

```
video_downloader/
├── app.py                   # Main Flask application
├── config.py                # Configurations (download paths, settings)
├── requirements.txt         # Python dependencies
│
├── downloads/               # Main download folder (auto-deleted daily)
│   ├── 2025-07-14/          # Folder by date (YYYY-MM-DD)
│   │   ├── video-title.mp4
│   │   ├── audio-title.mp3
│   │   └── fallback-14-52-01.mp4
│
├── logs/                    # Logs directory
│   └── app.log              # All system and error logs
│
├── utils/                   # Utilities (shared functions)
│   ├── logger.py            # Logging setup
│   └── response.py          # JSON helpers for success/error
│
├── modules/                 # Feature-specific downloaders
│   └── yt_downloader.py     # Handles YouTube/Facebook/Instagram downloads
│
└── cron/                    # Scheduled job scripts
    └── daily_cleanup.py     # Deletes folders older than 1 day
```

---

## ✅ Features

- 📥 Download from YouTube, Facebook, and Instagram
- 🎧 Supports MP4 (video) and MP3 (audio)
- 🗂 Organized by date to prevent clutter
- 🔁 Auto-deletion of old files to save space
- ⚙️ Easily extendable (add more modules)
- 🔒 Safe from name collisions and secure subprocess handling

---

## 🚀 Run the Project

```bash
cd video_downloader
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

---

## 🧹 Cleanup Recommendation

Use the `daily_cleanup.py` script to auto-delete files older than 1 day. You need to schedule `cron/daily_cleanup.py` via a cron job.

---

## 📌 To Do

- [ ] Frontend UI with React or plain HTML/JS
- [ ] User session tracking (optional)
- [ ] Admin panel (optional)
