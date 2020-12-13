# -*- coding: utf-8 -*-
"""The Twitter visualization module."""

import re
from fpdf import FPDF
from emoji import demojize
from app.backend.visualization.helpers.limit_string import split_string_in_words_with_len_limit
from app.backend.visualization.helpers.get_and_process_image import get_and_process_image


class TwitterVisualize(FPDF):
    """The class to visualize Twitter information on the PDF."""
    def __init__(self, analysis_response=None):
        super().__init__()
        self.analysis_response = analysis_response
        self.character_of_subjects = None
        self.tuples_with_info_and_posts = ()
        self.set_doc_option("core_fonts_encoding", "utf-8")

    def twitter_visualize(self):
        """
        Call other methods to visualize Twitter information if there is any.
        """
        dict_to_twitter_subjects = self.analysis_response["twitter"]
        (self.character_of_subjects, self.tuples_with_info_and_posts), \
            = dict_to_twitter_subjects.items()
        if self.tuples_with_info_and_posts:
            self.__twitter_visualize_write_title()
            self.__twitter_visualize_write_info_about_each_subject()

    def __twitter_visualize_write_title(self):
        """Write the title of Twitter on the PDF."""
        self.set_font("OpenSans", "BI", size=16)
        self.cell(w=0, h=5, txt="Twitter", ln=2)

    def __twitter_visualize_write_info_about_each_subject(self):
        """
        Visualize information about each found subject on Twitter.
        """
        if len(self.tuples_with_info_and_posts) > 1:
            self.set_font("OpenSans", "I", size=14)
            self.cell(w=0, h=5, txt="Potential users", ln=2)
        self.ln(5)
        self.set_font("OpenSans", size=14)
        for tuple_of_info_and_posts in self.tuples_with_info_and_posts:
            info_about_subject = tuple_of_info_and_posts[0]
            posts_of_subject = tuple_of_info_and_posts[1]
            self.__twitter_visualize_get_and_visualize_image(info_about_subject)
            self.__twitter_visualize_put_info_in_bullet_list(info_about_subject)
            self.__twitter_visualize_output_two_last_posts(posts_of_subject)
            self.ln(15)
        self.ln()
        self.line(
            self.get_x(), self.get_y() - 10, 210 - self.get_x(), self.get_y() - 10
        )
        self.set_font(family="OpenSans", style="", size=14)
        # """For TEST:""" self.cell(w=0, txt="HIII!!!")

    def __twitter_visualize_get_and_visualize_image(self, info: dict):
        """
        Get, process and visualize the Twitter profile image.
        """
        subject_image_url = info["profile_image_url_https"]
        processed_image = get_and_process_image(subject_image_url)
        self.image(name=processed_image, w=20, h=20)

    def __twitter_visualize_put_info_in_bullet_list(self, info: dict):
        """
        Visualize information about a subject on Twitter \
        as items in a bullet list.
        """
        self.set_font("OpenSans", size=14)
        current_ordinate = self.get_y()
        self.set_xy(35, current_ordinate - 20)
        screen_name = info["screen_name"]
        self.cell(
            w=0, h=6, txt=f"\u2022 Screen name: {screen_name}", ln=2,
            link=f"https://www.twitter.com/{screen_name}/"
        )
        description = info["description"]
        description_limited_in_len = split_string_in_words_with_len_limit(description, limit=45)
        de_emojified_description = demojize(description_limited_in_len)
        description_without_emoji_signs = re.sub(r":[a-zA-Z-_.]+:", "", de_emojified_description)
        if b"\\U" in description_without_emoji_signs.encode("unicode-escape"):
            self.cell(w=0, h=6, txt="\u2022 Description: ", ln=2)
        else:
            self.cell(
                w=0, h=6, txt=f"\u2022 Description: {description_without_emoji_signs}",
                ln=2
            )
        full_name = info["name"]
        de_emojified_full_name = demojize(full_name)
        full_name_without_emoji_signs = re.sub(r":[a-zA-Z-_.]+:", "", de_emojified_full_name)
        if b"\\U" in full_name_without_emoji_signs.encode("unicode-escape"):
            self.cell(w=0, h=6, txt="\u2022 Full name: ", ln=2)
        else:
            self.cell(w=0, h=6, txt=f"\u2022 Full name: {full_name_without_emoji_signs}", ln=2)
        location = info["location"]
        self.cell(w=0, h=6, txt=f"\u2022 Location: {location}", ln=2)
        number_of_followers = info["followers_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Number of followers: {number_of_followers}", ln=2)
        number_of_following = info["friends_count"]
        self.cell(w=0, h=6, txt=f"\u2022 Number of following: {number_of_following}", ln=2)
        external_url = info["url"] if info["url"] else "None"
        self.cell(
            w=0, h=6, txt=f"\u2022 External URL: {external_url}", ln=2,
            link=info["url"] if info["url"] else ""
        )

    def __twitter_visualize_output_two_last_posts(self, posts: list):
        """Visualize two last posts from the Twitter profile."""
        selected_posts = posts[0:2]
        self.cell(w=0, h=6, txt="\u2022 Two last posts:", ln=2)
        self.set_font("OpenSans", style="I", size=14)
        for post in selected_posts:
            post_limited_in_len = split_string_in_words_with_len_limit(post, limit=60)
            de_emojified_post = demojize(post_limited_in_len)
            post_without_emoji_signs = re.sub(r":[a-zA-Z-_.]+:", "", de_emojified_post)
            if b"\\U" in post_without_emoji_signs.encode("unicode-escape"):
                self.cell(w=0, h=6, txt="- ", ln=2)
                continue
            self.cell(w=0, h=6, txt=f"- {post_without_emoji_signs}", ln=2)
