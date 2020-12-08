# -*- coding: utf-8 -*-
"""The Twitter analyzing module with the necessary class."""

import string
from app.backend.analyzing.substring_match.find_similarity_ratio import find_similarity_ratio


class TwitterAnalyze:
    """
    The class to run filters against screen name (if user input has screen name), \
    otherwise run filters against first and last names, user location and description.
    """
    def __init__(self, scraping_response, user_input):
        self.tuples_of_info_and_posts = scraping_response["twitter"]
        self.user_input = user_input
        self._tuples_after_name_filter = []
        self.tuples_after_location_filter = []
        self.tuples_after_all_filters = []

    def twitter_analyze(self):
        """
        Call other methods to run filters against screen name (if user input has screen name), \
        otherwise run filters against first and last names, user location and description.
        """
        if self.user_input["twitter_profile"]:
            self.__twitter_analyze_screen_name()
        else:
            self.__twitter_analyze_first_and_last_names()
            self.__twitter_analyze_location()
            self.__analyze_twitter_description()

    def __twitter_analyze_screen_name(self):
        """
        Run filtering against screen names (if user input has a screen name).
        """
        required_screen_name = self.user_input["twitter_profile"]
        for info_and_posts in self.tuples_of_info_and_posts:
            only_user_info = info_and_posts[0]
            twitter_screen_name = only_user_info["screen_name"]
            if required_screen_name == twitter_screen_name:
                self.tuples_after_all_filters.append(info_and_posts)
                break

    def __twitter_analyze_first_and_last_names(self):
        """
        Run filtering against first and last names (if no screen name was required).
        """
        required_first_name = self.user_input["first_name"]
        required_last_name = self.user_input["last_name"]
        required_full_name = " ".join([required_first_name, required_last_name])
        for info_and_posts in self.tuples_of_info_and_posts:
            only_user_info = info_and_posts[0]
            twitter_full_name = only_user_info["name"]
            if required_full_name == twitter_full_name:
                self._tuples_after_name_filter.append(info_and_posts)

    def __twitter_analyze_location(self):
        """
        Run filtering against location (if no screen name was required and name filter succeeded).
        """
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

    def __analyze_twitter_description(self):
        """
        Run filtering against description (if no screen name was required \
        and location filter succeeded).
        """
        required_additional_text = self.user_input["additional_text"]
        for info_and_posts in self.tuples_after_location_filter:
            only_user_info = info_and_posts[0]
            twitter_description = only_user_info["description"]
            similarity = find_similarity_ratio(
                required_additional_text, twitter_description
            )
            if similarity >= 0.6:
                self.tuples_after_all_filters.append(info_and_posts)

    @staticmethod
    def _twitter_sanitize_and_convert_to_set(input_str: str) -> set:
        """
        Sanitize the string from punctuation and put all words into a set.

        Args:
             `input_str`: the initial string to sanitize.
        Returns:
            `set`: the set from sanitized strings (no punctuation and lowercase).
        """
        string_sanitized = input_str.lower().translate(
            str.maketrans("", "", string.punctuation)
        )
        string_sanitized_as_set = set(string_sanitized.split())
        return string_sanitized_as_set
