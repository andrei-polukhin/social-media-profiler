# -*- coding: utf-8 -*-

import json
import unittest
from app.backend.analyzing.instagram.instagram import caller_analyze_instagram
from app.backend.analyzing.substring_match.find_similarity_ratio import find_similarity_ratio


class TestAnalyzingInstagram(unittest.TestCase):
    user_input = {
        "first_name": "Denis",
        "last_name": "Voitsekovsky",
        "company": "",
        "job_title": "",
        "school": "Lyceum 142",
        "twitter_profile": "",
        "instagram_nickname": "",
        "location": "Ukraine",
        "additional_text": "hate being sober"
    }

    def setUp(self):
        with open("resources/instagram_analyzing_resource.json") as file:
            self.instagram_scraping_response = json.load(file)

    def test_assure_needed_subject_is_found(self):
        analyzed_response = caller_analyze_instagram(
            self.instagram_scraping_response,
            TestAnalyzingInstagram.user_input
        )
        (character_of_response, list_of_returned_subject), = analyzed_response["instagram"].items()
        self.assertEqual(character_of_response, "found_subjects")
        self.assertEqual(len(list_of_returned_subject), 1)
        found_subject = list_of_returned_subject[0]
        # Testing the full name
        required_full_name = " ".join([
            TestAnalyzingInstagram.user_input["first_name"],
            TestAnalyzingInstagram.user_input["last_name"]
        ])
        received_full_name = found_subject["full_name"]
        self.assertEqual(required_full_name, received_full_name)
        # Testing the additional information
        required_biography = TestAnalyzingInstagram.user_input["additional_text"]
        received_biography = found_subject["biography"]
        similarity_ratio = find_similarity_ratio(required_biography, received_biography)
        self.assertGreaterEqual(similarity_ratio, 0.6)


if __name__ == '__main__':
    unittest.main()
