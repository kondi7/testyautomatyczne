from playwright.sync_api import expect, Playwright
from pages.main_page import MainPage
from settings.fixtures import user_data

def test_login_to_app(user_data: dict, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    main_page = MainPage(page)
    main_page.navigate()
    page.pause()
    main_page.login_to_app(user_data)

    context.close()
    browser.close()