# -*- coding: utf-8 -*-
"""The module to de-emojify the given string"""


def de_emojify(string: str) -> str:
    """
    Get the string and replace all emojis in there with empty spaces.

    Args:
        `string`: the string from which emojis should be deleted.
    Returns:
        `str`: the string without emojis.
    """
    return string.encode('ascii', 'ignore').decode('ascii')
