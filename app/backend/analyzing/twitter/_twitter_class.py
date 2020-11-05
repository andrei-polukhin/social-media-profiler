# -*- coding: utf-8 -*-
import string
from app.backend.analyzing.substring_match.find_similarity_ratio import find_similarity_ratio


class TwitterAnalyze:
    def __init__(self, scraping_response, user_input):
        self.tuples_of_info_and_posts = scraping_response["twitter"]
        self.user_input = user_input
        self._tuples_after_name_filter = []
        self.tuples_after_location_filter = []
        self.tuples_after_description_filter = []

    def twitter_analyze(self):
        self._twitter_analyze_first_and_last_names()
        self._twitter_analyze_location()
        self._analyze_twitter_description()

    def _twitter_analyze_first_and_last_names(self):
        required_first_name = self.user_input["first_name"]
        required_last_name = self.user_input["last_name"]
        required_full_name = " ".join([required_first_name, required_last_name])
        for info_and_posts in self.tuples_of_info_and_posts:
            only_user_info = info_and_posts[0]
            twitter_full_name = only_user_info["name"]
            if required_full_name == twitter_full_name:
                self._tuples_after_name_filter.append(info_and_posts)

    def _twitter_analyze_location(self):
        required_location = self.user_input["location"]
        required_location_sanitized_set = self._twitter_sanitize_and_convert_to_set(
            required_location
        )
        for info_and_posts in self._tuples_after_name_filter:
            only_user_info = info_and_posts[0]
            twitter_location = only_user_info["location"]
            twitter_location_sanitized_set = self._twitter_sanitize_and_convert_to_set(
                twitter_location
            )
            if required_location_sanitized_set.intersection(twitter_location_sanitized_set):
                self.tuples_after_location_filter.append(info_and_posts)

    def _analyze_twitter_description(self):
        required_additional_text = self.user_input["additional_text"]
        for info_and_posts in self.tuples_after_location_filter:
            only_user_info = info_and_posts[0]
            twitter_description = only_user_info["description"]
            similarity = find_similarity_ratio(
                required_additional_text, twitter_description
            )
            if similarity >= 0.4:
                self.tuples_after_description_filter.append(info_and_posts)

    @staticmethod
    def _twitter_sanitize_and_convert_to_set(input_str: str):
        string_sanitized = input_str.lower().translate(
            str.maketrans("", "", string.punctuation)
        )
        string_sanitized_as_set = set(string_sanitized.split())
        return string_sanitized_as_set
