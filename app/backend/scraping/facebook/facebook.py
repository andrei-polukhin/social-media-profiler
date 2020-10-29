# -*- coding: utf-8 -*-
from app.backend.scraping.facebook.facebook_filter import FacebookFilterLinks
from app.backend.scraping.scraper.scraping import scraping


def caller_facebook(query):
    results_to_filter = {}
    facebook_obj = FacebookFilterLinks(query)
    facebook_obj.facebook_open_home_page()
    facebook_obj.facebook_authenticate()
    facebook_obj.facebook_find_scraping_links()
    facebook_obj.facebook_filter_links()
    filtered_items = facebook_obj.regex_matching_items
    scraped_webpages = scraping(filtered_items)
    results_to_filter["facebook"] = scraped_webpages
    return results_to_filter


if __name__ == "__main__":
    print(caller_facebook("ongradient"))
