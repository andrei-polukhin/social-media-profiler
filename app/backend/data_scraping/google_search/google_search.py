# -*- coding: utf-8 -*-
from app.backend.data_scraping.google_search.mining import mining
from app.backend.data_scraping.google_search.filtering import filtering
from app.backend.data_scraping.scraper.scraping import scraping


def caller_google_search(query):
    results_to_filter = {}
    elicited_items = mining(query)
    filtered_items = filtering(elicited_items)
    scraped_webpages = scraping(filtered_items)
    results_to_filter["google_search"] = scraped_webpages
    return results_to_filter


if __name__ == "__main__":
    print(caller_google_search("github andrew"))
