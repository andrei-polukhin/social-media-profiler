# -*- coding: utf-8 -*-
from datetime import datetime
from app.backend.visualization._visualization_class import Visualization


def main_visualization(analysis_response, user_input, pdf_output_location):
    pdf = Visualization(analysis_response)
    pdf.add_page()
    _display_name_and_location(pdf, user_input)
    pdf.instagram_visualize()
    pdf.twitter_visualize()
    pdf.linkedin_visualize()
    pdf.facebook_visualize()
    pdf.google_search_visualize()
    str_of_output = _choose_name_of_file(user_input)
    pdf.output(f"{pdf_output_location}/{str_of_output}")


def _display_name_and_location(pdf_object, user_input):
    pdf_object.set_font("Times", "B", size=18)
    full_name = " ".join([user_input["first_name"], user_input["last_name"]])
    pdf_object.cell(w=0, h=6, txt=full_name, ln=2)
    pdf_object.set_font("Times", "I", size=18)
    pdf_object.cell(w=0, h=6, txt=user_input["location"], ln=2)
    pdf_object.ln(10)


def _choose_name_of_file(user_input):
    full_name = "".join([user_input["first_name"], user_input["last_name"]])
    time_str_to_output = datetime.now().replace(microsecond=0).isoformat()
    file_name_to_output = "_".join([full_name, time_str_to_output])
    return file_name_to_output


if __name__ == "__main__":
    to_visualize = {'facebook': [], 'instagram': {'potential_subjects': []}, 'linkedin': {'potential_subjects_after_filtering': [{'industryName': 'Professional Training', 'lastName': 'Butler', 'locationName': 'Ukraine', 'student': False, 'geoCountryName': 'Ukraine', 'firstName': 'Amy', 'headline': 'Director Of Studies at The London School of English', 'experience': [{'locationName': 'Kyiv, Kyiv City, Ukraine', 'companyName': 'The London School of English', 'timePeriod': {'startDate': {'month': 8, 'year': 2020}}, 'company': {'employeeCountRange': {'start': 11, 'end': 50}, 'industries': ['Education Management']}, 'title': 'Director Of Studies'}, {'companyName': 'Freelance', 'timePeriod': {'startDate': {'month': 1, 'year': 2015}}, 'title': 'Writer'}, {'locationName': 'Kiev Region, Ukraine', 'companyName': 'The London School of English', 'timePeriod': {'endDate': {'month': 8, 'year': 2020}, 'startDate': {'month': 8, 'year': 2019}}, 'company': {'employeeCountRange': {'start': 11, 'end': 50}, 'industries': ['Education Management']}, 'title': 'Senior Teacher'}, {'locationName': 'Moscow, Russian Federation', 'companyName': 'English Playschool Moscow', 'timePeriod': {'endDate': {'month': 7, 'year': 2019}, 'startDate': {'month': 9, 'year': 2018}}, 'title': 'English Teacher for Very Young Learners'}, {'locationName': 'Tbilisi, Georgia', 'companyName': 'American Councils', 'timePeriod': {'endDate': {'month': 5, 'year': 2018}, 'startDate': {'month': 1, 'year': 2018}}, 'title': 'English Teacher'}], 'skills': [{'name': 'Social Media'}, {'name': 'Editing'}, {'name': 'Microsoft Office'}, {'name': 'Microsoft Excel'}, {'name': 'PowerPoint'}, {'name': 'Social Networking'}, {'name': 'Microsoft Word'}, {'name': 'Copy Editing'}, {'name': 'Outlook'}, {'name': 'Creative Writing'}, {'name': 'CELTA'}, {'name': 'Marketing Communications'}, {'name': 'Research'}, {'name': 'Marketing'}, {'name': 'Teaching'}, {'name': 'Social Media Marketing'}, {'name': 'Blogging'}, {'name': 'Public Speaking'}, {'name': 'Writing'}], 'education': [{'timePeriod': {'startDate': {'year': 2018}}, 'degreeName': 'Delta Module 2', 'schoolName': 'University of Cambridge'}, {'timePeriod': {'startDate': {'year': 2013}}, 'degreeName': 'Cambridge CELTA', 'schoolName': 'University of Cambridge'}, {'timePeriod': {'endDate': {'year': 2009}, 'startDate': {'year': 2007}}, 'degreeName': 'B.A.', 'schoolName': 'University of Michigan', 'fieldOfStudy': 'Film, Screenwriting'}], 'languages': [], 'publications': [], 'certifications': [], 'honors': []}]}, 'twitter': {'found_subjects': [({'name': 'Amy Butler', 'screen_name': 'WayfarersBook', 'location': 'Kyiv, Ukraine', 'description': 'Long-term expat, CELTA/Delta qualified English teacher, freelance writer. Insta: wayfarersbook', 'url': 'https://t.co/7fIVtM8Ne0', 'followers_count': 697, 'friends_count': 680, 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1018140475222523904/ADqhB2yj_normal.jpg'}, ['@CailinONeil @VickyFlipFlop @instagram Mine is basically cake, donuts, pasta, and the odd glamour fashion photo. ', "@RoamingRequired Lucky. We've got all sorts of rules because everyone's really paranoid about voter fraud.", "@quickdarshan Embarrassingly, I've never tried before. (Me of little faith in my one vote.) My bf managed to vote i… ", '@RoamingRequired Can you vote by mail? We need to get there. Or online, like Estonia, country of the freaking future.', "@quickdarshan I know it's rigged, it still makes me really mad. Also seeing the clips of governors not being concer… ", 'These lines to vote are insane. We need to start rethinking our voting procedures now. ', "@thethoughtcard I live in Kyiv -- it's a crazy affordable European destination. I've traveled a lot around Ukraine… ", 'RT @inclpablo: me after guessing the password of my own email ', "Man, it's really a shame the cops can't do anything about all those looters. Definitely seems like they're trying.… ", "How do you just walk by an old man bleeding on the ground?!\nDon't turn on the sound unless you want to be ill. ", 'RT @JordanUhl: Who does this protect? ', 'RT @joshfoxfilm: People stuck in traffic are witnessing NYPD beat up folks on their way home. ', "I don't know whether or not this was actually before curfew, but why would you escalate with this tiny group of pea… ", '@gaelemorag Thanks for reading. While the title is provocative, the content itself is more geared towards getting p… ', 'Looking for links to legit places to donate to looted/vandalized #NYC businesses. This article is a good starting p… ', "@RoamingRequired @sunriseon7 Yes, it's embarrassing how we're treating international press. We even got publicly called out by Russia...", 'Your daily reminder that police are abusing and arresting cooperative reporters and journalists. Maybe if they did… ', '@travchats A lot of people are hating on listicles, but if it comes from someone who has done the research, they ca… ', 'This is a super resource for people who are looking to get informed but are also a bit overwhelmed with information… ', 'In case anyone is wondering who is inciting violence, this FBI thread has devastating examples of #PoliceBrutality. '])]}, 'google_search': {'name': []}}
    sample_input = taken_input = {
        "first_name": "Amy",
        "last_name": "Butler",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "Cambridge University",
        "twitter_profile": "WayfarersBook",
        "instagram_nickname": "Wayfarersbook",
        "location": "Ukraine",
        "additional_text": "CELTA/Delta qualified teacher",
    }
    main_visualization(to_visualize, sample_input, "/home/andrew")
