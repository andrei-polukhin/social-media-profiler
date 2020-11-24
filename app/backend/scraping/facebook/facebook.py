# -*- coding: utf-8 -*-
"""The main Facebook scraping module."""

from app.backend.scraping.facebook._facebook_filter import FacebookFilterLinks
from app.backend.scraping.scraper.scraping import scraping


def caller_facebook(full_name: str) -> dict:
    """
    Call all Facebook scraping methods to get potential links about a person \
    and scrape on selectors.

    Args:
        `full_name`: the full name of the person links about whom we want to find.
    Returns:
        `dict`: the dictionary with links and with elements on them with values.
    """
    results_to_filter = {}
    facebook_obj = FacebookFilterLinks(full_name)
    facebook_obj.facebook_open_home_page()
    facebook_obj.facebook_authenticate()
    facebook_obj.facebook_find_scraping_links()
    facebook_obj.facebook_filter_links()
    filtered_items = facebook_obj.regex_matching_items
    scraped_webpages = scraping(filtered_items)
    results_to_filter["facebook"] = scraped_webpages
    return results_to_filter
