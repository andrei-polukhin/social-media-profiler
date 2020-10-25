from app.backend.facebook.facebook_search import FacebookSearchLinks
from app.backend.scraper.scraping import scraping


def facebook(query):
    results_to_display = {}
    o = FacebookSearchLinks(query)
    o.open_home_page()
    o.facebook_authenticate()
    o.find_scraping_links()
    filtered_items = o.regex_matching_items
    scraped_webpages = scraping(filtered_items)
    results_to_display["facebook"] = scraped_webpages
    return results_to_display


if __name__ == "__main__":
    print(facebook("ongradient"))
