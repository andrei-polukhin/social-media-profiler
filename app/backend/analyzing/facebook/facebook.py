# -*- coding: utf-8 -*-
from app.backend.analyzing.facebook._facebook_class import FacebookAnalyze


def caller_analyze_facebook(scraping_response, user_input):
    results_to_visualize = {}
    facebook_obj = FacebookAnalyze(scraping_response, user_input)
    facebook_obj.facebook_analyze()
    results_to_visualize["facebook"] = facebook_obj.user_info_after_profile_name_filter
    return results_to_visualize


if __name__ == "__main__":
    facebook_browser_response = {'facebook': [{'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.caughey.921/'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.mcgaughey.3/', 'name_if_profile': 'Evan McGaughey'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.mccauley.73/', 'name_if_profile': 'Evan McCauley'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/E.EvanM.McG/'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.mccaughan/'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/evan.mcconaughey/', 'name_if_profile': 'Evan McConaughey'}, {'service_name': 'Facebook Profile', 'link': 'https://www.facebook.com/amccaughey1/', 'name_if_profile': 'Amanda Riel'}, {'service_name': 'Facebook Group', 'link': 'https://www.facebook.com/groups/Scottycameronbuysell1/'}]}
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
    print(caller_analyze_facebook(facebook_browser_response, taken_input))
