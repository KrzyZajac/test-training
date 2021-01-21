import pytest
from assets.main_page_data import BEST_PLAYERS_HEADER_TEXT
from assets.urls import TEAM_COMPARISON_PAGE_URL
from objects.main_page_object import MainPageObject
from selenium.webdriver import Chrome


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_main_page_title_is_displayed(browser):
    main_page = MainPageObject(browser)
    main_page.open_page()
    assert main_page.main_page_title().is_displayed()


def test_main_page_nav(browser):
    main_page = MainPageObject(browser)
    main_page.open_page()
    assert main_page.main_page_nav().is_displayed()
    assert len(main_page.navigation_button()) == 2


def test_best_player_cards_header_text(browser):
    main_page = MainPageObject(browser)
    main_page.open_page()
    assert main_page.best_players_cards_header().text == BEST_PLAYERS_HEADER_TEXT


def test_main_menu_buttons(browser):
    main_page = MainPageObject(browser)
    main_page.open_page()
    (main_page.navigation_button())[0].click()
    browser.implicitly_wait(5)
    assert browser.current_url == TEAM_COMPARISON_PAGE_URL

