# -*- coding: utf-8 -*-
import json
import re
from app.backend.scraping.facebook._facebook_search import FacebookSearchLinks


class FacebookFilterLinks(FacebookSearchLinks):
    def __init__(self, full_name):
        super(FacebookFilterLinks, self).__init__(full_name)
        self.file_contents = {}
        self.params_keys = []

    def facebook_filter_links(self):
        self.facebook_read_facebook_params()
        generator = self.facebook_get_regex_matching_keys()
        self.regex_matching_items = list(generator)

    def facebook_read_facebook_params(self):
        try:
            with open("facebook_params.json") as file:
                self.file_contents = json.load(file)
        except FileNotFoundError:
            with open("./facebook/facebook_params.json") as file:
                self.file_contents = json.load(file)
        self.params_keys = self.file_contents.keys()

    def facebook_get_regex_matching_keys(self):
        for element in self._hrefs_of_elements:
            for key in self.params_keys:
                if re.fullmatch(key, element):
                    yield element, self.file_contents[key]
