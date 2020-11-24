# -*- coding: utf-8 -*-

import unittest
from dotenv import load_dotenv
from app.backend.scraping.facebook.facebook import caller_facebook


class TestScrapingFacebook(unittest.TestCase):
    load_dotenv("../app/backend/scraping/.env")
    full_name = "Evan McCauley"

    def setUp(self):
        returned_dictionary = caller_facebook(TestScrapingFacebook.full_name)
        self.list_of_subjects_as_dicts = returned_dictionary["facebook"]

    def test_preliminary_check_of_type_of_return(self):
        for subject_as_dict in self.list_of_subjects_as_dicts:
            self.assertIsInstance(subject_as_dict, dict)

    def test_contents_of_each_subject_as_dict(self):
        for subject_as_dict in self.list_of_subjects_as_dicts:
            self.assertIsInstance(subject_as_dict["link"], str)
            possible_profile_names = [
                subject_as_dict.get("Profile name: "),
                subject_as_dict.get("Channel name: "),
                subject_as_dict.get("Group name: ")
            ]
            self.assertTrue(any(possible_profile_names))
