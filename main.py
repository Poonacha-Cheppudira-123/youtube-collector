from podcast_collection.important_lists import (
    cmo_phrase_variations,
    media_types,
    cmo_adjectives,
    cmo_responsibilities,
)
from podcast_collection.curate_search_strings import curate_search_string


def main() -> None:
    # Curate search query
    search_query = curate_search_string(
        cmo_phrase_variations, media_types, cmo_adjectives, cmo_responsibilities
    )
    print(search_query)


if __name__ == "__main__":
    main()
