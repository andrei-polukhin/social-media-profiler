# -*- coding: utf-8 -*-
"""The module with the Facebook analyzing class."""


class FacebookAnalyze:
    """The class to analyze full name in Facebook profiles."""
    def __init__(self, scraping_response, user_input):
        self.user_info_as_dicts = scraping_response["facebook"]
        self.user_input = user_input
        self.user_info_after_profile_name_filter = []

    def facebook_analyze(self):
        """Call other method to analyze full name in profiles."""
        self.__facebook_analyze_name_in_profiles()

    def __facebook_analyze_name_in_profiles(self):
        """
        Leave only profiles whose full name is the same as defined in user input.
        """
        required_first_name = self.user_input["first_name"]
        required_last_name = self.user_input["last_name"]
        required_full_name = " ".join([required_first_name, required_last_name])
        for user_info in self.user_info_as_dicts:
            user_info: dict
            possible_profile_names = [
                user_info.get("Profile name: "),
                user_info.get("Channel name: "),
                user_info.get("Group name: ")
            ]
            if required_full_name in possible_profile_names:
                self.user_info_after_profile_name_filter.append(user_info)
