# -*- coding: utf-8 -*-
"""The main Twitter scraping module."""

from app.backend.scraping.twitter._twitter_search import TwitterSearch


def caller_twitter(query: str) -> dict:
    """
    Call Twitter scraping methods and write information about found subjects to the dict.

    Args:
        `query`: the query to run API calls against.
    Returns:
        `dict`: the dictionary with information about subjects found on Twitter.
    """
    results_to_filter = {}
    twitter_obj = TwitterSearch(query)
    twitter_obj.twitter_authorize()
    twitter_obj.twitter_search()
    found_subjects_info = twitter_obj.filtered_subjects_info
    found_subjects_posts = twitter_obj.subjects_posts_text
    results_to_filter["twitter"] = list(zip(found_subjects_info, found_subjects_posts))
    return results_to_filter
