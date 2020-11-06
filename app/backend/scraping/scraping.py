# -*- coding: utf-8 -*-
from concurrent.futures import ProcessPoolExecutor
from dotenv import load_dotenv

from app.backend.scraping.facebook.facebook import caller_facebook
from app.backend.scraping.google_search.google_search import caller_google_search
from app.backend.scraping.instagram.instagram import caller_instagram
from app.backend.scraping.linkedin.linkedin import caller_linkedin
from app.backend.scraping.twitter.twitter import caller_twitter


def main_scraping(user_input):
    load_dotenv(".env")
    full_name = " ".join([user_input["first_name"], user_input["last_name"]])
    with ProcessPoolExecutor(max_workers=5) as pool:
        facebook_process = pool.submit(caller_facebook, full_name=full_name)
        linkedin_process = pool.submit(
            caller_linkedin,
            user_input=user_input
        )
        instagram_process = pool.submit(
            caller_instagram,
            query=user_input.get("instagram_profile")
            if user_input.get("instagram_profile") else full_name
        )
        google_search_process = pool.submit(
            caller_google_search, user_input=user_input
        )
        twitter_process = pool.submit(
            caller_twitter, query=user_input.get("twitter_profile")
            if user_input.get("twitter_profile") else full_name
        )
    scraping_results = {
        **facebook_process.result(),
        **google_search_process.result(),
        **instagram_process.result(),
        **linkedin_process.result(),
        **twitter_process.result(),
    }
    return scraping_results


if __name__ == "__main__":
    sample_input = {
        "first_name": "Amy",
        "last_name": "Butler",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "Cambridge University",
        "twitter_profile": "WayfarersBook",
        "instagram_nickname": "Wayfarersbook",
        "location": "Ukraine",
        "additional_text": "CELTA/Delta teacher",
    }
    response = main_scraping(sample_input)
    print(response)
