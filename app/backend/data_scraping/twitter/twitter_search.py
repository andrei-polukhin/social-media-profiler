from app.backend.data_scraping.twitter.twitter_authorize \
    import TwitterAuthorize


class TwitterSearch(TwitterAuthorize):
    def __init__(self, query):
        super(TwitterSearch, self).__init__()
        self.query = query
        self.found_subjects = []
        self.found_subjects_info = []
        self.filtered_subjects_info = []

    def twitter_search(self):
        self.twitter_search_subjects_with_api()
        self.twitter_transform_subjects_to_dicts()
        self.twitter_filter_subjects_info()

    def twitter_search_subjects_with_api(self):
        self.found_subjects = self.api.search_users(
            self.query
        )

    def twitter_transform_subjects_to_dicts(self):
        for user_object in self.found_subjects:
            user_as_dict = vars(user_object)
            self.found_subjects_info.append(user_as_dict)

    def twitter_filter_subjects_info(self):
        for subject_info in self.found_subjects_info:
            filtered_subject_info = {
                k: v
                for k, v in subject_info.items()
                if k in [
                    "name",
                    "screen_name",
                    "location",
                    "description",
                    "followers_count",
                    "friends_count",
                    "profile_image_url_https",
                    "url"

                ]
            }
            self.filtered_subjects_info.append(filtered_subject_info)


if __name__ == "__main__":
    twitter_obj = TwitterSearch("bumetsov")
    twitter_obj.twitter_authorize()
    twitter_obj.twitter_search()
    print(twitter_obj.filtered_subjects_info)
