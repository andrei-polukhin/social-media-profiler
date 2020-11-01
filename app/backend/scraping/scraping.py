# -*- coding: utf-8 -*-
from concurrent.futures import ProcessPoolExecutor

from app.backend.scraping.facebook.facebook import caller_facebook
from app.backend.scraping.google_search.google_search import caller_google_search
from app.backend.scraping.instagram.instagram import caller_instagram
from app.backend.scraping.linkedin.linkedin import caller_linkedin
from app.backend.scraping.twitter.twitter import caller_twitter


def main_scraping(
    first_name,
    last_name,
    company=None,
    job_title=None,
    school=None,
    twitter_profile=None,
    instagram_profile=None,
    **kwargs
):
    scraping_results = []
    full_name = " ".join([first_name, last_name])
    with ProcessPoolExecutor(max_workers=5) as pool:
        facebook_pool = pool.submit(caller_facebook, query=full_name)
        linkedin_pool = pool.submit(
            caller_linkedin,
            first_name=first_name,
            last_name=last_name,
            job_title=job_title,
            company=company,
            school=school
        )
        instagram_pool = pool.submit(
            caller_instagram,
            query=instagram_profile if instagram_profile else full_name
        )
        google_search_pool = pool.submit(
            caller_google_search, name=full_name, **kwargs
        )
        twitter_pool = pool.submit(
            caller_twitter, query=twitter_profile
            if twitter_profile else full_name
        )
    scraping_results.extend(
        [
            facebook_pool.result(),
            google_search_pool.result(),
            instagram_pool.result(),
            linkedin_pool.result(),
            twitter_pool.result(),
        ]
    )
    return scraping_results


if __name__ == "__main__":
    response = main_scraping(
        first_name="Amy",
        last_name="Butler",
        company="The London School of English",
        job_title="Director of Studies",
        school="University of Cambridge",
        twitter_profile="WayfarersBook",
        instagram_profile="wayfarersbook"
    )
    print(response)
