# -*- coding: utf-8 -*-
import re
from app.backend.scraping.twitter._twitter_authorize import TwitterAuthorize


class TwitterSearch(TwitterAuthorize):
    def __init__(self, query):
        super().__init__()
        self.query = query
        self._found_subjects = []
        self._found_subjects_info = []
        self._subject_screen_name = []
        self.filtered_subjects_info = []
        self.subjects_posts_text = []

    def twitter_search(self):
        self._twitter_search_subjects_with_api()
        self._twitter_transform_subjects_to_dicts()
        self._twitter_filter_subjects_info()
        self._twitter_get_and_filter_subjects_posts()

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
            self._subject_screen_name.append(filtered_subject_info["screen_name"])

    def _twitter_get_and_filter_subjects_posts(self):
        for subject_screen_name in self._subject_screen_name:
            subject_posts = self._api.user_timeline(screen_name=subject_screen_name)
            list_for_subject_posts_text = []
            for subject_post in subject_posts:
                post_text = subject_post.text
                # Replace links to tweets with empty strings using regex
                cleaned_tweet = re.sub(r"http\S+", "", post_text)
                list_for_subject_posts_text.append(cleaned_tweet)
            self.subjects_posts_text.append(list_for_subject_posts_text)


if __name__ == "__main__":
    twitter_obj = TwitterSearch("bumetsov")
    twitter_obj.twitter_authorize()
    twitter_obj.twitter_search()
    print(twitter_obj.filtered_subjects_info)
