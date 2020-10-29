import json
import re
from app.backend.scraping.facebook.facebook_search import FacebookSearchLinks


class FacebookFilterLinks(FacebookSearchLinks):
    def __init__(self, query):
        super().__init__(query)

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
        for element in self.hrefs_of_elements:
            for key in self.params_keys:
                if re.fullmatch(key, element):
                    yield element, self.file_contents[key]
