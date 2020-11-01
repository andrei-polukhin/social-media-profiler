# -*- coding: utf-8 -*-
from collections import Counter

from app.backend.scraping.linkedin._linkedin_search import LinkedinSearch


class LinkedinFindIds(LinkedinSearch):
    def __init__(self, first_name, last_name, job_title, company, school):
        super().__init__(first_name, last_name, job_title, company, school)
        self._found_subjects_public_ids = []
        self._potential_subjects_public_ids = []
        self._potential_subjects_ids_after_filtering = []

    def linkedin_find_ids(self):
        if self._found_subjects:
            self._linkedin_get_found_subjects_ids()
        else:
            self._linkedin_get_potential_subjects_ids()
            self._linkedin_sort_potential_subjects_ids_by_frequency()

    def _linkedin_get_found_subjects_ids(self):
        for subject_as_dict in self._found_subjects:
            self._found_subjects_public_ids.append(
                subject_as_dict["public_id"]
            )

    def _linkedin_get_potential_subjects_ids(self):
        for subject_as_dict in self._potential_subjects:
            self._potential_subjects_public_ids.append(
                subject_as_dict["public_id"]
            )

    def _linkedin_sort_potential_subjects_ids_by_frequency(self):
        counted_candidates_ids = Counter(self._potential_subjects_public_ids)
        for candidate_id, frequency in counted_candidates_ids.items():
            if frequency == 3:
                self._found_subjects_public_ids.append(candidate_id)
                break
            if frequency == 2:
                self._potential_subjects_ids_after_filtering.append(
                    candidate_id
                )
