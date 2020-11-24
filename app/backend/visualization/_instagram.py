# -*- coding: utf-8 -*-
"""The Instagram visualization module."""

from fpdf import FPDF
from app.backend.visualization.helpers.limit_string import split_string_in_words_with_len_limit
from app.backend.visualization.helpers.get_and_process_image import get_and_process_image


class InstagramVisualize(FPDF):
    """The class to visualize Instagram information on the PDF."""
    def __init__(self, analysis_response=None):
        super().__init__()
        self.analysis_response = analysis_response
        self.dict_of_instagram_subjects = {}
        self.set_doc_option("core_fonts_encoding", "windows-1252")

    def instagram_visualize(self):
        """
        Call other methods to visualize Instagram information if there is any.
        """
        self.dict_of_instagram_subjects = self.analysis_response["instagram"]
        if any(self.dict_of_instagram_subjects.values()):
            self.__instagram_visualize_write_title()
            self.__instagram_visualize_write_info_about_each_subject()

    def __instagram_visualize_write_title(self):
        """Write the title of Instagram on the PDF."""
        self.set_font("Times", "BI", size=16)
        self.cell(w=0, h=5, txt="Instagram", ln=2)

    def __instagram_visualize_write_info_about_each_subject(self):
        """
        Visualize information about each subject on Instagram.
        """
        self.set_font("Times", "I", size=14)
        if self.dict_of_instagram_subjects.get("potential_subjects") is not None:
            self.cell(w=0, h=5, txt="Potential users", ln=2)
        self.ln(5)
        self.set_font("Times", size=14)
        list_of_subjects = list(self.dict_of_instagram_subjects.values())[0]
        for subject in list_of_subjects:
            self.__instagram_visualize_process_and_visualize_image(subject)
            self.__instagram_visualize_put_info_in_bullet_list(subject)
            self.ln(15)
        self.ln()
        self.line(
            self.get_x(), self.get_y() - 10, 210 - self.get_x(), self.get_y() - 10
        )
        # """For TEST:""" self.cell(w=0, txt="HIII!!!")

    def __instagram_visualize_process_and_visualize_image(self, subject: dict):
        """
        Get, process and visualize the Instagram profile image.
        """
        subject_image_url = subject["profile_pic_url"]
        processed_image = get_and_process_image(subject_image_url)
        self.image(name=processed_image, w=45, h=45)

    def __instagram_visualize_put_info_in_bullet_list(self, subject: dict):
        """
        Visualize information about a subject on Instagram \
        as items in a bullet list.
        """
        current_ordinate = self.get_y()
        self.set_xy(65, current_ordinate - 40)
        username = subject["username"]
        self.cell(
            w=0, h=6, txt=f"\u2022 Instagram nickname: {username}", ln=2,
            link=f"https://www.instagram.com/{username}/"
        )
        biography = subject["biography"]
        biography_processed = split_string_in_words_with_len_limit(biography)
        try:
            self.cell(
                w=0, h=6, txt=f"\u2022 Biography: {biography_processed}",
                ln=2
            )
        except UnicodeEncodeError:
            pass
        full_name = subject["full_name"]
        self.cell(w=0, h=6, txt=f"\u2022 Full name: {full_name}", ln=2)
        media_count = subject["media_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Media count: {media_count}", ln=2)
        number_of_followers = subject["follower_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Number of followers: {number_of_followers}", ln=2)
        number_of_following = subject["following_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Number of following: {number_of_following}", ln=2)
