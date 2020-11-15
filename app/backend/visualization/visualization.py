# -*- coding: utf-8 -*-
from app.backend.visualization._visualization_class import Visualization
from datetime import datetime


def caller_visualize(analysis_response, user_input, location):
    pdf = Visualization(analysis_response)
    pdf.add_page()
    _display_name_and_location(pdf, user_input)
    pdf.instagram_visualize()
    pdf.twitter_visualize()
    pdf.linkedin_visualize()
    pdf.facebook_visualize()
    pdf.google_search_visualize()
    str_of_output = _choose_name_of_file(user_input)
    pdf.output(f"{location}/{str_of_output}")


def _display_name_and_location(pdf_object, user_input):
    pdf_object.set_font("Times", "B", size=18)
    full_name = " ".join([user_input["first_name"], user_input["last_name"]])
    pdf_object.cell(w=0, h=6, txt=full_name, ln=2)
    pdf_object.set_font("Times", "I", size=18)
    pdf_object.cell(w=0, h=6, txt=user_input["location"], ln=2)


def _choose_name_of_file(user_input):
    full_name = "".join([user_input["first_name"], user_input["last_name"]])
    time_str_to_output = datetime.now().replace(microsecond=0).isoformat()
    file_name_to_output = "".join([full_name, time_str_to_output])
    return file_name_to_output
