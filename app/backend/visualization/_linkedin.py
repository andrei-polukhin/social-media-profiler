# -*- coding: utf-8 -*-
"""The LinkedIn visualization module."""

from fpdf import FPDF


class LinkedinVisualize(FPDF):
    """The class to visualize LinkedIn information on the PDF."""
    def __init__(self, analysis_response=None):
        super().__init__()
        self.analysis_response = analysis_response
        self.character_of_subjects = None
        self.lists_of_info = []
        self.set_doc_option("core_fonts_encoding", "windows-1252")

    def linkedin_visualize(self):
        """
        Call other methods to visualize LinkedIn information if there is any.
        """
        dict_to_linkedin_subjects = self.analysis_response["linkedin"]
        (self.character_of_subjects, self.lists_of_info), = dict_to_linkedin_subjects.items()
        if self.lists_of_info:
            self.__linkedin_visualize_write_title()
            self.__linkedin_visualize_write_info_about_each_subject()

    def __linkedin_visualize_write_title(self):
        """Write the title of LinkedIn on the PDF."""
        self.set_font("Times", "BI", size=16)
        self.cell(w=0, h=6, txt="LinkedIn", ln=2)

    def __linkedin_visualize_write_info_about_each_subject(self):
        """
        Visualize information about each found subject on LinkedIn.
        """
        self.set_font("Times", "I", size=14)
        if self.character_of_subjects == "potential_subjects_after_filtering":
            self.cell(w=0, h=6, txt="Potential user(s)", ln=2)
        self.ln(5)
        for subject in self.lists_of_info:
            self.__linkedin_visualize_write_name_of_subject(subject)
            self.__linkedin_visualize_write_other_info(subject)
            self.ln(15)
        self.ln()
        current_abscissa = self.get_x()
        current_ordinate = self.get_y()
        self.line(
            current_abscissa, current_ordinate - 10, 210 - current_abscissa, current_ordinate - 10
        )
        # """For TEST:""" self.cell(w=0, txt="HIII!!!")

    def __linkedin_visualize_write_name_of_subject(self, subject_as_dict: dict):
        """Write the full name of the found subject on LinkedIn."""
        self.set_font("Times", "B", size=14)
        first_name = subject_as_dict["firstName"]
        last_name = subject_as_dict["lastName"]
        full_name = " ".join([first_name, last_name])
        self.cell(w=0, h=6, txt=full_name, ln=2)

    def __linkedin_visualize_write_other_info(self, subject_as_dict: dict):
        """Write other analyzed information about a subject."""
        self.set_font("Times", size=14)
        headline = subject_as_dict["headline"]
        self.cell(w=0, h=6, txt=f"Headline: {headline}.", ln=2)
        industry = subject_as_dict["industryName"]
        self.cell(w=0, h=6, txt=f"Industry: {industry}.", ln=2)
        location = subject_as_dict["locationName"]
        self.cell(w=0, h=6, txt=f"Location: {location}.", ln=2)
        self.__linkedin_visualize_write_experience(subject_as_dict)
        self.__linkedin_visualize_write_education(subject_as_dict)
        self.__linkedin_visualize_write_skills(subject_as_dict)

    def __linkedin_visualize_write_experience(self, subject_as_dict: dict):
        """Write the work experience of the found subject."""
        self.cell(w=0, h=6, txt="Work experience:", ln=2)
        list_of_experiences = subject_as_dict["experience"]
        self.set_x(20)
        for experience in list_of_experiences:
            self.set_font("Times", "I", size=14)
            company_name = experience["companyName"]
            self.cell(w=0, h=6, txt=f"\u2022 {company_name}", ln=2)
            self.set_font("Times", size=14)
            job_title = experience["title"]
            self.cell(w=0, h=6, txt=f"Job title: {job_title}.", ln=2)
            company_location = experience.get("locationName")
            if company_location is not None:
                self.cell(w=0, h=6, txt=f"Company location: {company_location}.", ln=2)
            time_period = experience["timePeriod"]
            self.__linkedin_visualize_write_time_period_for_experience(time_period)
        self.ln()

    def __linkedin_visualize_write_time_period_for_experience(self, time_period: dict):
        """
        Write time period (start date and end date, if any) for a particular work experience.
        """
        start_date = time_period["startDate"]
        end_date = time_period.get("endDate")
        if end_date is None:
            end_date_str = "Now"
        else:
            end_date_values = [str(element) for element in end_date.values()]
            end_date_values[0] = end_date_values[0] \
                if len(end_date_values[0]) == 2 \
                else "0" + end_date_values[0]
            end_date_str = "/".join(end_date_values)
        start_date_values = [str(element) for element in start_date.values()]
        start_date_values[0] = start_date_values[0] \
            if len(start_date_values[0]) == 2 \
            else "0" + start_date_values[0]
        start_date_str = "/".join(start_date_values)
        date_period_str_to_output = " - ".join([start_date_str, end_date_str])
        self.cell(w=0, h=6, txt=f"Time period: {date_period_str_to_output}.", ln=2)

    def __linkedin_visualize_write_education(self, subject_as_dict: dict):
        """Write the education of the found subject."""
        self.cell(w=0, h=6, txt="Education:", ln=2)
        list_of_educations = subject_as_dict["education"]
        self.set_x(20)
        for education in list_of_educations:
            self.set_font("Times", "I", size=14)
            degree_name = education.get("degreeName")
            if degree_name is not None:
                self.cell(w=0, h=6, txt=f"\u2022 {degree_name}", ln=2)
            self.set_font("Times", size=14)
            school_name = education["schoolName"]
            self.cell(w=0, h=6, txt=f"School name: {school_name}.", ln=2)
            time_period = education.get("timePeriod")
            if time_period is not None:
                self.__linkedin_visualize_write_time_period_for_education(time_period)
        self.ln()

    def __linkedin_visualize_write_time_period_for_education(self, time_period: dict):
        """
        Write time period (start date and end date, if any) for a particular education.
        """
        start_date = time_period["startDate"]
        end_date = time_period.get("endDate")
        if end_date is None:
            date_period_str_to_output = start_date["year"]
        else:
            end_date_str_to_output = end_date["year"]
            start_date_str_to_output = start_date["year"]
            date_period_str_to_output = f"{start_date_str_to_output}-{end_date_str_to_output}"
        self.cell(w=0, h=6, txt=f"Time period: {date_period_str_to_output}.", ln=2)

    def __linkedin_visualize_write_skills(self, subject_as_dict: dict):
        """Visualize all skills from the LinkedIn profile of the found subject."""
        if subject_as_dict["skills"]:
            list_of_skills_to_output = []
            skills = subject_as_dict["skills"]
            for skill_as_dict in skills:
                name_of_skill = skill_as_dict["name"]
                list_of_skills_to_output.append(name_of_skill)
            skills_output_str = ", ".join(list_of_skills_to_output)
            self.multi_cell(w=0, h=6, txt=f"Skills: {skills_output_str}.", ln=2)


