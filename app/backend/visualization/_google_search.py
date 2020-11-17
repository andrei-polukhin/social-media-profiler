# -*- coding: utf-8 -*-
"""The Google Search visualization module."""

from fpdf import FPDF
from app.backend.visualization.helpers.limit_string import split_string_in_words_with_len_limit
from app.backend.visualization.helpers.get_and_process_image import get_and_process_image


class GoogleSearchVisualize(FPDF):
    """The class to visualize Google Search information on the PDF."""
    def __init__(self, analysis_response=None):
        super().__init__()
        self.analysis_response = analysis_response
        self.dict_of_results = {}
        self.set_doc_option("core_fonts_encoding", "windows-1252")

    def google_search_visualize(self):
        """
        Call other methods to visualize Google Search information if there is any.
        """
        self.dict_of_results = self.analysis_response["google_search"]
        if any(self.dict_of_results.values()):
            self._google_search_visualize_write_title()
            self._google_search_visualize_write_info_about_each_subject()

    def _google_search_visualize_write_title(self):
        """Write the title of Google Search on the PDF."""
        self.set_font("Times", "BI", size=16)
        self.cell(w=0, h=6, txt="Google Search", ln=2)

    def _google_search_visualize_write_info_about_each_subject(self):
        """
        Visualize information about found subjects from Google Search.
        """
        for service, service_info in self.dict_of_results.items():
            if service == "name" and service_info:
                self.set_font("Times", "BI", size=14)
                self.cell(w=0, h=6, txt="Information based on the full name", ln=2)
                self._google_search_visualize_write_subject_info(service_info)
            elif service != "name" and service_info:
                self.set_font("Times", "BI", size=14)
                self.cell(w=0, h=6, txt="Information based on extra input", ln=2)
                self._google_search_visualize_write_subject_info(service_info)
        current_abscissa = self.get_x()
        current_ordinate = self.get_y()
        self.line(
            current_abscissa, current_ordinate - 5, 210 - current_abscissa, current_ordinate - 5
        )
        # self.cell(w=0, h=6, txt="HII", ln=2)

    def _google_search_visualize_write_subject_info(self, list_of_subject_info: list):
        """Visualize information about a particular subject from a list of subjects' info."""
        for subject_info in list_of_subject_info:
            service_name = subject_info["service_name"]
            self._google_search_visualize_write_service_name(service_name)
            subject_info.pop("service_name", None)
            if subject_info.get("img_url") is not None:
                self._google_visualize_write_if_image(subject_info)
                self.ln()
            else:
                self._google_visualize_write_if_no_image(subject_info)
                self.ln()

    def _google_search_visualize_write_service_name(self, service_name: str):
        """Write service name from Google Search."""
        self.set_font("Times", "I", size=14)
        self.cell(w=0, h=6, txt=service_name, ln=2)

    def _google_visualize_write_if_image(self, subject_info: dict):
        """
        Visualize information about a particular subject if an image should be shown.
        """
        subject_img_url = subject_info["img_url"]
        processed_image = get_and_process_image(subject_img_url)
        self.image(name=processed_image, w=40, h=40)
        current_ordinate = self.get_y()
        self.set_xy(55, current_ordinate - 40)
        subject_info.pop("img_url", None)
        self._google_visualize_write_items_in_bullet_list(subject_info)

    def _google_visualize_write_if_no_image(self, subject_info):
        """
        Visualize information about a particular subject if no image should be shown.
        """
        self._google_visualize_write_items_in_bullet_list(subject_info)

    def _google_visualize_write_items_in_bullet_list(self, subject_info_filtered: dict):
        """
        Visualize information about a filtered subject from Google Search \
        as items in a bullet list.
        """
        self.set_font("Times", "", size=14)
        for description, value in subject_info_filtered.items():
            if description == "link":
                continue
            if isinstance(value, list):
                value = ", ".join(value)
            value_processed = split_string_in_words_with_len_limit(value, limit=60)
            if " name" in description:
                self.cell(
                    w=0, h=6, txt=f"\u2022 {description}{value_processed}.", ln=2,
                    link=subject_info_filtered["link"]
                )
                continue
            self.cell(w=0, h=6, txt=f"\u2022 {description}{value_processed}.", ln=2)


if __name__ == "__main__":
    google_search_response = {'google_search': {'github': [{'service_name': 'GitHub Profile', 'link': 'https://github.com/pythad', 'Full name: ': 'Vladyslav Ovchynnykov', 'Nickname: ': 'pythad', 'Popular repos: ': ['nider', 'selenium_extensions', 'parliament-scaper', 'pythad.github.io'], 'URLs of popular repos: ': ['https://github.com/pythad/nider', 'https://github.com/pythad/selenium_extensions', 'https://github.com/pythad/parliament-scaper', 'https://github.com/pythad/pythad.github.io'], 'img_url': 'https://avatars1.githubusercontent.com/u/10961029?s=460&u=3e6d98f79223f26c0478221863f85c906f27a3c0&v=4', 'Number of followers: ': '33', 'Number of following: ': '15', 'Location: ': 'Kyiv, Ukraine'}], 'name': [{'service_name': 'GitHub Profile', 'link': 'https://github.com/pythad', 'Full name: ': 'Vladyslav Ovchynnykov', 'Nickname: ': 'pythad', 'Popular repos: ': ['nider', 'selenium_extensions', 'parliament-scaper', 'pythad.github.io'], 'URLs of popular repos: ': ['https://github.com/pythad/nider', 'https://github.com/pythad/selenium_extensions', 'https://github.com/pythad/parliament-scaper', 'https://github.com/pythad/pythad.github.io'], 'img_url': 'https://avatars1.githubusercontent.com/u/10961029?s=460&u=3e6d98f79223f26c0478221863f85c906f27a3c0&v=4', 'Number of followers: ': '33', 'Number of following: ': '15', 'Location: ': 'Kyiv, Ukraine'}]}}
    pdf = GoogleSearchVisualize(google_search_response)
    pdf.add_page()
    pdf.google_search_visualize()
    pdf.output("class.pdf")
