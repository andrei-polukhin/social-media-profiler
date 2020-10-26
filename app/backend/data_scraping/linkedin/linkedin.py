from app.backend.data_scraping.linkedin.linkedin_class import Linkedin


def caller_linkedin(
        first_name,
        last_name,
        job_title=None,
        current_company=None,
        school=None
):
    results_to_filter = {}
    linkedin_obj = Linkedin(
        first_name,
        last_name,
        job_title,
        current_company,
        school
    )
    linkedin_obj.linkedin()
    results_to_filter["linkedin"] = list_of_all_items = []
    list_of_all_items.append(
        {"found_subjects": linkedin_obj.found_subjects}
    )
    list_of_all_items.append(
        {"potential_subjects": linkedin_obj.potential_subjects}
    )
    return results_to_filter


if __name__ == "__main__":
    print(caller_linkedin("Amy", "Butler", school="Michigan"))
