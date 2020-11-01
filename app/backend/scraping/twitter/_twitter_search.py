# -*- coding: utf-8 -*-
from app.backend.scraping.twitter._twitter_authorize import TwitterAuthorize


class TwitterSearch(TwitterAuthorize):
    def __init__(self, query):
        super().__init__()
        self.query = query
        self._found_subjects = []
        self._found_subjects_info = []
        self.filtered_subjects_info = []

    def twitter_search(self):
        self._twitter_search_subjects_with_api()
        self._twitter_transform_subjects_to_dicts()
        self._twitter_filter_subjects_info()

    def _twitter_search_subjects_with_api(self):
        self._found_subjects = self._api.search_users(self.query)

    def _twitter_transform_subjects_to_dicts(self):
        for user_object in self._found_subjects:
            user_as_dict = vars(user_object)
            self._found_subjects_info.append(user_as_dict)

    def _twitter_filter_subjects_info(self):
        for subject_info in self._found_subjects_info:
            filtered_subject_info = {
                k: v
                for k, v in subject_info.items()
                if k
                in [
                    "name",
                    "screen_name",
                    "location",
                    "description",
                    "followers_count",
                    "friends_count",
                    "profile_image_url_https",
                    "url",
                ]
            }
            self.filtered_subjects_info.append(filtered_subject_info)


if __name__ == "__main__":
    twitter_obj = TwitterSearch("bumetsov")
    twitter_obj.twitter_authorize()
    twitter_obj.twitter_search()
    print(twitter_obj.filtered_subjects_info)
