# -*- coding: utf-8 -*-
def split_string_in_words_with_len_limit(string: str, limit=45):
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
