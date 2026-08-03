import yt_dlp

def download(url, output_dir="downloads"):
    ydl_opts = {
        'format': 'bv*+ba/b',
        'outtmpl': f'{output_dir}/%(uploader)s_%(title).100s_%(id)s.%(ext)s',
        'noplaylist': True,
        'socket_timeout': 30,
        'retries': 10,
        'fragment_retries': 10,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        },
        # Convert to mp4 as a postprocessing step, not a hard requirement
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"\n✨ Download completed: {filename}")
    except yt_dlp.utils.DownloadError as e:
        msg = str(e)
        if "Failed to connect" in msg or "Could not connect" in msg:
            print(f"\n❌ Network error — couldn't reach the site's servers.")
            print("This isn't a code bug. Check your connection/VPN and try again.")
        else:
            print(f"\n❌ Download error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == '__main__':
    url = input("Enter the URL: ").strip()
    download(url)