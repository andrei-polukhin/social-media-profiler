# -*- coding: utf-8 -*-

import unittest
from dotenv import load_dotenv
from app.backend.scraping.linkedin.linkedin import caller_linkedin


class TestScrapingLinkedin(unittest.TestCase):
    load_dotenv("app/backend/scraping/.env")
    user_input = {
        "first_name": "Bill",
        "last_name": "Gates",
        "company": "Bill & Melinda Gates Foundation",
        "job_title": "Co-chair",
        "school": "Cambridge University",
        "twitter_profile": "",
        "instagram_nickname": "",
        "location": "California, USA",
        "additional_text": "The founder of Microsoft.",
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
