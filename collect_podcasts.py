from datetime import datetime
import uuid
from podcast_collection.important_lists import (
    cmo_phrase_variations,
    media_types,
    cmo_adjectives,
    cmo_responsibilities,
)
from podcast_collection.curate_search_strings import curate_search_string
from podcast_collection.retrieve_valid_url import (
    find_video_and_extract_info,
    verify_video_info,
)
from podcast_collection.download_video import download_youtube


def main() -> None:
    """Downloads a specified number of YouTube videos related to Chief Marketing Officers (CMOs)."""
    verified_url_list = []
    num_of_desired_videos = int(input("Specify the number of urls you want: "))
    count = 0

    while count < num_of_desired_videos:
        search_query = curate_search_string(
            cmo_phrase_variations, media_types, cmo_adjectives, cmo_responsibilities
        )

        youtube_info = find_video_and_extract_info(search_query)
        verified_url = verify_video_info(youtube_info)
        if verified_url != "This video is not related to Chief Marketing Officers":
            verified_url_list.append(verified_url)
            count += 1

    download_url_list = list(set(verified_url_list))

    secure_file_name = ""
    video_title = youtube_info["video_title"]
    formatted_title = video_title.replace(" ", "_")
    secure_file_name = f"{uuid.uuid4().hex}-{formatted_title}"

    file_path = ""
    collection_endpoint = ""
    current_time = ""
    for download_url in download_url_list:
        file_path = download_youtube(
            download_url,
            secure_file_name,
            rate_limit=5000000,
            my_format="best[ext=mp4]",
        )
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        collection_endpoint = "YouTube"


if __name__ == "__main__":
    main()
