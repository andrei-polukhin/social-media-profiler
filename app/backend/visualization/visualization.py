# -*- coding: utf-8 -*-
"""The main visualization module."""

from datetime import datetime
from app.backend.visualization._visualization_class import Visualization


def main_visualization(analysis_response: dict, user_input: dict, pdf_output_location: str) -> None:
    """
    Call Visualization class and visualize information from all social media networks, \
    then output a PDF file that contains current time and full name of the desired subject \
    in the name.

    Args:
        `analysis_response`: the dictionary received after an analysis of the scraped information.\n
        `user_input`: the app's user input represented as a dict.\n
        `pdf_output_location`: the location on the PC where to output the PDF file.
    Returns:
        `None`: outputs a PDF file with all the information into a specific location.
    """
    pdf = Visualization(analysis_response)
    pdf.add_page()
    _display_name_and_location(pdf, user_input)
    pdf.instagram_visualize()
    pdf.twitter_visualize()
    pdf.linkedin_visualize()
    pdf.google_search_visualize()
    str_of_output = _choose_name_of_file(user_input)
    pdf.output(f"{pdf_output_location}/{str_of_output}", "F")


def _display_name_and_location(pdf_object, user_input: dict):
    """
    Display the desired subject full name and location on the PDF.

    Args:
         `pdf_object`: the FPDF object to visualize full name and location.\n
         `user_input`: the app's user input represented as a dict.
    """
    pdf_object.set_font("OpenSans", "B", size=18)
    full_name = " ".join([user_input["first_name"], user_input["last_name"]])
    pdf_object.cell(w=0, h=6, txt=full_name, ln=2)
    pdf_object.set_font("OpenSans", "I", size=18)
    pdf_object.cell(w=0, h=6, txt=user_input["location"], ln=2)
    pdf_object.ln(10)


def _choose_name_of_file(user_input: dict) -> str:
    """
    Based on the full name of the desired subject and current date, \
    return the name of the PDF file.

    Args:
         `user_input`: the app's user input represented as a dict.
    Returns:
        `str`: the name of the PDF file which will be saved in the user-specified directory.
    """
    full_name = "".join([user_input["first_name"], user_input["last_name"]])
    time_str_to_output = datetime.now().replace(microsecond=0).isoformat()
    file_name_to_output = "_".join([full_name, time_str_to_output])
    return file_name_to_output
