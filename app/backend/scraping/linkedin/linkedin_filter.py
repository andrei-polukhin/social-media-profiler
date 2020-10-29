from collections import Counter

from app.backend.scraping.linkedin.linkedin_search import LinkedinSearch


class LinkedinFilter(LinkedinSearch):
    def __init__(self, first_name, last_name, job_title, company, school):
        super().__init__(first_name, last_name, job_title, company, school)
        self.potential_subjects_public_ids = []
        self.potential_subjects_after_filtering = []

    def linkedin_filter(self):
        if not self.found_subjects:
            self.linkedin_get_subjects_ids()
            self.linkedin_sort_subjects_public_ids_by_frequency_in_list()

    def linkedin_get_subjects_ids(self):
        for subject_as_dict in self.potential_subjects:
            self.potential_subjects_public_ids.append(subject_as_dict["public_id"])

    def linkedin_sort_subjects_public_ids_by_frequency_in_list(self):
        counted_candidates_ids = Counter(self.potential_subjects_public_ids)
        for candidate_id, frequency in counted_candidates_ids.items():
            if frequency == 3:
                self.found_subjects.append(candidate_id)
            if frequency == 2:
                self.potential_subjects_after_filtering.append(candidate_id)
