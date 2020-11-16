# -*- coding: utf-8 -*-
"""The main Google Search scraping module."""

from app.backend.scraping.google_search._google_mining import mining
from app.backend.scraping.google_search._google_filter import filtering
from app.backend.scraping.scraper.scraping import scraping


def caller_google_search(user_input):
    """
    Call all Google scraping function to get information about a person \
    and scrape it on selectors.

    Args:
        user_input: user input represented as a dictionary.
    Returns:
        dict: the dictionary with links and with elements on them with values.
    """
    results_to_filter = {}
    results_to_filter["google_search"] = scraped_webpages = {}
    full_name = " ".join([user_input["first_name"], user_input["last_name"]])
    input_to_scrape = {
        k: v
        for k, v in user_input.items()
        if k not in [
            "first_name",
            "last_name",
            "company",
            "job_title",
            "school",
            "twitter_profile",
            "instagram_nickname",
            "location",
            "additional_text"
        ]
    }
    input_to_scrape["name"] = full_name
    for selector, query in input_to_scrape.items():
        if selector == "name":
            searching_query = query
        else:
            searching_query = " ".join([selector, query])
        elicited_items = mining(searching_query)
        filtered_items = filtering(elicited_items)
        scraped_webpages_for_this_selector = scraping(filtered_items)
        scraped_webpages[selector] = scraped_webpages_for_this_selector
    return results_to_filter


if __name__ == "__main__":
    sample_input = {
        "first_name": "Evan",
        "last_name": "McCauley",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "MIT University",
        "twitter_profile": "abumetsov",
        "instagram_nickname": "Wayfarersbook",
        "location": "Ukraine",
        "additional_text": "CELTA/Delta teacher",
        "github": "pythad"
    }
    print(caller_google_search(sample_input))
