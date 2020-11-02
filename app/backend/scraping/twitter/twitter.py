# -*- coding: utf-8 -*-
from app.backend.scraping.twitter._twitter_search import TwitterSearch


def caller_twitter(query):
    results_to_filter = {}
    twitter_obj = TwitterSearch(query)
    twitter_obj.twitter_authorize()
    twitter_obj.twitter_search()
    found_subjects_info = twitter_obj.filtered_subjects_info
    found_subjects_posts = twitter_obj.subjects_posts_text
    results_to_filter["twitter"] = list(zip(found_subjects_info, found_subjects_posts))
    return results_to_filter


if __name__ == "__main__":
    print(caller_twitter("wayfarersbook"))
