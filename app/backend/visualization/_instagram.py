# -*- coding: utf-8 -*-
from app.backend.visualization.helpers.split_string import split_string_in_words_with_len_limit
from app.backend.visualization.helpers.get_and_process_image import get_and_process_image
from fpdf import FPDF


class InstagramVisualize(FPDF):
    def __init__(self, analysis_response=None):
        super().__init__()
        self.analysis_response = analysis_response
        self.list_of_instagram_subjects = []
        self.set_doc_option("core_fonts_encoding", "windows-1252")

    def instagram_visualize(self):
        self.list_of_instagram_subjects = self.analysis_response["instagram"]
        if any(self.list_of_instagram_subjects.values()):
            self._instagram_visualize_write_title()
            self._instagram_visualize_write_info_about_each_subject()

    def _instagram_visualize_write_title(self):
        self.set_font("Times", "BI", size=16)
        self.cell(w=0, h=5, txt="Instagram", ln=2)

    def _instagram_visualize_write_info_about_each_subject(self):
        self.set_font("Times", "I", size=14)
        if len(self.list_of_instagram_subjects) > 1:
            self.cell(w=0, h=5, txt="Potential users", ln=2)
        self.ln(5)
        self.set_font("Times", size=14)
        for subject in self.list_of_instagram_subjects:
            self._instagram_visualize_process_and_visualize_image(subject)
            self._instagram_visualize_put_info_in_bullet_list(subject)
            self.ln(15)
        self.ln()
        current_abscissa = self.get_x()
        current_ordinate = self.get_y()
        self.line(
            current_abscissa, current_ordinate - 10, 210 - current_abscissa, current_ordinate - 10
        )
        # """For TEST:""" self.cell(w=0, txt="HIII!!!")

    def _instagram_visualize_process_and_visualize_image(self, subject):
        subject_image_url = subject["profile_pic_url"]
        processed_image = get_and_process_image(subject_image_url)
        self.image(name=processed_image, w=45, h=45)

    def _instagram_visualize_put_info_in_bullet_list(self, subject):
        current_ordinate = self.get_y()
        self.set_xy(65, current_ordinate - 40)
        username = subject["username"]
        self.cell(
            w=0, h=6, txt=f"\u2022 Instagram nickname: {username}", ln=2,
            link=f"https://www.instagram.com/{username}/"
        )
        biography = subject["biography"]
        biography_processed = split_string_in_words_with_len_limit(biography)
        self.cell(
            w=0, h=6, txt=u"\u2022 Biography: {}".format(biography_processed),
            ln=2
        )
        full_name = subject["full_name"]
        self.cell(w=0, h=6, txt=f"\u2022 Full name: {full_name}", ln=2)
        media_count = subject["media_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Media count: {media_count}", ln=2)
        number_of_followers = subject["follower_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Number of followers: {number_of_followers}", ln=2)
        number_of_following = subject["following_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Number of following: {number_of_following}", ln=2)


if __name__ == "__main__":
    instagram_dict = {'instagram': [{'biography': "The Wayfarer's Bookshop est. 1996 specializes in rare exploration, travel and voyage related items", 'follower_count': 56, 'following_count': 10, 'full_name': 'Eric Peter Waschke', 'media_count': 0, 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/69569940_450144195583218_4396135465405644800_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=dQA0tdaNQr8AX-J5d3N&oh=55edb598eb2014804c32c10a5d96faaa&oe=5FC8203B', 'username': 'wayfarersbookshop', 'whatsapp_number': ''}, {'biography': '21. Edinburgh bookseller. Wayfarer. Professionally quirky and curious. She/her or They/Them. Hufflepuff.', 'follower_count': 157, 'following_count': 331, 'full_name': 'Niall', 'media_count': 54, 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/18513669_1390552421001286_650901666643574784_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=d7t2KwrpFG0AX_powxk&oh=f6e1bb5c3338bcc1da9711eb1fe08a48&oe=5FC7DB97', 'username': 'wayfarersbooks', 'whatsapp_number': ''}, {'biography': '21. Edinburgh bookseller. Wayfarer. Professionally quirky and curious. She/her or They/Them. Hufflepuff.', 'follower_count': 157, 'following_count': 331, 'full_name': 'Niall', 'media_count': 54, 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/18513669_1390552421001286_650901666643574784_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=d7t2KwrpFG0AX_powxk&oh=f6e1bb5c3338bcc1da9711eb1fe08a48&oe=5FC7DB97', 'username': 'wayfarersbooks', 'whatsapp_number': ''}]}
    pdf = InstagramVisualize(instagram_dict)
    pdf.add_page()
    pdf.instagram_visualize()
    pdf.output("class.pdf")
