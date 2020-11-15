# -*- coding: utf-8 -*-
from fpdf import FPDF
from app.backend.visualization.helpers.split_string import split_string_in_words_with_len_limit
from app.backend.visualization.helpers.get_and_process_image import get_and_process_image


class TwitterVisualize(FPDF):
    def __init__(self, analysis_response=None):
        super().__init__()
        self.analysis_response = analysis_response
        self.character_of_subjects = None
        self.tuples_with_info_and_posts = ()
        self.set_doc_option("core_fonts_encoding", "windows-1252")

    def twitter_visualize(self):
        dict_to_twitter_subjects = self.analysis_response["twitter"]
        (self.character_of_subjects, self.tuples_with_info_and_posts), = dict_to_twitter_subjects.items()
        if self.tuples_with_info_and_posts:
            self._twitter_visualize_write_title()
            self._twitter_visualize_write_info_about_each_subject()

    def _twitter_visualize_write_title(self):
        self.set_font("Times", "BI", size=16)
        self.cell(w=0, h=5, txt="Twitter", ln=2)

    def _twitter_visualize_write_info_about_each_subject(self):
        self.set_font("Times", "I", size=14)
        if len(self.tuples_with_info_and_posts) > 1:
            self.cell(w=0, h=5, txt="Potential users", ln=2)
        self.ln(5)
        self.set_font("Times", size=14)
        for tuple_of_info_and_posts in self.tuples_with_info_and_posts:
            info_about_subject = tuple_of_info_and_posts[0]
            posts_of_subject = tuple_of_info_and_posts[1]
            self._twitter_visualize_get_and_visualize_image(info_about_subject)
            self._twitter_visualize_put_info_in_bullet_list(info_about_subject)
            self._twitter_visualize_output_two_last_posts(posts_of_subject)
            self.ln(15)
        self.ln()
        current_abscissa = self.get_x()
        current_ordinate = self.get_y()
        self.line(
            current_abscissa, current_ordinate - 10, 210 - current_abscissa, current_ordinate - 10
        )
        self.set_font(family="Times", style="", size=14)
        # """For TEST:""" self.cell(w=0, txt="HIII!!!")

    def _twitter_visualize_get_and_visualize_image(self, info):
        subject_image_url = info["profile_image_url_https"]
        processed_image = get_and_process_image(subject_image_url)
        self.image(name=processed_image, w=20, h=20)

    def _twitter_visualize_put_info_in_bullet_list(self, info):
        current_ordinate = self.get_y()
        self.set_xy(35, current_ordinate - 20)
        screen_name = info["screen_name"]
        self.cell(
            w=0, h=6, txt=f"\u2022 Screen name: {screen_name}", ln=2,
            link=f"https://www.twitter.com/{screen_name}/"
        )
        description = info["description"]
        description_processed = split_string_in_words_with_len_limit(description, limit=60)
        self.cell(
            w=0, h=6, txt=u"\u2022 Description: {}".format(description_processed),
            ln=2
        )
        full_name = info["name"]
        self.cell(w=0, h=6, txt=f"\u2022 Full name: {full_name}", ln=2)
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

    def _twitter_visualize_output_two_last_posts(self, posts):
        selected_posts = posts[0:2]
        self.cell(w=0, h=6, txt=u"\u2022 Two last posts:", ln=2)
        self.set_font("Times", style="I", size=14)
        for post in selected_posts:
            processed_post = split_string_in_words_with_len_limit(post, limit=75)
            self.cell(w=0, h=6, txt=f"- {processed_post}", ln=2)


if __name__ == "__main__":
    twitter_response = {'twitter': {'potential_subjects': [({'description': 'Long-term expat, CELTA/Delta qualified English teacher, freelance writer. Insta: wayfarersbook', 'followers_count': 699, 'friends_count': 680, 'location': 'Kyiv, Ukraine', 'name': 'Amy Butler', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1018140475222523904/ADqhB2yj_normal.jpg', 'screen_name': 'WayfarersBook', 'url': 'https://t.co/7fIVtM8Ne0'}, ['@CailinONeil @VickyFlipFlop @instagram Mine is basically cake, donuts, pasta, and the odd glamour fashion photo. ', "@RoamingRequired Lucky. We've got all sorts of rules because everyone's really paranoid about voter fraud.", "@quickdarshan Embarrassingly, I've never tried before. (Me of little faith in my one vote.) My bf managed to vote i… ", '@RoamingRequired Can you vote by mail? We need to get there. Or online, like Estonia, country of the freaking future.', "@quickdarshan I know it's rigged, it still makes me really mad. Also seeing the clips of governors not being concer… ", 'These lines to vote are insane. We need to start rethinking our voting procedures now. ', "@thethoughtcard I live in Kyiv -- it's a crazy affordable European destination. I've traveled a lot around Ukraine… ", 'RT @inclpablo: me after guessing the password of my own email ', "Man, it's really a shame the cops can't do anything about all those looters. Definitely seems like they're trying.… ", "How do you just walk by an old man bleeding on the ground?!\nDon't turn on the sound unless you want to be ill. ", 'RT @JordanUhl: Who does this protect? ', 'RT @joshfoxfilm: People stuck in traffic are witnessing NYPD beat up folks on their way home. ', "I don't know whether or not this was actually before curfew, but why would you escalate with this tiny group of pea… ", '@gaelemorag Thanks for reading. While the title is provocative, the content itself is more geared towards getting p… ', 'Looking for links to legit places to donate to looted/vandalized #NYC businesses. This article is a good starting p… ', "@RoamingRequired @sunriseon7 Yes, it's embarrassing how we're treating international press. We even got publicly called out by Russia...", 'Your daily reminder that police are abusing and arresting cooperative reporters and journalists. Maybe if they did… ', '@travchats A lot of people are hating on listicles, but if it comes from someone who has done the research, they ca… ', 'This is a super resource for people who are looking to get informed but are also a bit overwhelmed with information… ', 'In case anyone is wondering who is inciting violence, this FBI thread has devastating examples of #PoliceBrutality. '])]}}
    pdf = TwitterVisualize(twitter_response)
    pdf.add_page()
    pdf.twitter_visualize()
    pdf.output("class.pdf")
