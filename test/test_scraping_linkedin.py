# -*- coding: utf-8 -*-

import unittest
from app.backend.scraping.linkedin.linkedin import caller_linkedin


class TestScrapingLinkedin(unittest.TestCase):
    # In case you want to test on your PC, uncomment the line below
    # load_dotenv("app/backend/scraping/.env")
    user_input = {
        "first_name": "Kevin",
        "last_name": "Goldsmith",
        "company": "Anaconda",
        "job_title": "Chief Technology Officer at Anaconda, Inc.",
        "school": "",
        "twitter_profile": "",
        "instagram_nickname": "",
        "location": "Seattle",
        "additional_text": "CTO at Anaconda.",
    }

    def setUp(self):
        scraping_response = caller_linkedin(TestScrapingLinkedin.user_input)
        dict_from_linkedin = scraping_response["linkedin"]
        (
            (self.character_of_return, self.returned_subjects),
        ) = dict_from_linkedin.items()

    def test_commit_preliminary_check(self):
        self.assertEqual(self.character_of_return, "potential_subjects_after_filtering")
        self.assertIsInstance(self.returned_subjects, list)
        self.assertEqual(len(self.returned_subjects), 1)

    def test_assure_contents_of_list_of_returned_subjects(self):
        returned_subject = self.returned_subjects[0]
        allowed_keys = [
            "industryName",
            "lastName",
            "locationName",
            "student",
            "geoCountryName",
            "firstName",
            "headline",
            "experience",
            "skills",
            "education",
            "languages",
            "publications",
            "certifications",
            "honors",
        ]
        for key in returned_subject.keys():
            self.assertIn(key, allowed_keys)
