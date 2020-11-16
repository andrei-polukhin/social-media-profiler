# -*- coding: utf-8 -*-
"""The module with the Instagram analyzing class."""

from app.backend.analyzing.substring_match.find_similarity_ratio import find_similarity_ratio


class InstagramAnalyze:
    """The class to analyze scraped Instagram profiles by their nickname and biography."""
    def __init__(self, scraping_response, user_input):
        self.user_info_as_dicts = scraping_response["instagram"]
        self.required_instagram_nickname = user_input.get("instagram_nickname")
        self.required_full_name = " ".join([
            user_input.get("first_name"),
            user_input.get("last_name")
        ])
        self.required_description = user_input.get("additional_text")
        self.user_info_after_name_filter = []
        self.user_info_after_desc_filter = []

    def instagram_analyze(self):
        """Call other methods to filter profiles by their nickname and biography."""
        self._instagram_filter_by_nick_or_name()
        self._instagram_filter_by_biography()

    def _instagram_filter_by_nick_or_name(self):
        """Filter scraped Instagram profiles by their nickname."""
        for user_info in self.user_info_as_dicts:
            received_instagram_nickname = user_info["username"]
            received_full_name = user_info["full_name"]
            if self.required_instagram_nickname == received_instagram_nickname \
                    or not self.required_instagram_nickname \
                    and self.required_full_name == received_full_name:
                self.user_info_after_name_filter.append(user_info)

    def _instagram_filter_by_biography(self):
        """Filter Instagram subjects after the nickname filter by their biography."""
        for user_info in self.user_info_after_name_filter:
            received_description = user_info["biography"]
            similarity = find_similarity_ratio(
                self.required_description, received_description
            )
            if similarity >= 0.4:
                self.user_info_after_desc_filter.append(user_info)
