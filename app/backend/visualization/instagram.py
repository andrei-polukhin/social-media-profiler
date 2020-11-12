# -*- coding: utf-8 -*-
from fpdf import FPDF
import io
from urllib.request import urlopen
from PIL import Image, ImageDraw
import numpy as np


class InstagramVisualize(FPDF):
    def __init__(self, analysis_response):
        super().__init__()
        self.list_of_instagram_subjects = analysis_response["instagram"]
        self.set_doc_option("core_fonts_encoding", "windows-1252")

    def instagram_visualize(self):
        if self.list_of_instagram_subjects:
            self._write_title_of_instagram()
            self._write_information_about_each_subject()

    def _write_title_of_instagram(self):
        self.set_font("Times", "BI", size=16)
        self.cell(w=0, h=10, txt="Instagram", ln=2)

    def _write_information_about_each_subject(self):
        self.set_font("Times", size=14)
        for subject in self.list_of_instagram_subjects:
            self._process_and_visualize_image(subject)
            self._put_all_subject_info_in_bullet_list(subject)
            self.ln(15)
        self.ln()
        self.line(self.get_x(), self.get_y()-10, 210 - self.get_x(), self.get_y()-10)
        # """For TEST:""" self.cell(w=0, txt="HIII!!!")

    def _process_and_visualize_image(self, subject):
        subject_image_url = subject["profile_pic_url"]
        processed_image = self._get_and_process_instagram_image(subject_image_url)
        self.image(name=processed_image, w=45, h=45)

    def _put_all_subject_info_in_bullet_list(self, subject):
        current_ordinate = self.get_y()
        self.set_xy(65, current_ordinate-40)
        username = subject["username"]
        self.cell(
            w=0, h=6, txt=f"\u2022 Instagram nickname: {username}", ln=2,
            link=f"https://www.instagram.com/{username}/"
        )
        biography = subject["biography"]
        biography_processed = self._split_string_in_words_with_len_limit(biography)
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

    @staticmethod
    def _get_and_process_instagram_image(url):
        img = io.BytesIO(urlopen(url).read())
        pillow_img = Image.open(img).convert("RGB")
        np_image = np.array(pillow_img)

        h, w = pillow_img.size
        # Create same size alpha layer with circle
        alpha = Image.new("L", pillow_img.size, 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0, 0, h, w], 0, 360, fill=255)

        # Convert alpha Image to numpy array
        np_alpha = np.array(alpha)

        # Add alpha layer to RGB
        np_image = np.dstack((np_image, np_alpha))

        # Save with alpha
        cropped_image_in_bytes = io.BytesIO()
        cropped_image = Image.fromarray(np_image)
        cropped_image.save(cropped_image_in_bytes, "PNG")
        cropped_image_in_bytes.seek(0)
        cropped_image = cropped_image_in_bytes.read()

        # Non test code
        data_bytes_io = io.BytesIO(cropped_image)
        return data_bytes_io

    @staticmethod
    def _split_string_in_words_with_len_limit(string: str, limit=45):
        accumulated_words = []
        list_of_words_in_string = string.split()
        for word in list_of_words_in_string:
            string_from_current_list = " ".join(accumulated_words)
            if len(string_from_current_list) + len(word) + 1 <= limit:
                accumulated_words.append(word)
                continue
            accumulated_words[-1] += "..."
            break
        return " ".join(accumulated_words)


if __name__ == "__main__":
    instagram_dict = {'instagram': [{'biography': "The Wayfarer's Bookshop est. 1996 specializes in rare exploration, travel and voyage related items", 'follower_count': 56, 'following_count': 10, 'full_name': 'Eric Peter Waschke', 'media_count': 0, 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/69569940_450144195583218_4396135465405644800_n.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=dQA0tdaNQr8AX-J5d3N&oh=55edb598eb2014804c32c10a5d96faaa&oe=5FC8203B', 'username': 'wayfarersbookshop', 'whatsapp_number': ''}, {'biography': '21. Edinburgh bookseller. Wayfarer. Professionally quirky and curious. She/her or They/Them. Hufflepuff.', 'follower_count': 157, 'following_count': 331, 'full_name': 'Niall', 'media_count': 54, 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/18513669_1390552421001286_650901666643574784_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=d7t2KwrpFG0AX_powxk&oh=f6e1bb5c3338bcc1da9711eb1fe08a48&oe=5FC7DB97', 'username': 'wayfarersbooks', 'whatsapp_number': ''}, {'biography': '21. Edinburgh bookseller. Wayfarer. Professionally quirky and curious. She/her or They/Them. Hufflepuff.', 'follower_count': 157, 'following_count': 331, 'full_name': 'Niall', 'media_count': 54, 'profile_pic_url': 'https://instagram.fiev25-2.fna.fbcdn.net/v/t51.2885-19/s150x150/18513669_1390552421001286_650901666643574784_a.jpg?_nc_ht=instagram.fiev25-2.fna.fbcdn.net&_nc_ohc=d7t2KwrpFG0AX_powxk&oh=f6e1bb5c3338bcc1da9711eb1fe08a48&oe=5FC7DB97', 'username': 'wayfarersbooks', 'whatsapp_number': ''}]}
    pdf = InstagramVisualize(instagram_dict)
    pdf.add_page()
    pdf.instagram_visualize()
    pdf.output("class.pdf")
