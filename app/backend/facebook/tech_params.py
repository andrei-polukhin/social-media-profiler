# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

EMAIL_FIELD = (By.ID, "email")
PASSWORD_FIELD = (By.ID, "pass")
SUBMIT_BUTTON = (By.ID, "u_0_b")

SEARCH_LINK = "https://www.facebook.com/search/top?q="
FOUND_LINKS = (By.CSS_SELECTOR, ".d2edcug0.glvd648r.o7dlgrpb a")
