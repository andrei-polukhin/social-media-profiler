# -*- coding: utf-8 -*-
"""The main Twitter analyzing module."""

from app.backend.analyzing.twitter._twitter_class import TwitterAnalyze


def caller_analyze_twitter(scraping_response: dict, user_input: dict) -> dict:
    """
    Take scraping response and run Twitter methods to filter it according to the user input.

    Args:
        `scraping_response`: the dict that has been received after scraping.\n
        `user_input`: user input represented as a dict.
    Returns:
        `dict`: the dictionary with filtered Twitter profiles.
    """
    results_to_visualize = {}
    twitter_obj = TwitterAnalyze(scraping_response, user_input)
    twitter_obj.twitter_analyze()
    if twitter_obj.tuples_after_all_filters:
        results_to_visualize["twitter"] = {
            "found_subjects": twitter_obj.tuples_after_all_filters
        }
    else:
        results_to_visualize["twitter"] = {
            "potential_subjects": twitter_obj.tuples_after_location_filter
        }
    return results_to_visualize
