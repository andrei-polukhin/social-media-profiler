from linkedin_api import Linkedin as LinkedinAPI

from app.backend.config import LINKEDIN_LOGIN, LINKEDIN_PASSWORD


class LinkedinSearch:
    def __init__(
            self,
            first_name,
            last_name,
            job_title,
            current_company,
            school
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.keyword_company = current_company
        self.keyword_school = school
        self.keyword_title = job_title
        self.api = None
        self.found_subjects = []
        self.potential_subjects = []

    def linkedin_search(self):
        self.linkedin_authenticate()
        self.linkedin_search_for_subjects()

    def linkedin_authenticate(self):
        self.api = LinkedinAPI(LINKEDIN_LOGIN, LINKEDIN_PASSWORD)

    def linkedin_search_for_subjects(self):
        self.linkedin_search_in_ideal_case()
        if not self.found_subjects:
            self.linkedin_search_for_potential_candidate()

    def linkedin_search_in_ideal_case(self):
        if self.keyword_company \
                and self.keyword_school and self.keyword_title:
            self.found_subjects = self.api.search_people(
                keyword_first_name=self.first_name,
                keyword_last_name=self.last_name,
                keyword_company=self.keyword_company,
                keyword_school=self.keyword_school,
                keyword_title=self.keyword_title
            )

    def linkedin_search_for_potential_candidate(self):
        for i in range(3):
            try:
                results = self.api.search_people(
                    keyword_first_name=self.first_name,
                    keyword_last_name=self.last_name,
                    keyword_company=None
                    if i != 0
                    else self.keyword_company if self.keyword_company
                    else 1 / 0,
                    keyword_school=None
                    if i != 1
                    else self.keyword_school if self.keyword_school else 1 / 0,
                    keyword_title=None
                    if i != 2
                    else self.keyword_title if self.keyword_title else 1 / 0
                )
            except ZeroDivisionError:
                continue
            self.potential_subjects.extend(results)
