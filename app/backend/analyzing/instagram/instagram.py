# -*- coding: utf-8 -*-
"""The Instagram main analyzing module."""
from app.backend.analyzing.instagram._instagram_class import InstagramAnalyze


def caller_analyze_instagram(scraping_response: dict, user_input: dict) -> dict:
    """
    Take user input and filter all scraped Instagram profiles.

    Args:
         `scraping_response`: the dict that has been received after scraping.\n
         `user_input`: user input represented as a dict.
    Returns:
        `dict`: the dictionary with filtered Instagram profiles.
    """
    results_to_visualize = {}
    instagram_obj = InstagramAnalyze(scraping_response, user_input)
    instagram_obj.instagram_analyze()
    if instagram_obj.user_info_after_desc_filter:
        results_to_visualize["instagram"] = {
            "found_subjects": instagram_obj.user_info_after_desc_filter
        }
    else:
        results_to_visualize["instagram"] = {
            "potential_subjects": instagram_obj.user_info_after_name_filter
        }
    return results_to_visualize
