from playwright.sync_api import expect, Playwright
from settings.fixtures import user_data
from pages.main_page import MainPage
from pages.contact_us_page import ContactUsPage


def test_contact_us(user_data: dict, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    main_page = MainPage(page)
    contact_us_page = ContactUsPage(page)
    main_page.navigate()
    main_page.go_to_contact_us_form()
    page.pause()
    contact_us_page.send_message_button(user_data)
    expect(contact_us_page.send_message_prompt(user_data)).to_be_visible()

    context.close()
    browser.close()