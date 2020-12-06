# -*- coding: utf-8 -*-
"""The LinkedIn main scraping module."""

from app.backend.scraping.linkedin._linkedin_search_info import (
    LinkedinSearchSubjects,
)


def caller_linkedin(user_input: dict) -> dict:
    """
    Call LinkedIn scraping methods to get info about found and potential subjects.

    Args:
        `user_input`: user input represented as a dictionary.
    Returns:
        `dict`: the dictionary with information about found or potential subjects.
    """
    results_to_filter = {}
    linkedin_obj = LinkedinSearchSubjects(user_input)
    linkedin_obj.linkedin_search()
    linkedin_obj.linkedin_find_ids()
    linkedin_obj.linkedin_search_for_info()
    if linkedin_obj.found_subjects_info:
        results_to_filter["linkedin"] = \
            {"found_subjects": linkedin_obj.found_subjects_info}
    else:
        results_to_filter["linkedin"] = \
            {
                "potential_subjects_after_filtering":
                    linkedin_obj.potential_subjects_info_after_filtering
        }
    return results_to_filter
