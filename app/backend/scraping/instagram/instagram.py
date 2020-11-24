# -*- coding: utf-8 -*-
"""The main Instagram scraping module."""

from app.backend.scraping.instagram._instagram_class import Instagram


def caller_instagram(query: str) -> dict:
    """
    Call other Instagram scraping functions to get filtered info about person.

    Args:
        `query`: the query to run Instagram API and filtering functions against.
    Returns:
        `dict`: the dictionary with potential information about a desired person.
    """
    results_to_filter = {}
    instagram_object = Instagram(query)
    instagram_object.instagram()
    filtered_info = instagram_object.filtered_info_about_subjects
    results_to_filter["instagram"] = filtered_info
    return results_to_filter
