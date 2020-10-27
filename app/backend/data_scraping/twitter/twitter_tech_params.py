from selenium.webdriver.common.by import By

ALLOW_BUTTON = (By.ID, "allow")
PIN_VALUE = (By.XPATH, "//*[@id=\"oauth_pin\"]/p/kbd/code")
USERNAME_OR_EMAIL = (By.ID, "username_or_email")
PASSWORD = (By.ID, "password")
PHONE_NUMBER = (By.ID, "challenge_response")
SUBMIT_CHALLENGE_BUTTON = (By.ID, "email_challenge_submit")
