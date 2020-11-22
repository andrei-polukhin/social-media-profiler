# -*- coding: utf-8 -*-
"""The main module finding similarity ratio between two strings."""

from fingerprint import Fingerprint
from fingerprint.fingerprint import FingerprintException

FINGERPRINT = Fingerprint(kgram_len=4, window_len=3, base=101, modulo=256)


def find_similarity_ratio(f_string: str, s_string: str) -> float:
    """
    Take two strings and find similarity between them using \
    Rabin fingerprint and winnowing by Stanford.

    Args:
         `f_string`: first string.\n
         `s_string`: second string.
    Returns:
        `float`: the similarity ratio between two strings.
    """
    try:
        f_string_fingerprint = FINGERPRINT.generate(str=f_string)
        s_string_fingerprint = FINGERPRINT.generate(str=s_string)
    except (FingerprintException, IndexError):
        return 0
    f_string_only_hashes = [
        element[0]
        for element in f_string_fingerprint
    ]
    s_string_only_hashes = [
        element[0]
        for element in s_string_fingerprint
    ]
    common_hashes = set(f_string_only_hashes).intersection(set(s_string_only_hashes))
    minimal_length_of_string_hashes = len(
        min(f_string_only_hashes, s_string_only_hashes, key=len)
    )
    return len(common_hashes) / minimal_length_of_string_hashes


if __name__ == "__main__":
    print(find_similarity_ratio(
        "Institute of Mathematics trains highly skilled mathematicians.",
        "Institute of Mathematics is the only institution"
        "that trains highly skilled mathematicians."
    ))
