import yt_dlp
import re

ydl_opts = {
    "quiet": True,
    "default_search": "ytsearch",
    "format": "best",
    "get-url": True,
}

VERIFICATION_REGEX = r"\b(cmo|chief marketing officer)\b"


def find_video_and_extract_info(search_query: str) -> dict:
    """
    Finds a video on YouTube using the given search query and extracts relevant information.

    Args:
        search_query (str): The search query to find the video on YouTube.

    Returns:
        dict: A dictionary containing the extracted information of the first video entry.
    """

    youtube_info = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_result_info = ydl.extract_info(search_query, download=False)
        relevant_entry = search_result_info["entries"][0]

        youtube_info = {
            "video_title": relevant_entry["title"].lower(),
            "video_description": relevant_entry["description"].lower(),
            "video_url": relevant_entry["webpage_url"],
            "channel_title": relevant_entry["channel"].lower(),
            "channel_url": relevant_entry["uploader_url"],
        }

    return youtube_info


def verify_video_info(youtube_info: dict) -> str:
    """
    Verifies YouTube video information based on a predefined verification regex pattern.

    Args:
        youtube_info (dict): A dictionary containing YouTube video information.
            Required keys: "video_title", "video_description", "video_url", "channel_title", "channel_url"

    Returns:
        str: The verified URL (video URL or channel URL) if the information is related to Chief Marketing Officers.
            If not related, returns a message indicating that and suggests searching for another query.
    """

    verified_url = ""

    is_video_title_verified = bool(
        re.search(VERIFICATION_REGEX, youtube_info["video_title"])
    )
    is_video_description_verified = bool(
        re.search(VERIFICATION_REGEX, youtube_info["video_description"])
    )
    is_channel_title_verified = bool(
        re.search(VERIFICATION_REGEX, youtube_info["channel_title"])
    )

    if is_video_title_verified is True or is_video_description_verified is True:
        verified_url = youtube_info["video_url"]
    elif is_channel_title_verified is True:
        verified_url = youtube_info["channel_url"]
    else:
        verified_url = "This video is not related to Chief Marketing Officers"

    return verified_url
