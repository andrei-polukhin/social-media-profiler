# -*- coding: utf-8 -*-
"""The Instagram main analyzing module."""
from app.backend.analyzing.instagram._instagram_class import InstagramAnalyze


def caller_analyze_instagram(scraping_response: dict, user_input: dict) -> dict:
    """
    Take user input and filter all scraped Instagram profiles.

    Args:
         `scraping_response`: the dict that has been received after scraping.\n
         `user_input`: user input represented as a dict.
    Returns:
        `dict`: the dictionary with filtered Instagram profiles.
    """
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
    api_response = {'instagram': [{'username': 'fuck.em.idc', 'full_name': 'Denis Voitsekovsky', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/121415543_4529988857071822_3830538197733517469_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=oZTxW93A4L0AX902WQu&tp=1&oh=2e34b7f33346aa5738bcfaed92244fba&oe=5FE3B690', 'media_count': 1, 'follower_count': 414, 'following_count': 582, 'biography': 'hate being sober', 'public_email': '', 'public_phone_number': '', 'whatsapp_number': ''}, {'username': 'fuck_em_boa', 'full_name': 'idc', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/14717550_1259212560787694_8200461034838818816_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=F9R0LGUPfAsAX-WDE8s&tp=1&oh=ed52bd725741903f03791882bb7e32e6&oe=5FE2DC10', 'media_count': 0, 'follower_count': 398, 'following_count': 1488, 'biography': "don't use this account anymore follow @lilkinggabe", 'whatsapp_number': ''}, {'username': 'fuckit.idc', 'full_name': 'kill em with kindness🙂', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/14288013_657459741079511_1682470100_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=KElzjHFzHUIAX-W6G4r&tp=1&oh=05004de8fc7f2731886207d01d3b0fbc&oe=5FE36D90', 'media_count': 0, 'follower_count': 1, 'following_count': 0, 'biography': 'im not living, just surviving.', 'whatsapp_number': ''}, {'username': 'fuck.off.idc', 'full_name': 'Emma🌻', 'profile_pic_url': 'https://instagram.fssa6-2.fna.fbcdn.net/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fssa6-2.fna.fbcdn.net&_nc_ohc=eJfynleCkQkAX9w2Xim&oh=9ad35e4dfcb1ec7e29344f6219a7c862&oe=5FE54B0F&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2', 'media_count': 2, 'follower_count': 23, 'following_count': 69, 'biography': 'Lesbian//Leicester//restarting feed//works at JD sports 😋', 'whatsapp_number': ''}, {'username': 'idcemilie', 'full_name': 'fuck deg', 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/13740947_627403560751764_1198861129_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=KSBrtfwJpVMAX9vFvrl&tp=1&oh=39e21724760ddadd54bf7f7808f8b945&oe=5FE4CB9F', 'media_count': 0, 'follower_count': 3, 'following_count': 3, 'biography': '', 'whatsapp_number': ''}]}
    taken_input = {
        "first_name": "Denis",
        "last_name": "Voitsekovsky",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "MIT University",
        "twitter_profile": "abumetsov",
        "instagram_nickname": "",
        "location": "Ukraine",
        "additional_text": "hate sober people"
    }
    print(caller_analyze_instagram(api_response, taken_input))
