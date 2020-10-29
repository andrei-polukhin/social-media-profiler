# -*- coding: utf-8 -*-
from googleapiclient.discovery import build
import requests

from app.backend.config import IPSTACK_API_KEY, GOOGLE_DEVELOPER_KEY, GOOGLE_CSE_ID


def mining(query):
    country = get_country_code()
    found_items = custom_search(query, country)
    return found_items


def get_country_code():
    api = IPSTACK_API_KEY
    url = f"http://api.ipstack.com/check?access_key={api}"
    json = requests.get(url).json()
    return json["country_code"].lower()


def custom_search(query, country):
    service = build("customsearch", "v1", developerKey=GOOGLE_DEVELOPER_KEY)
    answer = (
        service.cse()
        .list(
            q=query,
            cx=GOOGLE_CSE_ID,
            gl=country,
        )
        .execute()
    )
    return answer["items"]


if __name__ == "__main__":
    from pprint import pprint

    pprint(mining("bill gates"))
    print(get_country_code())
    print(custom_search("pythad", "us"))
