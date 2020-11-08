# -*- coding: utf-8 -*-
class FacebookAnalyze:
    def __init__(self, scraping_response, user_input):
        self.user_info_as_dicts = scraping_response["facebook"]
        self.user_input = user_input
        self.user_info_after_profile_name_filter = []

    def facebook_analyze(self):
        self._facebook_analyze_name_in_profiles()

    def _facebook_analyze_name_in_profiles(self):
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
