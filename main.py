import yt_dlp
import os
from colorama import Fore
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

def download_video(url, output_path):
    ydl_opts = {
        # Only select formats that are already muxed (no merging, no ffmpeg needed)
        'format': 'best[ext=mp4][acodec!=none][vcodec!=none]/best[acodec!=none][vcodec!=none]',
        'outtmpl': output_path,
        'noplaylist': True,
        'quiet': True,
        'postprocessors': [],  # No postprocessing, so no ffmpeg
        'merge_output_format': None,  # Don't merge
        'allow_unplayable_formats': False,
        'ignoreerrors': False,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        msg = str(e)
        if 'This video is not available in your country' in msg:
            print(Fore.RED + "Error: This video is not available in your country.")
        elif 'requested format not available' in msg or 'merging of multiple formats' in msg:
            print(Fore.RED + "Could not find a single file with both video and audio (progressive MP4). Try another video or install ffmpeg for advanced downloads.")
        else:
            print(Fore.RED + f"Download error: {e}")
        print(Fore.RESET)

# Main function to execute the download process
def main():
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
    folder = input(Fore.LIGHTMAGENTA_EX + "Enter output folder (default: downloads): ").strip() or "downloads"
    os.makedirs(folder, exist_ok=True)
    output_path = os.path.join(folder, f"{filename}.mp4")
    download_video(url, output_path)
    print(Fore.GREEN +f"Downloaded to: {output_path}")
    print(Fore.RESET + "Done!")

main()