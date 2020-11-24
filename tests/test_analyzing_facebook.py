# -*- coding: utf-8 -*-

import unittest
from app.backend.analyzing.facebook.facebook import caller_analyze_facebook


class TestAnalyzingFacebook(unittest.TestCase):
    facebook_response_to_analyze = {
        "facebook": [
            {
                "service_name": "Facebook Profile",
                "link": "https://www.facebook.com/evan.mccauley.73/",
                "Profile name: ": "Evan McCauley",
            },
            {
                "service_name": "Facebook Profile",
                "link": "https://www.facebook.com/evan.mccauley.9/",
                "Profile name: ": "Evan McCauley",
            },
            {
                "service_name": "Facebook Profile",
                "link": "https://www.facebook.com/evan.mccauley.7/",
                "Profile name: ": "Evan McCauley",
            },
            {
                "service_name": "Facebook Profile",
                "link": "https://www.facebook.com/evan.mccauley.5/",
                "Profile name: ": "Evan McCauley",
            },
            {
                "service_name": "Facebook Profile",
                "link": "https://www.facebook.com/evan.mccauley/",
                "Profile name: ": "Evan E McCauley",
            },
        ]
    }
    user_input = {
        "first_name": "Evan",
        "last_name": "McCauley",
        "company": "Netflix",
        "job_title": "Junior Software Engineer",
        "school": "MIT University",
        "twitter_profile": "",
        "instagram_profile": "",
        "location": "Germany",
        "additional_text": "A C++ enthusiast.",
    }

    def setUp(self):
        analyzed_response = caller_analyze_facebook(
            TestAnalyzingFacebook.facebook_response_to_analyze,
            TestAnalyzingFacebook.user_input,
        )
        self.list_of_filtered_subjects = analyzed_response["facebook"]

    def test_assure_all_objects_are_analyzed(self):
        self.assertIsInstance(self.list_of_filtered_subjects, list)
        self.assertEqual(len(self.list_of_filtered_subjects), 4)

    def test_assure_subjects_are_found_correctly(self):
        required_full_name = " ".join(
            [
                TestAnalyzingFacebook.user_input["first_name"],
                TestAnalyzingFacebook.user_input["last_name"],
            ]
        )
        for filtered_subject in self.list_of_filtered_subjects:
            possible_profile_names = [
                filtered_subject.get("Profile name: "),
                filtered_subject.get("Channel name: "),
                filtered_subject.get("Group name: "),
            ]
            self.assertIn(required_full_name, possible_profile_names)


if __name__ == "__main__":
    unittest.main()
