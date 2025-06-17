# 🎬 YouTube Video Downloader

A simple, user-friendly Python script to download YouTube videos as MP4 files — no ffmpeg required for most videos!

## ✨ Features
- 🔗 Download any public YouTube video by URL
- 📝 Choose your own filename or use the original video title
- 📁 Select or create your preferred output folder
- 🚫 No ffmpeg required for most downloads (downloads progressive MP4s)
- 🌍 Friendly error messages for region-locked or unavailable videos
- 🎨 Colorful, interactive command-line prompts

## 🚀 Getting Started

### 1. Clone or Download
Download or clone this repository to your computer.

### 2. Install Requirements
Create a virtual environment (optional but recommended):
```powershell
python -m venv .venv
.venv\Scripts\activate
```
Install dependencies:
```powershell
pip install yt-dlp colorama
```

### 3. Run the Script
```powershell
python main.py
```

## 🛠️ Usage
1. Enter the YouTube video URL when prompted.
2. Choose to use the original title or enter a custom filename.
3. Select an output folder (default: `downloads`).
4. The video will be downloaded as an MP4 file.

## ⚠️ Notes
- If a video is not available in your country, you’ll get a friendly error message.
- If a video cannot be downloaded as a single MP4 file, you’ll be notified. For advanced downloads, install ffmpeg.

## 📦 Dependencies
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [colorama](https://pypi.org/project/colorama/)

## 💡 License
MIT License

---

Enjoy downloading! 🚀
