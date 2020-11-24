# -*- coding: utf-8 -*-

import json
import unittest
from app.backend.analyzing.linkedin.linkedin import caller_analyze_linkedin


class TestAnalyzingLinkedin(unittest.TestCase):
    def setUp(self):
        with open("resources/linkedin_analyzing_resource.json") as file:
            scraping_response = json.load(file)
        analyzing_response = caller_analyze_linkedin(scraping_response)
        dict_after_analysis = analyzing_response["linkedin"]
        (
            (self.character_of_return, self.list_of_subjects),
        ) = dict_after_analysis.items()

    def test_for_no_additions(self):
        self.assertEqual(self.character_of_return, "found_subjects")
        self.assertEqual(len(self.list_of_subjects), 1)

    def test_filtering_certifications(self):
        for subject in self.list_of_subjects:
            list_of_subject_certifications = subject["certifications"]
            for subject_certification in list_of_subject_certifications:
                subject_certification.pop("authority", None)
                subject_certification.pop("name", None)
                subject_certification.pop("timePeriod", None)
                subject_certification.pop("url", None)
                self.assertFalse(subject_certification)

    def test_filtering_education(self):
        for subject in self.list_of_subjects:
            list_of_subject_education = subject["education"]
            for subject_education in list_of_subject_education:
                subject_education.pop("degreeName", None)
                subject_education.pop("fieldOfStudy", None)
                subject_education.pop("schoolName", None)
                subject_education.pop("timePeriod", None)
                self.assertFalse(subject_education)

    def test_filtering_experience(self):
        for subject in self.list_of_subjects:
            list_of_subject_experience = subject["experience"]
            for subject_experience in list_of_subject_experience:
                subject_experience.pop("company", None)
                subject_experience.pop("companyName", None)
                subject_experience.pop("locationName", None)
                subject_experience.pop("timePeriod", None)
                subject_experience.pop("title", None)
                self.assertFalse(subject_experience)

    def test_filtering_skills(self):
        for subject in self.list_of_subjects:
            list_of_subject_education = subject["skills"]
            for subject_education in list_of_subject_education:
                subject_education.pop("name", None)
                self.assertFalse(subject_education)


if __name__ == "__main__":
    unittest.main()
