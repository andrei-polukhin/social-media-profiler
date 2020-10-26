from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import tweepy

from app.backend.config \
    import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_LOGIN, TWITTER_PASSWORD
from app.backend.data_scraping.facebook.facebook_homepage import FacebookHomepage
from app.backend.data_scraping.twitter.twitter_tech_params \
    import ALLOW_BUTTON, PIN_VALUE, USERNAME_OR_EMAIL, PASSWORD


class TwitterAuthorize:
    CALLBACK_URI = "oob"

    def __init__(self):
        self.redirect_url = ""
        self.api = None
        self.auth = None
        self.pin_value = 0
        options = FacebookHomepage.add_chrome_options()
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
        self.twitter_allow_button_and_pin_value()

    def twitter_send_login_and_password(self):
        login_field = self.wait.until(
            EC.presence_of_element_located(
                USERNAME_OR_EMAIL
            )
        )
        login_field.send_keys(TWITTER_LOGIN)
        password_field = self.wait.until(
            EC.presence_of_element_located(
                PASSWORD
            )
        )
        password_field.send_keys(TWITTER_PASSWORD)

    def twitter_allow_button_and_pin_value(self):
        allow_button = self.wait.until(
            EC.element_to_be_clickable(
                ALLOW_BUTTON
            )
        )
        allow_button.click()
        pin_element = self.wait.until(
            EC.presence_of_element_located(
                PIN_VALUE
            )
        )
        self.pin_value = pin_element.text

    def twitter_get_api(self):
        self.auth.get_access_token(self.pin_value)
        self.api = tweepy.API(self.auth)


if __name__ == "__main__":
    twitter_obj = TwitterAuthorize()
    twitter_obj.twitter_authorize()
