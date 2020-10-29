# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class FacebookHomepage:
    def __init__(self):
        options = self.add_chrome_options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def open_home_page(self):
        self.driver.get("https://www.facebook.com")

    @staticmethod
    def add_chrome_options():
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        # options.add_argument("headless")
        return options


if __name__ == "__main__":
    o = FacebookHomepage()
    o.open_home_page()
