# -*- coding: utf-8 -*-
from app.backend.scraping.linkedin._linkedin_filter import LinkedinFilter


class LinkedinSearchSubjects(LinkedinFilter):
    def __init__(self, first_name, last_name, job_title, company, school):
        super().__init__(first_name, last_name, job_title, company, school)
        self.found_subjects_info = []
        self.potential_subjects_after_filtering_info = []
        self.searching_instructions = {}

    def linkedin_search_for_info(self):
        self._linkedin_search_for_all_subjects()
        self._linkedin_filter_all_subjects()

    def _linkedin_search_for_all_subjects(self):
        self.searching_instructions = {
            0: {0: self.found_subjects, 1: self.found_subjects_info},
            1: {
                0: self.potential_subjects_after_filtering,
                1: self.potential_subjects_after_filtering_info,
            },
        }
        for dictionary_as_instructions in self.searching_instructions.values():
            list_of_ids = dictionary_as_instructions[0]
            list_to_append_subjects = dictionary_as_instructions[1]
            for subject_id in list_of_ids:
                subject_info = self.api.get_profile(subject_id)
                list_to_append_subjects.append(subject_info)

    def _linkedin_filter_all_subjects(self):
        filtering_lists = [
            self.found_subjects_info,
            self.potential_subjects_after_filtering_info,
        ]
        for list_to_filter in filtering_lists:
            for i, returned_obj in enumerate(list_to_filter):
                standardized_properties = {
                    k: v
                    for k, v in returned_obj.items()
                    if k
                    in [
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
                }
                list_to_filter[i] = standardized_properties
