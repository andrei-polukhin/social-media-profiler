# -*- coding: utf-8 -*-
"""The module to de-emojify the given string"""

import re


def de_emojify(string: str) -> str:
    """
        Get the string and replace all emojis in there with empty spaces.

        Args:
            `string`: the string from which emojis should be deleted.
        Returns:
            `str`: the string without emojis.
    """
    regex_pattern = re.compile(pattern="["
                                       u"\U0001F600-\U0001F64F"  # emoticons
                                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                       "]+", flags=re.UNICODE)
    return regex_pattern.sub(r"", string)
