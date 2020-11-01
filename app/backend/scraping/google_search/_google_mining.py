# -*- coding: utf-8 -*-
import os
from googleapiclient.discovery import build
import requests


def mining(query):
    country = _get_country_code()
    found_items = _custom_search(query, country)
    return found_items


def _get_country_code():
    api = os.getenv("IPSTACK_API_KEY")
    url = f"http://api.ipstack.com/check?access_key={api}"
    json = requests.get(url).json()
    return json["country_code"].lower()


def _custom_search(query, country):
    service = build("customsearch", "v1", developerKey=os.getenv("GOOGLE_DEVELOPER_KEY"))
    answer = (
        service.cse()
        .list(
            q=query,
            cx=os.getenv("GOOGLE_CSE_ID"),
            gl=country,
        )
        .execute()
    )
    return answer["items"]


if __name__ == "__main__":
    from pprint import pprint

    pprint(mining("bill gates"))
    print(_get_country_code())
    print(_custom_search("pythad", "us"))
