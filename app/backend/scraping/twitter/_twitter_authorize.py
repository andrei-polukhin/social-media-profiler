# -*- coding: utf-8 -*-
import tweepy

from app.backend._config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET,
)


class TwitterAuthorize:
    def __init__(self):
        self.redirect_url = ""
        self.api = None
        self.auth = None

    def twitter_authorize(self):
        self._twitter_get_auth()
        self._twitter_get_api()

    def _twitter_get_auth(self):
        self.auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

    def _twitter_get_api(self):
        self.api = tweepy.API(self.auth)


if __name__ == "__main__":
    twitter_obj = TwitterAuthorize()
    twitter_obj.twitter_authorize()
