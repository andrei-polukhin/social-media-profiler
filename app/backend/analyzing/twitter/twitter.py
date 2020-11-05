# -*- coding: utf-8 -*-
from app.backend.analyzing.twitter._twitter_class import TwitterAnalyze


def caller_analyze_twitter(scraping_response, user_input):
    results_to_visualize = {}
    twitter_obj = TwitterAnalyze(scraping_response, user_input)
    twitter_obj.twitter_analyze()
    results_to_visualize["twitter"] = twitter_obj.tuples_after_description_filter
    return results_to_visualize


if __name__ == "__main__":
    taken_input = {
        "first_name": "Amy",
        "last_name": "Butler",
        "company": "LSE",
        "job_title": "Director of Studies",
        "school": "MIT University",
        "twitter_profile": "abumetsov",
        "instagram_profile": "Wayfarersbook",
        "location": "Ukraine",
        "additional_text": "CELTA/Delta teacher"
    }
    twitter_api_response = {
        'twitter': [
            (
                {
                    'name': 'Amy Butler',
                    'screen_name': 'WayfarersBook',
                    'location': 'Kyiv, Ukraine',
                    'description': 'Long-term expat, CELTA/Delta qualified English teacher, freelance writer. Insta: wayfarersbook',
                    'url': 'https://t.co/7fIVtM8Ne0',
                    'followers_count': 699,
                    'friends_count': 680,
                    'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1018140475222523904/ADqhB2yj_normal.jpg'
                },
                [
                    '@CailinONeil @VickyFlipFlop @instagram Mine is basically cake, donuts, pasta, and the odd glamour fashion photo. ',
                    "@RoamingRequired Lucky. We've got all sorts of rules because everyone's really paranoid about "
                    "voter fraud.",
                    "@quickdarshan Embarrassingly, I've never tried before. (Me of little faith in my one vote.) My bf managed to vote i… ",
                    '@RoamingRequired Can you vote by mail? We need to get there. Or online, like Estonia, country of the freaking future.',
                    "@quickdarshan I know it's rigged, it still makes me really mad. Also seeing the clips of governors not being concer… ",
                    'These lines to vote are insane. We need to start rethinking our voting procedures now. ',
                    "@thethoughtcard I live in Kyiv -- it's a crazy affordable European destination. I've traveled a lot around Ukraine… ",
                    'RT @inclpablo: me after guessing the password of my own email ',
                    "Man, it's really a shame the cops can't do anything about all those looters. Definitely seems like they're trying.… ",
                    "How do you just walk by an old man bleeding on the ground?!\nDon't turn on the sound unless you want to be ill. ",
                    'RT @JordanUhl: Who does this protect? ',
                    'RT @joshfoxfilm: People stuck in traffic are witnessing NYPD beat up folks on their way home. ',
                    "I don't know whether or not this was actually before curfew, but why would you escalate with this tiny group of pea… ",
                    '@gaelemorag Thanks for reading. While the title is provocative, the content itself is more geared towards getting p… ',
                    'Looking for links to legit places to donate to looted/vandalized #NYC businesses. This article is a good starting p… ',
                    "@RoamingRequired @sunriseon7 Yes, it's embarrassing how we're treating international press. We even got publicly called out by Russia...",
                    'Your daily reminder that police are abusing and arresting cooperative reporters and journalists. Maybe if they did… ',
                    '@travchats A lot of people are hating on listicles, but if it comes from someone who has done the research, they ca… ',
                    'This is a super resource for people who are looking to get informed but are also a bit overwhelmed with information… ',
                    'In case anyone is wondering who is inciting violence, this FBI thread has devastating examples of #PoliceBrutality. '
                    ]
            )
        ]
    }
    print(caller_analyze_twitter(twitter_api_response, taken_input))
