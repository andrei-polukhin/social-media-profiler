# -*- coding: utf-8 -*-
from app.backend.scraping.linkedin._linkedin_search_info import (
    LinkedinSearchSubjects,
)


def caller_linkedin(user_input):
    results_to_filter = {}
    linkedin_obj = LinkedinSearchSubjects(user_input)
    linkedin_obj.linkedin_search()
    linkedin_obj.linkedin_find_ids()
    linkedin_obj.linkedin_search_for_info()
    if linkedin_obj.found_subjects_info:
        results_to_filter["linkedin"] = \
            {"found_subjects": linkedin_obj.found_subjects_info}
    else:
        results_to_filter["linkedin"] = \
            {
                "potential_subjects_after_filtering":
                    linkedin_obj.potential_subjects_info_after_filtering
            }
    return results_to_filter


if __name__ == "__main__":
    sample_user_input = {
        "first_name": "Amy",
        "last_name": "Butler",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "Cambridge University",
        "twitter_profile": "abumetsov",
        "instagram_nickname": "Wayfarersbook",
        "location": "Ukraine",
        "additional_text": "CELTA/Delta teacher",
    }
    print(caller_linkedin(sample_user_input))