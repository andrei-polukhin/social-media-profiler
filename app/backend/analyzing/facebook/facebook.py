# -*- coding: utf-8 -*-
"""The Facebook main analyzing module."""

from app.backend.analyzing.facebook._facebook_class import FacebookAnalyze


def caller_analyze_facebook(scraping_response: dict, user_input: dict) -> dict:
    """
    Call Facebook analyzing methods to filter scraped Facebook profiles.

    Args:
         scraping_response: the dict that has been received after scraping.
         user_input: user input represented as a dict.
    Returns:
        dict: the dictionary of analyzed and filtered Facebook subjects.
    """
    results_to_visualize = {}
    facebook_obj = FacebookAnalyze(scraping_response, user_input)
    facebook_obj.facebook_analyze()
    results_to_visualize["facebook"] = facebook_obj.user_info_after_profile_name_filter
    return results_to_visualize


if __name__ == "__main__":
    sample_facebook_response = {'facebook': [{'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.mccauley.73/', 'Profile name: ': 'Evan McCauley'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.mccauley.9/', 'Profile name: ': 'Evan McCauley'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.mccauley.7/', 'Profile name: ': 'Evan McCauley'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.mccauley.5/', 'Profile name: ': 'Evan McCauley'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.mccauley/', 'Profile name: ': 'Evan E McCauley'}]}
    taken_input = {
        "first_name": "Evan",
        "last_name": "McCauley",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "MIT University",
        "twitter_profile": "abumetsov",
        "instagram_profile": "Wayfarersbook",
        "location": "Ukraine",
        "additional_text": "CELTA/Delta teacher"
    }
    print(caller_analyze_facebook(sample_facebook_response, taken_input))
