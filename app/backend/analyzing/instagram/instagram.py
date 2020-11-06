# -*- coding: utf-8 -*-
from app.backend.analyzing.instagram._instagram_class import InstagramAnalyze


def caller_analyze_instagram(scraping_response, user_input):
    results_to_visualize = {}
    instagram_obj = InstagramAnalyze(scraping_response, user_input)
    instagram_obj.instagram_analyze()
    if instagram_obj.user_info_after_desc_filter:
        results_to_visualize["instagram"] = {
            "found_subjects": instagram_obj.user_info_after_desc_filter
        }
    else:
        results_to_visualize["instagram"] = {
            "potential_subjects": instagram_obj.user_info_after_name_filter
        }
    return results_to_visualize


if __name__ == "__main__":
    api_response = {'instagram': [{'username': 'wayfarersbookshop', 'full_name': 'Eric Peter Waschke', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/69569940_450144195583218_4396135465405644800_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=dQA0tdaNQr8AX-J5d3N&oh=55edb598eb2014804c32c10a5d96faaa&oe=5FC8203B', 'media_count': 0, 'follower_count': 56, 'following_count': 10, 'biography': "The Wayfarer's Bookshop est. 1996 specializes in rare exploration, travel and voyage related items", 'whatsapp_number': ''}, {'username': 'wayfarersbooks', 'full_name': 'Niall', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/18513669_1390552421001286_650901666643574784_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=d7t2KwrpFG0AX_powxk&oh=f6e1bb5c3338bcc1da9711eb1fe08a48&oe=5FC7DB97', 'media_count': 54, 'follower_count': 157, 'following_count': 331, 'biography': '21. Edinburgh bookseller. Wayfarer. Professionally quirky and curious. She/her or They/Them. Hufflepuff.', 'whatsapp_number': ''}]}
    taken_input = {
        "first_name": "Eric",
        "last_name": "Peter Waschke",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "MIT University",
        "twitter_profile": "abumetsov",
        "instagram_nickname": "",
        "location": "Ukraine",
        "additional_text": "CELTA/Delta teacher"
    }
    print(caller_analyze_instagram(api_response, taken_input))

