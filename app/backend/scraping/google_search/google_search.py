# -*- coding: utf-8 -*-
from app.backend.scraping.google_search.google_mining import mining
from app.backend.scraping.google_search.google_filter import filtering
from app.backend.scraping.scraper.scraping import scraping


def caller_google_search(**kwargs):
    results_to_filter = {}
    results_to_filter["google_search"] = scraped_webpages = {}
    for selector, query in kwargs.items():
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
    print(caller_google_search(name="Vladyslav Ovchynnykov", github="pythad"))
