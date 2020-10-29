# -*- coding: utf-8 -*-
import json
import re


def filtering(items):
    only_title_link_snippet = google_filter(items)
    file_contents = read_json_file()
    generator = regex_matching_items(file_contents, only_title_link_snippet)
    after_regex_checked_items = list(generator)
    return after_regex_checked_items


def google_filter(items):
    end_list = []
    for item in items:
        cleaned_dict = {
            k: v for k, v in item.items() if k in {"title", "link", "snippet"}
        }
        end_list.append(cleaned_dict)
    return end_list


def read_json_file():
    try:
        with open("google_params.json") as file:
            file_contents = json.load(file)
    except FileNotFoundError:
        with open("app/backend/google_search/google_params.json") as file:
            file_contents = json.load(file)
    return file_contents


def regex_matching_items(file_contents, items):
    keys = file_contents.keys()
    for filtered_dict in items:
        link = filtered_dict["link"]
        for key in keys:
            if re.fullmatch(key, link):
                yield link, file_contents[key]


if __name__ == "__main__":
    from app.backend.scraping.google_search.mining import mining

    findings = mining("pythad")
    print("google_filter:\n", google_filter(findings), "\n")
    print(filtering(findings))
