# -*- coding: utf-8 -*-
import time
import json
import re

from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from app.backend.data_scraping.facebook.facebook_authenticate import (
    FacebookAuthenticate,
)
from app.backend.data_scraping.facebook.facebook_tech_params import (
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

    def find_scraping_links(self):
        self.open_search_link()
        self.check_presence_of_elements_links()
        self.get_hrefs_of_elements()
        self.close_browser()
        self.filter_links()

    def open_search_link(self):
        time.sleep(3)
        self.driver.get(self.search_link)
        self.driver.implicitly_wait(5)

    def check_presence_of_elements_links(self):
        try:
            self.found_elements_links = self.wait.until(
                EC.presence_of_all_elements_located(FOUND_LINKS_USUAL)
            )
        except TimeoutException:
            self.found_elements_links = self.wait.until(
                EC.presence_of_all_elements_located(FOUND_LINKS_OTHER)
            )

    def get_hrefs_of_elements(self):
        self.hrefs_of_elements: set
        for element in self.found_elements_links:
            href = element.get_property("href")
            if not href.endswith("/"):
                href = href + "/"
            self.hrefs_of_elements.add(href)
        self.hrefs_of_elements = list(self.hrefs_of_elements)

    def close_browser(self):
        self.driver.quit()

    def filter_links(self):
        self.read_facebook_params()
        generator = self.get_regex_matching_keys()
        self.regex_matching_items = list(generator)

    def read_facebook_params(self):
        try:
            with open("facebook_params.json") as file:
                self.file_contents = json.load(file)
        except FileNotFoundError:
            with open("app/backend/facebook/facebook_params.json") as file:
                self.file_contents = json.load(file)
        self.params_keys = self.file_contents.keys()

    def get_regex_matching_keys(self):
        for element in self.hrefs_of_elements:
            for key in self.params_keys:
                if re.fullmatch(key, element):
                    yield element, self.file_contents[key]


if __name__ == "__main__":
    o = FacebookSearchLinks("ongradient")
    o.open_home_page()
    o.facebook_authenticate()
    o.find_scraping_links()
    print(o.regex_matching_items)
