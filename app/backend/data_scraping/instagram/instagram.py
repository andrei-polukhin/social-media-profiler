from app.backend.data_scraping.instagram.instagram_class import Instagram


def caller_instagram(query):
    results_to_filter = {}
    instagram_object = Instagram(query)
    instagram_object.instagram()
    filtered_info = instagram_object.filtered_info_about_subjects
    results_to_filter["instagram"] = filtered_info
    return results_to_filter


if __name__ == "__main__":
    print(caller_instagram("cocacola"))
