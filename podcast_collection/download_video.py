import yt_dlp


def download_youtube(
    url: str, secure_file_name: str, rate_limit=5000000, my_format="best[ext=mp4]"
) -> str:
    """
    Download a YouTube video, channel, or playlist based on the provided URL.

    Parameters:
        url (str): The URL of the YouTube video, channel, or playlist to be downloaded.
        video_title (str): The title of the YouTube video. Used when downloading a single video.
        rate_limit (int, optional): The download rate limit in bytes per second. Default is 5000000 (5 MB/s).
        my_format (str, optional): The format of the downloaded video. Default is 'best[ext=mp4]'.

    Returns:
        str: The file path where the video or channel/playlist is downloaded.
    """

    file_path = "C:/Users/azs547/Code/cmo-podcast-collection/raw_videos"
    ydl_opts = None

    if url.startswith("https://www.youtube.com/@"):
        ydl_opts = {
            "ignoreerrors": True,
            "abort_on_unavailable_fragments": True,
            "format": my_format,
            "outtmpl": file_path
            + "/Channels/%(uploader)s/%(title)s ## %(uploader)s ## %(id)s.%(ext)s",
            "ratelimit": rate_limit,
        }
    elif url.startswith(
        "https://www.youtube.com/watch",
    ):
        file_path += secure_file_name
        ydl_opts = {
            "ignoreerrors": True,
            "abort_on_unavailable_fragments": True,
            "format": my_format,
            "outtmpl": file_path + ".%(ext)s",
            "ratelimit": rate_limit,
        }

    if ydl_opts is not None:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)

    return file_path
