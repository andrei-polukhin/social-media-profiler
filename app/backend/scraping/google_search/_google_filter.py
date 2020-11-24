# -*- coding: utf-8 -*-
"""The Google link filtering module."""

import json
import re


def filtering(items: list) -> list:
    """
    Take the list of dictionaries of links and filter them to only needed information.

    Args:
        `items`: the list of dictionaries of links that has to be filtered.
    Returns:
        `list`: the list of filtered dictionaries of elements according to the params file.
    """
    only_title_link_snippet = _google_filter(items)
    file_contents = _read_json_file()
    generator = _regex_matching_items(file_contents, only_title_link_snippet)
    after_regex_checked_items = list(generator)
    return after_regex_checked_items


def _google_filter(items: list) -> list:
    """
    Take list of dictionaries of items and return \
    only ``title``, ``link``, ``snippet`` keys from them.

    Args:
        `items`: the list of dictionaries of links that has to be filtered.
    Returns:
         `list`: the list of dictionaries of links with \
         only ``title``, ``link``, ``snippet`` keys.
    """
    end_list = []
    for item in items:
        cleaned_dict = {
            k: v for k, v in item.items() if k in {"title", "link", "snippet"}
        }
        end_list.append(cleaned_dict)
    return end_list


def _read_json_file():
    """
    Read the params JSON file.

    Returns:
        `dict`: JSON-loaded contents represented as a Python dict.
    """
    try:
        with open("app/backend/scraping/google_search/google_params.json") as file:
            file_contents = json.load(file)
    except FileNotFoundError:
        # For tests
        with open("../app/backend/scraping/google_search/google_params.json") as file:
            file_contents = json.load(file)
    return file_contents


def _regex_matching_items(file_contents: dict, items: list) -> iter:
    """
    Take JSON-loaded contents and list of dictionaries of links \
    and filter to those meeting regex requirements.

    Args:
        `file_contents`: JSON-loaded contents represented as a Python dict.\n
        `items`: the list of dictionaries of links with \
        only ``title``, ``link``, ``snippet`` keys.
    Returns:
        `iter`: iterable that can be transformed to the list of regex matching links \
        with the XPATH of elements that should be found.
    """
    keys = file_contents.keys()
    for filtered_dict in items:
        link = filtered_dict["link"]
        for key in keys:
            if re.fullmatch(key, link):
                yield link, file_contents[key]


if __name__ == "__main__":
    from app.backend.scraping.google_search._google_mining import mining

    findings = mining("pythad")
    print("google_filter:\n", _google_filter(findings), "\n")
    print(filtering(findings))
