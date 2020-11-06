# -*- coding: utf-8 -*-
from app.backend.scraping.linkedin._linkedin_find_ids import LinkedinFindIds


class LinkedinSearchSubjects(LinkedinFindIds):
    def __init__(self, user_input):
        super().__init__(user_input)
        self.found_subjects_info = []
        self.potential_subjects_info_after_filtering = []

    def linkedin_search_for_info(self):
        self._linkedin_search_for_all_subjects()
        self._linkedin_filter_all_subjects()

    def _linkedin_search_for_all_subjects(self):
        searching_instructions = {
            0: {
                0: self._found_subjects_public_ids,
                1: self.found_subjects_info
            },
            1: {
                0: self._potential_subjects_ids_after_filtering,
                1: self.potential_subjects_info_after_filtering,
            },
        }
        for dictionary_as_instructions in searching_instructions.values():
            list_of_ids = dictionary_as_instructions[0]
            list_to_append_subjects = dictionary_as_instructions[1]
            for subject_id in list_of_ids:
                subject_info = self._api.get_profile(subject_id)
                list_to_append_subjects.append(subject_info)

    def _linkedin_filter_all_subjects(self):
        filtering_lists = [
            self.found_subjects_info,
            self.potential_subjects_info_after_filtering,
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
