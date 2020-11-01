# -*- coding: utf-8 -*-
import os
from linkedin_api import Linkedin as LinkedinAPI


class LinkedinSearch:
    def __init__(self, first_name, last_name, job_title, company, school):
        self.first_name = first_name
        self.last_name = last_name
        self.keyword_company = company
        self.keyword_school = school
        self.keyword_title = job_title
        self._api = None
        self._found_subjects = []
        self._potential_subjects = []

    def linkedin_search(self):
        self._linkedin_authenticate()
        self._linkedin_search_for_subjects()

    def _linkedin_authenticate(self):
        self._api = LinkedinAPI(os.getenv("LINKEDIN_LOGIN"), os.getenv("LINKEDIN_PASSWORD"))

    def _linkedin_search_for_subjects(self):
        self._linkedin_search_in_ideal_case()
        if not self._found_subjects:
            self._linkedin_search_for_potential_candidate()

    def _linkedin_search_in_ideal_case(self):
        if self.keyword_company and self.keyword_school and self.keyword_title:
            self._found_subjects = self._api.search_people(
                keyword_first_name=self.first_name,
                keyword_last_name=self.last_name,
                keyword_company=self.keyword_company,
                keyword_school=self.keyword_school,
                keyword_title=self.keyword_title,
            )

    def _linkedin_search_for_potential_candidate(self):
        for i in range(3):
            try:
                results = self._api.search_people(
                    keyword_first_name=self.first_name,
                    keyword_last_name=self.last_name,
                    keyword_company=None
                    if i != 0
                    else self.keyword_company
                    if self.keyword_company
                    else 1 / 0,
                    keyword_school=None
                    if i != 1
                    else self.keyword_school
                    if self.keyword_school
                    else 1 / 0,
                    keyword_title=None
                    if i != 2
                    else self.keyword_title
                    if self.keyword_title
                    else 1 / 0,
                )
            except ZeroDivisionError:
                continue
            self._potential_subjects.extend(results)
