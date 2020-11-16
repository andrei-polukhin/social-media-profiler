# -*- coding: utf-8 -*-
"""The Twitter scraping authorization module."""

import os
import tweepy


class TwitterAuthorize:
    """The class to authorize on Twitter using its API."""
    def __init__(self):
        self._api = None
        self.__auth = None

    def twitter_authorize(self):
        """
        Call other methods to authorize on Twitter.
        """
        self._twitter_get_auth()
        self._twitter_get_api()

    def _twitter_get_auth(self):
        """
        Authorize on Twitter using API key, secret, access token and access token secret.
        """
        self.__auth = tweepy.OAuthHandler(
            os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_SECRET")
        )
        self.__auth.set_access_token(
            os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
        )

    def _twitter_get_api(self):
        """Get API access using OAuth2.0."""
        self._api = tweepy.API(self.__auth)


if __name__ == "__main__":
    twitter_obj = TwitterAuthorize()
    twitter_obj.twitter_authorize()
