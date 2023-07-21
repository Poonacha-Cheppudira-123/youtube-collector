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


def main() -> None:
    search_query = curate_search_string(
        cmo_phrase_variations, media_types, cmo_adjectives, cmo_responsibilities
    )
    youtube_info = find_video_and_extract_info(search_query)
    verified_url = verify_video_info(youtube_info)


if __name__ == "__main__":
    main()
