# -*- coding: utf-8 -*-
"""The module to limit a string to a specific length and put ellipsis after reaching the quota."""


def split_string_in_words_with_len_limit(string: str, limit=45) -> str:
    """
    Get string and limit it to the length specified as `limit`, \
    put ellipsis after reaching the quota.

    Args:
        string: the string that should be limited to a specific length.
        limit: the int value showing to which number of symbols the string should be limited.
    Returns:
        str: the limited string with an ellipsis at the end (if initial length has exceeded the quota.)
    """
    accumulated_words = []
    list_of_words_in_string = string.split()
    for word in list_of_words_in_string:
        string_from_current_list = " ".join(accumulated_words)
        if len(string_from_current_list) + len(word) + 1 <= limit:
            accumulated_words.append(word)
            continue
        accumulated_words[-1] += "..."
        break
    return " ".join(accumulated_words)
