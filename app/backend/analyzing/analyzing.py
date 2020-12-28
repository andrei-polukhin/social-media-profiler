# -*- coding: utf-8 -*-
"""The main analyzing module."""

from concurrent.futures import ProcessPoolExecutor

from app.backend.analyzing.instagram.instagram import caller_analyze_instagram
from app.backend.analyzing.linkedin.linkedin import caller_analyze_linkedin
from app.backend.analyzing.twitter.twitter import caller_analyze_twitter


def main_analyzing(scraping_response: dict, user_input: dict) -> dict:
    """
    Take scraping response and run filters according to the user input.

    Args:
        `scraping_response`: the dict that has been received after scraping.\n
        `user_input`: user input represented as a dict.
    Returns:
        `dict`: the dictionary with filtered profiles from all social media.
    """
    with ProcessPoolExecutor(max_workers=4) as pool:
        instagram_process = pool.submit(
            caller_analyze_instagram, scraping_response=scraping_response, user_input=user_input
        )
        linkedin_process = pool.submit(
            caller_analyze_linkedin, scraping_response=scraping_response
        )
        twitter_process = pool.submit(
            caller_analyze_twitter, scraping_response=scraping_response, user_input=user_input
        )
    try:
        # For Python3.9+
        analysis_results = instagram_process.result() | linkedin_process.result() | \
                           twitter_process.result()
        analysis_results["google_search"] = scraping_response["google_search"]
    except TypeError:
        # For Python <= 3.8
        analysis_results = {
            **instagram_process.result(),
            **linkedin_process.result(),
            **twitter_process.result(),
            "google_search": scraping_response["google_search"]
        }
    return analysis_results
