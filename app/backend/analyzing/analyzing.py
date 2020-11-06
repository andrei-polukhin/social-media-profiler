# -*- coding: utf-8 -*-
from concurrent.futures import ProcessPoolExecutor

from app.backend.analyzing.facebook.facebook import caller_analyze_facebook
from app.backend.analyzing.instagram.instagram import caller_analyze_instagram
from app.backend.analyzing.linkedin.linkedin import caller_analyze_linkedin
from app.backend.analyzing.twitter.twitter import caller_analyze_twitter


def main_analyzing(scraping_response, user_input):
    with ProcessPoolExecutor(max_workers=4) as pool:
        facebook_process = pool.submit(
            caller_analyze_facebook, scraping_response=scraping_response, user_input=user_input
        )
        instagram_process = pool.submit(
            caller_analyze_instagram, scraping_response=scraping_response, user_input=user_input
        )
        linkedin_process = pool.submit(
            caller_analyze_linkedin, scraping_response=scraping_response
        )
        twitter_process = pool.submit(
            caller_analyze_twitter, scraping_response=scraping_response, user_input=user_input
        )
    analysis_results = {
        **facebook_process.result(),
        **instagram_process.result(),
        **linkedin_process.result(),
        **twitter_process.result(),
    }
    return analysis_results
