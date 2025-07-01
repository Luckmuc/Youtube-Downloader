#!/bin/bash
echo "🎬 YouTube Downloader Setup"
echo "========================"

echo ""
echo "Creating virtual environment..."
python3 -m venv .venv

echo ""
echo "Activating virtual environment..."
source .venv/bin/activate

echo ""
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run the downloader:"
echo "1. Activate the virtual environment: source .venv/bin/activate"
echo "2. Run the script: python main.py"
echo ""
echo "For best quality, install FFmpeg:"
echo "Ubuntu/Debian: sudo apt install ffmpeg"
echo "macOS: brew install ffmpeg"
echo "Fedora: sudo dnf install ffmpeg"
echo ""
