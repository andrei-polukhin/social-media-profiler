# -*- coding: utf-8 -*-

import unittest
from dotenv import load_dotenv
from app.backend.scraping.google_search.google_search import caller_google_search


class TestScrapingGoogleSearch(unittest.TestCase):
    load_dotenv("../app/backend/scraping/.env")
    user_input = {
        "first_name": "Vladyslav",
        "last_name": "Ovchynnykov",
        "company": "Amazon",
        "job_title": "QA tester",
        "school": "MIT University",
        "twitter_profile": "",
        "instagram_nickname": "",
        "location": "Ukraine",
        "additional_text": "",
        "github": "pythad",
    }

    def setUp(self):
        returned_dictionary = caller_google_search(TestScrapingGoogleSearch.user_input)
        self.dict_of_returned_info = returned_dictionary["google_search"]

    def test_preliminary_check_of_the_correctness_of_return(self):
        self.assertIsInstance(self.dict_of_returned_info, dict)
        self.assertEqual(len(self.dict_of_returned_info.keys()), 2)

    def test_check_contents_of_the_returned_info(self):
        contents = self.dict_of_returned_info
        keys = contents.keys()
        self.assertIn("name", keys)
        self.assertIn("github", keys)
        for list_of_response_for_selector in contents.values():
            for dict_of_response in list_of_response_for_selector:
                self.assertIsNotNone(dict_of_response.get("service_name"))
                self.assertIsNotNone(dict_of_response.get("link"))
