# -*- coding: utf-8 -*-
"""The Instagram scraping module with the eponymous class."""

import json
import os

from instagram_private_api import (
    Client,
    ClientCookieExpiredError,
    ClientLoginRequiredError,
)

from app.backend.scraping.instagram._instagram_cookies import (
    load_from_json,
    on_login_callback,
)


class Instagram:
    """The class on scrape Instagram information from its official API."""
    SETTINGS_FILE = "cookie_settings.json"

    def __init__(self, query):
        self.query = query
        self.__api = None
        self.__device_id = None
        self._found_subjects = {}
        self._query_matching_users = []
        self._subject_ids = []
        self._extracted_info_about_subjects = []
        self.filtered_info_about_subjects = []

    def instagram(self):
        """Call other methods to scrape Instagram information from its API."""
        self._instagram_authenticate()
        self._instagram_search_for_subjects()
        self._instagram_get_ids_of_found_subjects()
        self._instagram_extract_info_with_subject_ids()
        self._instagram_filter_info_about_subjects()

    def _instagram_authenticate(self):
        """Authenticate and create/re-use cookie file to avoid throttling."""
        try:
            if not os.path.isfile(Instagram.SETTINGS_FILE):
                # Cookie settings file does not exist
                # Creating new file
                self.__api = Client(
                    os.getenv("INSTAGRAM_LOGIN"),
                    os.getenv("INSTAGRAM_PASSWORD"),
                    on_login=lambda x: on_login_callback(
                        x, Instagram.SETTINGS_FILE
                    ),
                )
            else:
                # Reusing auth settings from cookies
                with open(Instagram.SETTINGS_FILE) as file_data:
                    cached_settings = json.load(
                        file_data, object_hook=load_from_json
                    )
                self.__device_id = cached_settings.get("device_id")
                # Authenticating with saved settings.
                self.__api = Client(
                    os.getenv("INSTAGRAM_LOGIN"), os.getenv("INSTAGRAM_PASSWORD"),
                    settings=cached_settings
                )
        except (ClientCookieExpiredError, ClientLoginRequiredError):
            # Cookies have expired
            # Re-login but using default settings
            self.__api = Client(
                os.getenv("INSTAGRAM_LOGIN"),
                os.getenv("INSTAGRAM_PASSWORD"),
                device_id=self.__device_id,
                on_login=lambda x: on_login_callback(
                    x, Instagram.SETTINGS_FILE
                ),
            )

    def _instagram_search_for_subjects(self):
        """Search for potential users using API."""
        self._found_subjects = self.__api.search_users(self.query)

    def _instagram_get_ids_of_found_subjects(self):
        """Get IDs of found Instagram users."""
        users_info_as_list = self._found_subjects["users"]
        for user_as_dict in users_info_as_list:
            user_id = user_as_dict["pk"]
            self._subject_ids.append(user_id)

    def _instagram_extract_info_with_subject_ids(self):
        """Extract more info about found Instagram users using their IDs."""
        for subject_id in self._subject_ids:
            subject_extracted_info_as_dict = self.__api.user_info(subject_id)
            subject_extracted_info = subject_extracted_info_as_dict["user"]
            self._extracted_info_about_subjects.append(subject_extracted_info)

    def _instagram_filter_info_about_subjects(self):
        """Filter found information about subjects saving only information \
        with specific keys (see code)."""
        for info_about_subject in self._extracted_info_about_subjects:
            sorted_dictionary = {
                k: v
                for k, v in info_about_subject.items()
                if k
                in [
                    "username",
                    "full_name",
                    "profile_pic_url",
                    "media_count",
                    "follower_count",
                    "following_count",
                    "biography",
                    "public_email",
                    "public_phone_number",
                    "whatsapp_number",
                ]
            }
            self.filtered_info_about_subjects.append(sorted_dictionary)


if __name__ == "__main__":
    instagram_object = Instagram("cocacola")
    instagram_object.instagram()
    print(instagram_object.filtered_info_about_subjects)
