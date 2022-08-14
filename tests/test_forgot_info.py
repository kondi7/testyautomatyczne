from playwright.sync_api import expect, Playwright
from time import time
from settings.fixtures import user_data
from pages.main_page import MainPage
from pages.forgot_info_page import ForgotPage


def test_forgot_info(user_data: dict, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    main_page = MainPage(page)
    forgot_info_page = ForgotPage(page)
    main_page.navigate()
    main_page.go_to_forgot_login_info_form()
    page.pause()
    forgot_info_page.find_my_login_info(user_data)

    context.close()
    browser.close()
