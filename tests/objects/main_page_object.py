from locators import main_page_locators as locators
from selenium.webdriver.common.by import By


class MainPageObject(object):

    def __init__(self, driver, *args, **kw):
        self.driver = driver

    def main_page_title(self):
        return self.driver.find_element(By.CLASS_NAME, locators.MAIN_PAGE_TITLE)

    def main_page_nav(self):
        return self.driver.find_element(By.CLASS_NAME, locators.MAIN_NAVIGATION)

    def navigation_button(self):
        return self.driver.find_elements(By.CLASS_NAME, locators.NAVIGATION_BUTTON)

    def best_players_cards_header(self):
        return self.driver.find_element(By.CLASS_NAME, locators.BEST_PLAYERS_CARDS_HEADER)

    def best_players_cards_section(self):
        return self.driver.find_element(By.CLASS_NAME, locators.BEST_PLAYERS_CARDS_SECTION)

    def best_player_card(self):
        return self.driver.find_elements(By.CLASS_NAME, locators.BEST_PLAYER_CARD)

    def player_photo(self):
        return self.driver.find_elements(By.CLASS_NAME, locators.PLAYER_PHOTO)

    def player_name(self):
        return self.driver.find_elements(By.CLASS_NAME, locators.PLAYER_NAME)

    def player_stats(self):
        return self.driver.find_elements(By.CLASS_NAME, locators.PLAYER_STATS)

    def footer(self):
        return self.driver.find_element(By.CLASS_NAME, locators.FOOTER)
