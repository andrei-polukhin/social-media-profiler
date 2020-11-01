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
        self._api = None
        self.__auth = None

    def twitter_authorize(self):
        self._twitter_get_auth()
        self._twitter_get_api()

    def _twitter_get_auth(self):
        self.__auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        self.__auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

    def _twitter_get_api(self):
        self._api = tweepy.API(self.__auth)


if __name__ == "__main__":
    twitter_obj = TwitterAuthorize()
    twitter_obj.twitter_authorize()
