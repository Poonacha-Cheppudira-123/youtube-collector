import random


def curate_search_string(
    cmo_phrase_variations: list,
    media_types: list,
    cmo_adjectives: list,
    cmo_responsibilities: list,
) -> str:
    """Randomize important lists, retrieve random str from each list, and append to search string

    Args:
        cmo_phrase_variations (list): A list of different words for CMO
        media_types (list): A list of video/audio types
        cmo_adjectives (list): A list of adjectives describing
        cmo_responsibilities (list): A list of tasks CMOs engage in

    Returns:
        str: A formatted search query created by concatenated, random elements from the lists
    """

    random.shuffle(cmo_phrase_variations)
    random.shuffle(media_types)
    random.shuffle(cmo_adjectives)
    random.shuffle(cmo_responsibilities)

    cmo_phrase_variation = random.choice(cmo_phrase_variations)
    media_type = random.choice(media_types)
    cmo_adjective = random.choice(cmo_adjectives)
    cmo_responsibility = random.choice(cmo_responsibilities)

    search_query = (
        f"{cmo_adjective} {cmo_phrase_variation} on {cmo_responsibility} {media_type}"
    )

    return search_query
