# -*- coding: utf-8 -*-
from collections import Counter

from app.backend.scraping.linkedin._linkedin_search import LinkedinSearch


class LinkedinFilter(LinkedinSearch):
    def __init__(self, first_name, last_name, job_title, company, school):
        super().__init__(first_name, last_name, job_title, company, school)
        self._potential_subjects_public_ids = []
        self._potential_subjects_after_filtering = []

    def linkedin_filter(self):
        if not self._found_subjects:
            self._linkedin_get_subjects_ids()
            self._linkedin_sort_subjects_public_ids_by_frequency_in_list()

    def _linkedin_get_subjects_ids(self):
        for subject_as_dict in self._potential_subjects:
            self._potential_subjects_public_ids.append(
                subject_as_dict["public_id"]
            )

    def _linkedin_sort_subjects_public_ids_by_frequency_in_list(self):
        counted_candidates_ids = Counter(self._potential_subjects_public_ids)
        for candidate_id, frequency in counted_candidates_ids.items():
            if frequency == 3:
                self._found_subjects.append(candidate_id)
                break
            if frequency == 2:
                self._potential_subjects_after_filtering.append(candidate_id)
