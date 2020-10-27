from app.backend.data_scraping.twitter.twitter_search import TwitterSearch


def caller_twitter(query):
    results_to_filter = {}
    twitter_obj = TwitterSearch(query)
    twitter_obj.twitter_authorize()
    twitter_obj.twitter_search()
    found_subjects = twitter_obj.filtered_subjects_info
    results_to_filter["twitter"] = found_subjects
    return results_to_filter


if __name__ == "__main__":
    print(caller_twitter("code"))
