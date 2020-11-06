# -*- coding: utf-8 -*-
from fingerprint import Fingerprint

FINGERPRINT = Fingerprint(kgram_len=3, window_len=4, base=11, modulo=100)


def find_similarity_ratio(f_string, s_string):
    f_string_fingerprint = FINGERPRINT.generate(str=f_string)
    s_string_fingerprint = FINGERPRINT.generate(str=s_string)
    f_string_only_hashes = [
        element[0]
        for element in f_string_fingerprint
    ]
    s_string_only_hashes = [
        element[0]
        for element in s_string_fingerprint
    ]
    common_hashes = set(f_string_only_hashes).intersection(set(s_string_only_hashes))
    length_common_hashes = len(common_hashes)
    minimal_length_of_string = len(min(f_string_only_hashes, s_string_only_hashes, key=len))
    return length_common_hashes / minimal_length_of_string
