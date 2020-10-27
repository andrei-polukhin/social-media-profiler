from app.backend.data_scraping.twitter.twitter_authorization import TwitterAuthorize


class TwitterSearchSubjects(TwitterAuthorize):
    def __init__(self, query):
        super(TwitterSearchSubjects, self).__init__()
        self.query = query
        self.list_of_found_subjects = []
        self.ids_of_found_subjects = []

    def twitter_search(self):
        pass

    def twitter_search_subjects_with_api(self):
        self.list_of_found_subjects = self.api.search_users(
            self.query
        )
        self.ids_of_found_subjects = list(
            map(lambda x: x.id, self.list_of_found_subjects)
        )
