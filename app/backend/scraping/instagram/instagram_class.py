from instagram_private_api import Client

from app.backend.config import INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD


class Instagram:
    def __init__(self, query):
        self.query = query
        self.api = None
        self.found_subjects = {}
        self.query_matching_users = []
        self.subject_ids = []
        self.extracted_info_about_subjects = []
        self.filtered_info_about_subjects = []

    def instagram(self):
        self._instagram_authenticate()
        self._instagram_search_for_subjects()
        self._instagram_get_ids_of_found_subjects()
        self._instagram_extract_info_with_subject_ids()
        self._instagram_filter_info_about_subjects()
        self._instagram_logout()

    def _instagram_authenticate(self):
        self.api = Client(INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD)

    def _instagram_search_for_subjects(self):
        self.found_subjects = self.api.search_users(self.query)

    def _instagram_get_ids_of_found_subjects(self):
        users_info_as_list = self.found_subjects["users"]
        for user_as_dict in users_info_as_list:
            user_id = user_as_dict["pk"]
            self.subject_ids.append(user_id)

    def _instagram_extract_info_with_subject_ids(self):
        for subject_id in self.subject_ids:
            subject_extracted_info_as_dict = self.api.user_info(subject_id)
            subject_extracted_info = subject_extracted_info_as_dict["user"]
            self.extracted_info_about_subjects.append(subject_extracted_info)

    def _instagram_filter_info_about_subjects(self):
        for info_about_subject in self.extracted_info_about_subjects:
            sorted_dictionary = {
                k: v
                for k, v in info_about_subject.items()
                if k
                in [
                    "username",
                    "full_name",
                    "profile_pic_url",
                    "media_count",
                    "follower_count",
                    "following_count",
                    "biography",
                    "public_email",
                    "public_phone_number",
                    "whatsapp_number",
                ]
            }
            self.filtered_info_about_subjects.append(sorted_dictionary)

    def _instagram_logout(self):
        self.api.logout()


if __name__ == "__main__":
    instagram_object = Instagram("cocacola")
    instagram_object.instagram()
    print(instagram_object.filtered_info_about_subjects)
