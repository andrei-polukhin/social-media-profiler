# -*- coding: utf-8 -*-
"""The LinkedIn scraping module to find IDs of found subjects or potential candidates."""

from collections import Counter

from app.backend.scraping.linkedin._linkedin_search import LinkedinSearch


class LinkedinFindIds(LinkedinSearch):
    """
    The class to get IDS of found subjects (if they are), \
    otherwise find IDs of potential candidates.
    """
    def __init__(self, user_input):
        super().__init__(user_input)
        self._found_subjects_public_ids = []
        self._potential_subjects_public_ids = []
        self._potential_subjects_ids_after_filtering = []

    def linkedin_find_ids(self):
        """Get IDs for appropriate subjects."""
        if self._found_subjects:
            self.__linkedin_get_found_subjects_ids()
        else:
            self.__linkedin_get_potential_subjects_ids()
            self.__linkedin_sort_potential_subjects_ids_by_frequency()

    def __linkedin_get_found_subjects_ids(self):
        """Get IDs of the found subjects only."""
        for subject_as_dict in self._found_subjects:
            self._found_subjects_public_ids.append(
                subject_as_dict["public_id"]
            )

    def __linkedin_get_potential_subjects_ids(self):
        """Get IDs of potential candidates only."""
        for subject_as_dict in self._potential_subjects:
            self._potential_subjects_public_ids.append(
                subject_as_dict["public_id"]
            )

    def __linkedin_sort_potential_subjects_ids_by_frequency(self):
        """
        Sort potential candidates IDs by frequency \
        (if they are present twice - they remain potential ones after filtering, \
        if they are found 3 times - they are considered found ones after filtering).
        """
        counted_candidates_ids = Counter(self._potential_subjects_public_ids)
        for candidate_id, frequency in counted_candidates_ids.items():
            if frequency == 3:
                self._found_subjects_public_ids.append(candidate_id)
                break
            if frequency == 2:
                self._potential_subjects_ids_after_filtering.append(
                    candidate_id
                )
