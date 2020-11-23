# -*- coding: utf-8 -*-
"""The Facebook main analyzing module."""

from app.backend.analyzing.facebook._facebook_class import FacebookAnalyze


def caller_analyze_facebook(scraping_response: dict, user_input: dict) -> dict:
    """
    Call Facebook analyzing methods to filter scraped Facebook profiles.

    Args:
         `scraping_response`: the dict that has been received after scraping.\n
         `user_input`: user input represented as a dict.\n
    Returns:
        `dict`: the dictionary of analyzed and filtered Facebook subjects.
    """
    results_to_visualize = {}
    facebook_obj = FacebookAnalyze(scraping_response, user_input)
    facebook_obj.facebook_analyze()
    results_to_visualize["facebook"] = facebook_obj.user_info_after_profile_name_filter
    return results_to_visualize
