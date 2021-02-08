# -*- coding: utf-8 -*-
"""The Instagram visualization module."""

import re
import textwrap
from fpdf import FPDF
from emoji import demojize
from app.backend.visualization.helpers.get_and_process_image import get_and_process_image


class InstagramVisualize(FPDF):
    """The class to visualize Instagram information on the PDF."""
    def __init__(self, analysis_response=None):
        super().__init__()
        self.analysis_response = analysis_response
        self.dict_of_instagram_subjects = {}
        self.set_doc_option("core_fonts_encoding", "utf-8")

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
        self.set_font("OpenSans", "BI", size=16)
        self.cell(w=0, h=5, txt="Instagram", ln=2)

    def __instagram_visualize_write_info_about_each_subject(self):
        """
        Visualize information about each subject on Instagram.
        """
        self.set_font("OpenSans", "I", size=14)
        if self.dict_of_instagram_subjects.get("potential_subjects") is not None:
            self.cell(w=0, h=5, txt="Potential users", ln=2)
        self.ln(5)
        self.set_font("OpenSans", size=14)
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
        biography_limited_in_len = textwrap.shorten(biography, 40, placeholder="...")
        biography_de_emojified = demojize(biography_limited_in_len)
        biography_without_emoji_signs = re.sub(r":[a-zA-Z-_.]+:", "", biography_de_emojified)
        if b"\\U" in biography_without_emoji_signs.encode("unicode-escape"):
            self.cell(w=0, h=6, txt="\u2022 Biography: ", ln=2)
        else:
            self.cell(
                w=0, h=6, txt=f"\u2022 Biography: {biography_without_emoji_signs}",
                ln=2
            )
        full_name = subject["full_name"]
        full_name_deemojified = demojize(full_name)
        full_name_without_emoji_signs = re.sub(r":[a-zA-Z-_.]+:", "", full_name_deemojified)
        if b"\\U" in full_name_without_emoji_signs.encode("unicode-escape"):
            self.cell(w=0, h=6, txt="\u2022 Full name: ", ln=2)
        else:
            self.cell(w=0, h=6, txt=f"\u2022 Full name: {full_name_without_emoji_signs}", ln=2)
        media_count = subject["media_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Media count: {media_count}", ln=2)
        number_of_followers = subject["follower_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Number of followers: {number_of_followers}", ln=2)
        number_of_following = subject["following_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Number of following: {number_of_following}", ln=2)
