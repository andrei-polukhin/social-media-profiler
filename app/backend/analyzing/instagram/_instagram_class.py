class InstagramAnalyze:
    def __init__(self, scraping_response, user_input):
        self.user_info_as_dicts = scraping_response["instagram"]
        self.required_instagram_nickname = user_input.get("instagram_nickname")
        self.required_full_name = " ".join([
            user_input.get("first_name"),
            user_input.get("last_name")
        ])
        self.user_info_after_profile_filter = []

    def instagram_analyze(self):
        self._instagram_perform_analysis()

    def _instagram_perform_analysis(self):
        for user_info in self.user_info_as_dicts:
            received_instagram_nickname = user_info["username"]
            received_full_name = user_info["full_name"]
            if self.required_instagram_nickname == received_instagram_nickname \
                    or not self.required_instagram_nickname and self.required_full_name == received_full_name:
                self.user_info_after_profile_filter.append(user_info)
