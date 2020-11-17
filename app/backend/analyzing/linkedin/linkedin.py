# -*- coding: utf-8 -*-
"""The LinkedIn main analyzing module."""

from app.backend.analyzing.linkedin._linkedin_functions import linkedin_analyze


def caller_analyze_linkedin(scraping_response: dict) -> dict:
    """
    Take an initial scraping response and run filtering mechanisms against it.

    Args:
         `scraping_response`: the dict that has been received after scraping.
    Returns:
        `dict`: the dictionary with filtered information about subjects.
    """
    results_to_visualize = {}
    filtered_linkedin_response = linkedin_analyze(scraping_response)
    results_to_visualize["linkedin"] = filtered_linkedin_response
    return results_to_visualize
