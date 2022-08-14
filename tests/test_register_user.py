from playwright.sync_api import expect, Playwright
from time import time
from settings.fixtures import user_data
from pages.main_page import MainPage
from pages.register_page import RegisterPage


def test_register_user(user_data: dict, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    main_page = MainPage(page)
    register_page = RegisterPage(page)
    user_data["username"] = user_data["username"] + str(time())[:-10]
    main_page.navigate()
    main_page.go_to_register_form()
    page.pause()
    register_page.register_new_user(user_data)
    expect(register_page.user_registered_prompt(user_data)).to_be_visible()

    context.close()
    browser.close()
