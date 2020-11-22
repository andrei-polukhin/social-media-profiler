# -*- coding: utf-8 -*-
"""The Facebook scraping module initializing web-browser to open Facebook homepage."""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class FacebookHomepage:
    """The class to open Facebook homepage with a binary chromebrowser."""
    def __init__(self):
        options = self.__add_chrome_options()
        self._driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options
        )

    def facebook_open_home_page(self):
        """Open Facebook homepage."""
        self._driver.get("https://www.facebook.com")

    @staticmethod
    def __add_chrome_options():
        """Add browser options to disable notification and open headlessly."""
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("headless")
        return options


if __name__ == "__main__":
    o = FacebookHomepage()
    o.facebook_open_home_page()
