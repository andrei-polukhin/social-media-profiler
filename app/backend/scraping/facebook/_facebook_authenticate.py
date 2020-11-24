# -*- coding: utf-8 -*-
"""The Facebook scraping module doing authentication."""

import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from app.backend.scraping.facebook._facebook_tech_params import (
    EMAIL_FIELD,
    PASSWORD_FIELD,
    SUBMIT_BUTTON,
)
from app.backend.scraping.facebook._facebook_homepage import FacebookHomepage


class FacebookAuthenticate(FacebookHomepage):
    """
    The class authenticating user on Facebook.
    """
    def __init__(self):
        super().__init__()
        self._wait = WebDriverWait(self._driver, 5)
        self._login_field = None
        self._pass_field = None
        self._submit_button = None

    def facebook_authenticate(self):
        """
        Call other methods to commit authentication.
        """
        self.__facebook_find_login_and_password_fields()
        self.__facebook_send_credentials()
        self.__facebook_find_and_click_on_submit_button()

    def __facebook_find_login_and_password_fields(self):
        """
        Find login and password fields on the homepage.
        """
        login_selector = EMAIL_FIELD[0]
        login_value = EMAIL_FIELD[1]
        pass_selector = PASSWORD_FIELD[0]
        pass_value = PASSWORD_FIELD[1]
        self._login_field = self._driver.find_element(
            login_selector, login_value
        )
        self._pass_field = self._driver.find_element(
            pass_selector, pass_value
        )

    def __facebook_send_credentials(self):
        """
        Send credentials to Facebook login and password fields.
        """
        self._login_field.send_keys(os.getenv("FACEBOOK_LOGIN"))
        self._pass_field.send_keys(os.getenv("FACEBOOK_PASSWORD"))

    def __facebook_find_and_click_on_submit_button(self):
        """
        Press on the submit button after sending Facebook credentials.
        """
        self._submit_button = self._wait.until(
            EC.element_to_be_clickable(SUBMIT_BUTTON)
        )
        self._submit_button.click()
