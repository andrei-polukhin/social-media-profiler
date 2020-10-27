from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import tweepy
import time
import random

from app.backend.config \
    import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_LOGIN, \
    TWITTER_PASSWORD, TWITTER_PHONE_NUMBER
from app.backend.data_scraping.facebook.facebook_homepage \
    import FacebookHomepage
from app.backend.data_scraping.twitter.twitter_tech_params \
    import ALLOW_BUTTON, PIN_VALUE, USERNAME_OR_EMAIL, \
    PASSWORD, PHONE_NUMBER, SUBMIT_CHALLENGE_BUTTON


class TwitterAuthorize:
    CALLBACK_URI = "oob"

    def __init__(self):
        self.redirect_url = ""
        self.api = None
        self.auth = None
        self.pin_value = 0
        options = FacebookHomepage.add_chrome_options()
        options.add_argument("--lang=us")
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=options
        )
        self.wait = WebDriverWait(self.driver, 5)

    def twitter_authorize(self):
        self.twitter_get_redirect_url()
        self.twitter_get_pin_value()
        self.twitter_get_api()

    def twitter_get_redirect_url(self):
        self.auth = tweepy.OAuthHandler(
            TWITTER_API_KEY,
            TWITTER_API_SECRET,
            TwitterAuthorize.CALLBACK_URI
        )
        self.redirect_url = self.auth.get_authorization_url()

    def twitter_get_pin_value(self):
        self.driver.get(self.redirect_url)
        self.driver.implicitly_wait(5)
        self.twitter_send_login_and_password()
        self.twitter_allow_button()
        self.twitter_check_for_challenge()
        self.twitter_get_api()

    def twitter_send_login_and_password(self):
        time.sleep(random.randint(1, 2))
        login_field = self.wait.until(
            EC.presence_of_element_located(
                USERNAME_OR_EMAIL
            )
        )
        login_field.send_keys(TWITTER_LOGIN)
        time.sleep(random.randint(1, 2))
        password_field = self.wait.until(
            EC.presence_of_element_located(
                PASSWORD
            )
        )
        password_field.send_keys(TWITTER_PASSWORD)
        time.sleep(random.randint(1, 2))

    def twitter_check_for_challenge(self):
        if self.driver.current_url.startswith(
                "https://twitter.com/account/login_challenge"
        ):
            self.twitter_challenge_phone_number()
        self.twitter_allow_button()
        self.twitter_pin_element()

    def twitter_challenge_phone_number(self):
        time.sleep(random.randint(1, 2))
        phone_number = self.wait.until(
            EC.presence_of_element_located(
                PHONE_NUMBER
            )
        )
        phone_number.send_keys(TWITTER_PHONE_NUMBER)
        time.sleep(random.randint(1, 2))
        submit_challenge = self.wait.until(
            EC.element_to_be_clickable(
                SUBMIT_CHALLENGE_BUTTON
            )
        )
        submit_challenge.click()
        time.sleep(random.randint(1, 2))

    def twitter_allow_button(self):
        allow_button = self.wait.until(
            EC.element_to_be_clickable(
                ALLOW_BUTTON
            )
        )
        allow_button.click()

    def twitter_pin_element(self):
        pin_element = self.wait.until(
            EC.presence_of_element_located(
                PIN_VALUE
            )
        )
        self.pin_value = pin_element.text

    def twitter_get_api(self):
        _ = self.auth.get_access_token(self.pin_value)
        time.sleep(random.randint(2, 4))
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)


if __name__ == "__main__":
    twitter_obj = TwitterAuthorize()
    twitter_obj.twitter_authorize()
