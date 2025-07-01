import yt_dlp
import os
import ffmpeg
import shutil
from colorama import Fore
# Helper to check if ffmpeg is available
def check_ffmpeg():
    """Check if ffmpeg is available in the system"""
    return shutil.which('ffmpeg') is not None

# Helper to get video info (title)
def get_video_title(url):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get('title', 'video')
    except yt_dlp.utils.DownloadError as e:
        if 'This video is not available in your country' in str(e):
            print(Fore.RED + "Error: This video is not available in your country.")
        else:
            print(Fore.RED + f"Error: {e}")
        print(Fore.RESET)
        return None

def download_video(url, output_path, quality_choice='best'):
    ffmpeg_available = check_ffmpeg()
    
    if ffmpeg_available:
        # High-quality download with ffmpeg support
        ydl_opts = {
            'format': quality_choice,
            'outtmpl': output_path,
            'noplaylist': True,
            'quiet': True,
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }
        print(Fore.GREEN + "✓ FFmpeg detected - High quality downloads available!")
    else:
        # Fallback to progressive downloads without ffmpeg
        ydl_opts = {
            'format': 'best[ext=mp4][acodec!=none][vcodec!=none]/best[acodec!=none][vcodec!=none]',
            'outtmpl': output_path,
            'noplaylist': True,
            'quiet': True,
            'postprocessors': [],
            'merge_output_format': None,
            'allow_unplayable_formats': False,
            'ignoreerrors': False,
        }
        print(Fore.YELLOW + "⚠ FFmpeg not found - Using progressive download mode")
    
    print(Fore.RESET)
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        msg = str(e)
        if 'This video is not available in your country' in msg:
            print(Fore.RED + "Error: This video is not available in your country.")
        elif not ffmpeg_available and ('requested format not available' in msg or 'merging of multiple formats' in msg):
            print(Fore.RED + "Could not find a single file with both video and audio (progressive MP4).")
            print(Fore.YELLOW + "💡 Tip: Install ffmpeg for better format support and higher quality downloads!")
        else:
            print(Fore.RED + f"Download error: {e}")
        print(Fore.RESET)

# Main function to execute the download process
def main():
    print(Fore.CYAN + "🎬 YouTube Video Downloader")
    print(Fore.CYAN + "=" * 30)
    print(Fore.RESET)
    
    # Check ffmpeg availability
    if check_ffmpeg():
        print(Fore.GREEN + "✓ FFmpeg is available - Full quality downloads enabled!")
    else:
        print(Fore.YELLOW + "⚠ FFmpeg not found - Progressive downloads only")
        print(Fore.CYAN + "💡 For best quality, install ffmpeg: https://ffmpeg.org/download.html")
    print()
    
    url = input(Fore.BLUE + "Enter YouTube video URL: ")
    title = get_video_title(url)
    if not title:
        return
    
    print(f"Video title: {title}")
    
    use_default = input(Fore.YELLOW + "Use this title as filename? (Y/n): ").strip().lower()
    if use_default == 'n':  
        custom_title = input("Enter your desired filename (without extension): ").strip()
        filename = custom_title if custom_title else title
    else:
        filename = title
    
    # Quality selection if ffmpeg is available
    quality_choice = 'best'
    if check_ffmpeg():
        print(Fore.CYAN + "\nQuality options:")
        print("1. Best quality (default)")
        print("2. High quality (720p)")
        print("3. Medium quality (480p)")
        quality_input = input(Fore.YELLOW + "Choose quality (1-3, default: 1): ").strip()
        
        if quality_input == '2':
            quality_choice = 'best[height<=720]'
        elif quality_input == '3':
            quality_choice = 'best[height<=480]'
        else:
            quality_choice = 'best'
    
    folder = input(Fore.LIGHTMAGENTA_EX + "Enter output folder (default: downloads): ").strip() or "downloads"
    os.makedirs(folder, exist_ok=True)
    output_path = os.path.join(folder, f"{filename}.%(ext)s")
    
    print(Fore.CYAN + "\n🚀 Starting download...")
    download_video(url, output_path, quality_choice)
    print(Fore.GREEN + f"✓ Downloaded to: {folder}/{filename}.mp4")
    print(Fore.RESET + "Done!")

if __name__ == "__main__":
    main()