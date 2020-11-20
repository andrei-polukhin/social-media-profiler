# -*- coding: utf-8 -*-
"""The module filtering scraped Facebook links to satisfy conditions \
in the params file."""

import json
import re
from app.backend.scraping.facebook._facebook_search import FacebookSearchLinks


class FacebookFilterLinks(FacebookSearchLinks):
    """
    The class filtering received Facebook links to satisfy regex syntax \
    in the params file.
    """
    def __init__(self, full_name):
        super(FacebookFilterLinks, self).__init__(full_name)
        self.file_contents = {}
        self.params_keys = []

    def facebook_filter_links(self):
        """
        Call other methods to filter received links to those satisfying regex syntax.
        """
        self.facebook_read_facebook_params()
        generator = self.facebook_get_regex_matching_keys()
        self.regex_matching_items = list(generator)

    def facebook_read_facebook_params(self):
        """
        Read the params file to get regex expressions sought links have to match.
        """
        try:
            with open("app/backend/scraping/facebook/facebook_params.json") as file:
                self.file_contents = json.load(file)
        except FileNotFoundError:
            with open("scraping/facebook/facebook_params.json") as file:
                self.file_contents = json.load(file)
        self.params_keys = self.file_contents.keys()

    def facebook_get_regex_matching_keys(self) -> iter:
        """
        Generate iterable that can transformed to tuples of regex matching links \
        with the XPATH of elements that should be found.
        """
        for element in self._hrefs_of_elements:
            for key in self.params_keys:
                if re.fullmatch(key, element):
                    yield element, self.file_contents[key]
