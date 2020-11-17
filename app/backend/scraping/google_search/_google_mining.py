# -*- coding: utf-8 -*-
"""The Google link mining module."""

import os
from googleapiclient.discovery import build
import requests


def mining(query: str) -> list:
    """
    Call other functions to mine information about a particular person.

    Args:
        `query`: the query to which links will be found.
    Returns:
        `list`: the list of dictionaries of found info to the input query.
    """
    country = _get_country_code()
    found_items = _custom_search(query, country)
    return found_items


def _get_country_code():
    """
    Get the country of the user of the app.

    Returns:
        `str`: the country code of the user.
    """
    api = os.getenv("IPSTACK_API_KEY")
    url = f"http://api.ipstack.com/check?access_key={api}"
    json = requests.get(url).json()
    return json["country_code"].lower()


def _custom_search(query: str, country_code: str) -> list:
    """
    Call Google Custom Search API to find info to the input query.

    Args:
         `query`: the query to which links will be found.\n
         `country_code`: the country code of the user.
    Returns:
         `list`: the list of dictionaries of found info to the input query.
    """
    service = build("customsearch", "v1", developerKey=os.getenv("GOOGLE_DEVELOPER_KEY"))
    answer = (
        service.cse()
        .list(
            q=query,
            cx=os.getenv("GOOGLE_CSE_ID"),
            gl=country_code,
        )
        .execute()
    )
    return answer["items"]


if __name__ == "__main__":
    from pprint import pprint

    pprint(mining("bill gates"))
    print(_get_country_code())
    print(_custom_search("pythad", "us"))
