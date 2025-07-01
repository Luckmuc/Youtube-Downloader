@echo off
echo 🎬 YouTube Downloader Setup
echo ========================

echo.
echo Creating virtual environment...
python -m venv .venv

echo.
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo ✅ Setup complete!
echo.
echo To run the downloader:
echo 1. Activate the virtual environment: .venv\Scripts\activate
echo 2. Run the script: python main.py
echo.
echo For best quality, install FFmpeg from: https://ffmpeg.org/download.html
echo.
pause
