from playwright.sync_api import Page, Locator
from settings.params import settings


class MainPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def register_button(self) -> Locator:
        return self.page.locator("text=Register")

    def go_to_register_form(self) -> None:
        self.register_button.click()

    def navigate(self) -> None:
        self.page.goto(settings.TEST_URL)
