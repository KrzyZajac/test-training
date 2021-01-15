from tests.locators import main_page_locators as locators
from tests.assets.urls import MAIN_URL
from selenium import webdriver


class MainPageObject(object):

    def __init__(self, driver, *args, **kw):
        self.driver = webdriver.Chrome()
        self.driver.get(MAIN_URL)

    def main_page_title(self):
        self.driver.find_element(locators.MAIN_PAGE_TITLE)
