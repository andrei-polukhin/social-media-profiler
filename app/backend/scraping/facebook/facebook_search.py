# -*- coding: utf-8 -*-
import time

from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from app.backend.scraping.facebook.facebook_authenticate import (
    FacebookAuthenticate,
)
from app.backend.scraping.facebook.facebook_tech_params import (
    SEARCH_LINK,
    FOUND_LINKS_USUAL,
    FOUND_LINKS_OTHER
)


class FacebookSearchLinks(FacebookAuthenticate):
    def __init__(self, query):
        super().__init__()
        self.encoded_query = quote(query)
        self.search_link = SEARCH_LINK + self.encoded_query
        self.found_elements_links = None
        self.hrefs_of_elements = set()
        self.file_contents = {}
        self.params_keys = []
        self.regex_matching_items = []

    def facebook_find_scraping_links(self):
        self._facebook_open_search_link()
        self._facebook_check_presence_of_elements_links()
        self._facebook_get_hrefs_of_elements()
        self._facebook_close_browser()

    def _facebook_open_search_link(self):
        time.sleep(3)
        self.driver.get(self.search_link)
        self.driver.implicitly_wait(5)

    def _facebook_check_presence_of_elements_links(self):
        try:
            self.found_elements_links = self.wait.until(
                EC.presence_of_all_elements_located(FOUND_LINKS_USUAL)
            )
        except TimeoutException:
            self.found_elements_links = self.wait.until(
                EC.presence_of_all_elements_located(FOUND_LINKS_OTHER)
            )

    def _facebook_get_hrefs_of_elements(self):
        self.hrefs_of_elements: set
        for element in self.found_elements_links:
            href = element.get_property("href")
            if not href.endswith("/"):
                href = href + "/"
            self.hrefs_of_elements.add(href)
        self.hrefs_of_elements = list(self.hrefs_of_elements)

    def _facebook_close_browser(self):
        self.driver.quit()


if __name__ == "__main__":
    o = FacebookSearchLinks("ongradient")
    o.facebook_open_home_page()
    o.facebook_authenticate()
    o.facebook_find_scraping_links()
    print(o.regex_matching_items)
