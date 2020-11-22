# -*- coding: utf-8 -*-
"""The Facebook visualization module."""

from fpdf import FPDF


class FacebookVisualize(FPDF):
    """The class to visualize Facebook information on the PDF."""
    def __init__(self, analysis_response=None):
        super().__init__()
        self.analysis_response = analysis_response
        self.list_of_facebook_subjects = []

    def facebook_visualize(self):
        """Call other methods to visualize Facebook information if there is any."""
        self.list_of_facebook_subjects = self.analysis_response["facebook"]
        if self.list_of_facebook_subjects:
            self.__facebook_visualize_write_title_of_facebook()
            self.__facebook_visualize_write_info_about_each_subject()

    def __facebook_visualize_write_title_of_facebook(self):
        """Write the title of Facebook on the PDF."""
        self.set_font("Times", "BI", size=16)
        self.cell(w=0, h=6, txt="Facebook", ln=2)

    def __facebook_visualize_write_info_about_each_subject(self):
        """
        Visualize information about found subjects on Facebook \
        as items in a bullet list.
        """
        if len(self.list_of_facebook_subjects) > 1:
            self.set_font("Times", "I", size=14)
            self.cell(w=0, h=6, txt="Potential users", ln=2)
        self.ln(5)
        for subject in self.list_of_facebook_subjects:
            self.__facebook_visualize_write_name_of_service(subject)
            subject.pop("service_name", None)
            self.set_font("Times", size=14)
            self.set_x(20)
            for description, value in subject.items():
                if description == "link":
                    continue
                if " name" in description:
                    self.cell(
                        w=0, h=6, txt=f"{description}{value}", ln=2, link=subject["link"]
                    )
                    continue
                self.cell(w=0, h=6, txt=f"{description}{value}", ln=2)
            self.ln()

    def __facebook_visualize_write_name_of_service(self, subject: dict):
        """
        Write service name inside Facebook, i.e. `Facebook profile`, `Facebook group` \
        and so on.
        """
        self.set_font("Times", "B", size=14)
        service_name = subject["service_name"]
        self.cell(w=0, h=6, txt=service_name, ln=2)


if __name__ == "__main__":
    facebook_dict = {'facebook': [{'Profile name: ': 'Amy Butler',
                                   'link': 'https://www.facebook.com/amy.butler.7186/',
                                   'service_name': 'Facebook Profile'},
                                  {'Profile name: ': 'Amy Butler',
                                   'link': 'https://www.facebook.com/amy.butler.5686322/',
                                   'service_name': 'Facebook Profile'}]}
    pdf = FacebookVisualize(facebook_dict)
    pdf.add_page()
    pdf.facebook_visualize()
    pdf.output("class.pdf")