if __name__ == "__main__":
    linkedin_dict = {'linkedin': {'potential_subjects_after_filtering': [{'certifications': [], 'education': [{'degreeName': 'Delta Module 2', 'schoolName': 'University of Cambridge', 'timePeriod': {'startDate': {'year': 2018}}}, {'degreeName': 'Cambridge CELTA', 'schoolName': 'University of Cambridge', 'timePeriod': {'startDate': {'year': 2013}}}, {'degreeName': 'B.A.', 'fieldOfStudy': 'Film, Screenwriting', 'schoolName': 'University of Michigan', 'timePeriod': {'endDate': {'year': 2009}, 'startDate': {'year': 2007}}}], 'experience': [{'company': {'employeeCountRange': {'end': 50, 'start': 11}, 'industries': ['Education Management']}, 'companyName': 'The London School of English', 'locationName': 'Kyiv, Kyiv City, Ukraine', 'timePeriod': {'startDate': {'month': 8, 'year': 2020}}, 'title': 'Director Of Studies'}, {'companyName': 'Freelance', 'timePeriod': {'startDate': {'month': 1, 'year': 2015}}, 'title': 'Writer'}, {'company': {'employeeCountRange': {'end': 50, 'start': 11}, 'industries': ['Education Management']}, 'companyName': 'The London School of English', 'locationName': 'Kiev Region, Ukraine', 'timePeriod': {'endDate': {'month': 8, 'year': 2020}, 'startDate': {'month': 8, 'year': 2019}}, 'title': 'Senior Teacher'}, {'companyName': 'English Playschool Moscow', 'locationName': 'Moscow, Russian Federation', 'timePeriod': {'endDate': {'month': 7, 'year': 2019}, 'startDate': {'month': 9, 'year': 2018}}, 'title': 'English Teacher for Very Young Learners'}, {'companyName': 'American Councils', 'locationName': 'Tbilisi, Georgia', 'timePeriod': {'endDate': {'month': 5, 'year': 2018}, 'startDate': {'month': 1, 'year': 2018}}, 'title': 'English Teacher'}], 'firstName': 'Amy', 'geoCountryName': 'Ukraine', 'headline': 'Director Of Studies at The London School of English', 'honors': [], 'industryName': 'Professional Training', 'languages': [], 'lastName': 'Butler', 'locationName': 'Ukraine', 'publications': [], 'skills': [{'name': 'Social Media'}, {'name': 'Editing'}, {'name': 'Microsoft Office'}, {'name': 'Microsoft Excel'}, {'name': 'PowerPoint'}, {'name': 'Social Networking'}, {'name': 'Microsoft Word'}, {'name': 'Copy Editing'}, {'name': 'Outlook'}, {'name': 'Creative Writing'}, {'name': 'CELTA'}, {'name': 'Marketing Communications'}, {'name': 'Research'}, {'name': 'Marketing'}, {'name': 'Teaching'}, {'name': 'Social Media Marketing'}, {'name': 'Blogging'}, {'name': 'Public Speaking'}, {'name': 'Writing'}], 'student': False}]}}
    pdf = LinkedinVisualize(linkedin_dict)
    pdf.add_page()
    pdf.linkedin_visualize()
    pdf.output("class.pdf")
