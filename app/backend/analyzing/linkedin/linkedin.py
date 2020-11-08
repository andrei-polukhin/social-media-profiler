# -*- coding: utf-8 -*-
from app.backend.analyzing.linkedin._linkedin_functions import linkedin_analyze


def caller_analyze_linkedin(scraping_response):
    results_to_visualize = {}
    filtered_linkedin_response = linkedin_analyze(scraping_response)
    results_to_visualize["linkedin"] = filtered_linkedin_response
    return results_to_visualize
