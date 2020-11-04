class FacebookAnalyze:
    def __init__(self, facebook_response, user_input):
        self.user_info_as_dicts = facebook_response["facebook"]
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
            user_link = user_info["link"]
            if "/groups/" in user_link and user_info.get("group_name") == required_full_name\
                    or user_info.get("name_if_profile") == required_full_name:
                self.user_info_after_profile_name_filter.append(user_info)
