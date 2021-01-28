import pytest
from assets.main_page_data import BEST_PLAYERS_HEADER_TEXT
from assets.urls import MAIN_URL, TEAM_COMPARISON_PAGE_URL, SQUADS_PAGE_URL
from objects.main_page_object import MainPageObject
from selenium.webdriver import Chrome


@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(MAIN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_main_page_title_is_displayed(browser):
    assert MainPageObject(browser).main_page_title().is_displayed()


def test_main_page_nav(browser):
    main_page = MainPageObject(browser)
    assert main_page.main_page_nav().is_displayed()
    assert len(main_page.navigation_button()) == 2


def test_best_player_cards_header_text(browser):
    assert MainPageObject(browser).best_players_cards_header().text == BEST_PLAYERS_HEADER_TEXT


def test_main_menu_buttons(browser):
    MainPageObject(browser).navigation_button()[0].click()
    browser.implicitly_wait(2)
    assert browser.current_url == TEAM_COMPARISON_PAGE_URL
    browser.get(MAIN_URL)
    browser.implicitly_wait(2)
    MainPageObject(browser).navigation_button()[1].click()
    assert browser.current_url == SQUADS_PAGE_URL
