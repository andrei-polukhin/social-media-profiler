# -*- coding: utf-8 -*-

import pickle
import unittest
from app.backend.analyzing.twitter.twitter import caller_analyze_twitter
from app.backend.analyzing.substring_match.find_similarity_ratio import (
    find_similarity_ratio,
)


class TestAnalyzingTwitter(unittest.TestCase):
    user_input = {
        "first_name": "Amy",
        "last_name": "Butler",
        "company": "Firefox",
        "job_title": "Senior EAP teacher",
        "school": "MIT University",
        "twitter_profile": "",
        "instagram_profile": "",
        "location": "Ukraine",
        "additional_text": "CELTA English teacher",
    }

    def setUp(self):
        with open("resources/twitter_analyzing_resource.pickle", "rb") as file:
            scraped_data = pickle.load(file)
        analyzing_response = caller_analyze_twitter(
            scraped_data, TestAnalyzingTwitter.user_input
        )
        subjects_dictionary = analyzing_response["twitter"]
        (
            (self.character_of_return, self.returned_subjects),
        ) = subjects_dictionary.items()

    def test_commit_preliminary_check(self):
        self.assertEqual(self.character_of_return, "potential_subjects")
        self.assertEqual(len(self.returned_subjects), 1)
        self.assertIsInstance(self.returned_subjects[0], tuple)
        self.assertEqual(len(self.returned_subjects[0]), 2)
        self.assertIsInstance(self.returned_subjects[0][0], dict)
        self.assertIsInstance(self.returned_subjects[0][1], list)

    def test_compare_received_and_required_full_name(self):
        required_full_name = " ".join(
            [
                TestAnalyzingTwitter.user_input["first_name"],
                TestAnalyzingTwitter.user_input["last_name"],
            ]
        )
        subject_as_dict = self.returned_subjects[0][0]
        received_name = subject_as_dict["name"]
        self.assertEqual(required_full_name, received_name)

    def test_compare_received_and_required_location(self):
        required_location = TestAnalyzingTwitter.user_input["location"]
        subject_as_dict = self.returned_subjects[0][0]
        received_location = subject_as_dict["location"]
        required_location_sanitized = required_location.lower().replace(",", "")
        received_location_sanitized = received_location.lower().replace(",", "")
        required_location_as_set = set(required_location_sanitized.split())
        received_location_as_set = set(received_location_sanitized.split())
        self.assertTrue(required_location_as_set, received_location_as_set)

    def test_compare_description(self):
        required_description = TestAnalyzingTwitter.user_input["additional_text"]
        subject_as_dict = self.returned_subjects[0][0]
        received_description = subject_as_dict["description"]
        similarity_ratio = find_similarity_ratio(
            required_description, received_description
        )
        self.assertLess(similarity_ratio, 0.6)


if __name__ == "__main__":
    unittest.main()
