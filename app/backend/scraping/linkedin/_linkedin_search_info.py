# -*- coding: utf-8 -*-
"""The LinkedIn scraping module to search for info of filtered subjects."""

from app.backend.scraping.linkedin._linkedin_find_ids import LinkedinFindIds

IDS_IDX = 0
INFO_IDX = 1


class LinkedinSearchSubjects(LinkedinFindIds):
    """The class to search for info by filtered subjects' ids."""

    def __init__(self, user_input):
        super().__init__(user_input)
        self.found_subjects_info = []
        self.potential_subjects_info_after_filtering = []

    def linkedin_search_for_info(self):
        """Search for info by filtered subjects' ids."""
        self.__linkedin_search_for_all_subjects()
        self.__linkedin_filter_all_subjects()

    def __linkedin_search_for_all_subjects(self):
        """Organize API calls for all types of subjects: found and potential."""
        searching_instructions = (
            (
                self._found_subjects_public_ids,
                self.found_subjects_info
            ),
            (
                self._potential_subjects_ids_after_filtering,
                self.potential_subjects_info_after_filtering,
            ),
        )

        for dictionary_as_instructions in searching_instructions:
            list_of_ids = dictionary_as_instructions[IDS_IDX]
            list_to_append_subjects = dictionary_as_instructions[INFO_IDX]
            for subject_id in list_of_ids:
                subject_info = self._api.get_profile(subject_id)
                list_to_append_subjects.append(subject_info)

    def __linkedin_filter_all_subjects(self):
        """
        Filter the information from API and leave only information from specific keys (see code).
        """
        filtering_lists = [
            self.found_subjects_info,
            self.potential_subjects_info_after_filtering,
        ]
        for list_to_filter in filtering_lists:
            for i, returned_obj in enumerate(list_to_filter):
                standardized_properties = {
                    k: v
                    for k, v in returned_obj.items()
                    if k in [
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
