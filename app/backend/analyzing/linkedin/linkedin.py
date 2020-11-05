# -*- coding: utf-8 -*-
from app.backend.analyzing.linkedin._linkedin_functions import linkedin_analyze


def caller_analyze_linkedin(scraping_response):
    filtered_linkedin_response = linkedin_analyze(scraping_response)
    return filtered_linkedin_response
