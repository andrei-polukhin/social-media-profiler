# -*- coding: utf-8 -*-
from app.backend.google_search.mining import mining
from app.backend.google_search.filtering import filtering
from app.backend.google_search.scraping import scraping


def google_search(query):
    results_to_display = {}
    elicited_items = mining(query)
    filtered_items = filtering(elicited_items)
    scraped_webpages = scraping(filtered_items)
    results_to_display["google_search"] = scraped_webpages
    return results_to_display


if __name__ == "__main__":
    print(google_search("github andrew"))
