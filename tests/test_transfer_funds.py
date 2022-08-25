from playwright.sync_api import expect, Playwright
from pages.main_page import MainPage
from settings.fixtures import user_data
from pages.transfer_funds_page import TransferFunds


def test_transfer_funds(user_data: dict, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    main_page = MainPage(page)
    main_page.navigate()
    transfer_funds_page = TransferFunds(page)
    page.pause()
    main_page.login_to_app(user_data)
    transfer_funds_page.transfer(user_data)
    expect(transfer_funds_page.transfer_complete_prompt(user_data)).to_be_visible()

    context.close()
    browser.close()
