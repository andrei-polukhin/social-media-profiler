# -*- coding: utf-8 -*-
"""The main backend module."""

from app.backend.scraping.scraping import main_scraping
from app.backend.analyzing.analyzing import main_analyzing
from app.backend.visualization.visualization import main_visualization


def main_backend(user_input: dict, pdf_output_location: str):
    """
    Commit scraping, analysis and visualization.

    Args:
         user_input: the app's user input represented as a dict.
         pdf_output_location: the location on the PC where to output the PDF file.
    Returns:
        None: visualized PDF file.
    """
    scraping_results = main_scraping(user_input)
    analysis_results = main_analyzing(
        scraping_response=scraping_results, user_input=user_input
    )
    main_visualization(
        analysis_response=analysis_results, user_input=user_input,
        pdf_output_location=pdf_output_location
    )


if __name__ == '__main__':
    sample_input = {
        "first_name": "Amy",
        "last_name": "Butler",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "Cambridge University",
        "twitter_profile": "abumetsov",
        "instagram_nickname": "Wayfarersbook",
        "location": "Ukraine",
        "additional_text": "CELTA/Delta qualified English teacher",
    }
    LOCATION = "/home/andrew/Downloads"
    main_backend(sample_input, LOCATION)
