# -*- coding: utf-8 -*-

import unittest
import re
from app.backend.scraping.twitter.twitter import caller_twitter


class TestScrapingTwitter(unittest.TestCase):
    # In case you want to test on your PC, uncomment the line below
    # load_dotenv("app/backend/scraping/.env")
    query = "abumetsov"

    def setUp(self):
        scraping_response = caller_twitter(TestScrapingTwitter.query)
        self.tuples_of_info_and_posts = scraping_response["twitter"]

    def test_commit_preliminary_check(self):
        self.assertIsInstance(self.tuples_of_info_and_posts, list)
        for tuple_of_info_and_posts in self.tuples_of_info_and_posts:
            self.assertIsInstance(tuple_of_info_and_posts, tuple)
            subject_info = tuple_of_info_and_posts[0]
            posts = tuple_of_info_and_posts[1]
            self.assertIsInstance(subject_info, dict)
            self.assertIsInstance(posts, list)

    def test_assure_contents_of_return(self):
        for tuple_of_info_and_posts in self.tuples_of_info_and_posts:
            subject_info = tuple_of_info_and_posts[0]
            allowed_keys = [
                "name",
                "screen_name",
                "location",
                "description",
                "followers_count",
                "friends_count",
                "profile_image_url_https",
                "url",
            ]
            for k in subject_info.keys():
                self.assertIn(k, allowed_keys)
            posts = tuple_of_info_and_posts[1]
            for post in posts:
                self.assertFalse(re.match(r"http\S+", post))
