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

<<<<<<< HEAD
    @property
    def forgot_login_info_button(self) -> Locator:
        return self.page.locator("text=Forgot login info?")

    def go_to_forgot_login_info_form(self) -> None:
        self.forgot_login_info_button.click()

    def navigate(self) -> None:
        self.page.goto(settings.TEST_URL)

=======
    def navigate(self) -> None:
        self.page.goto(settings.TEST_URL)
>>>>>>> 955c463c696d1772ff8ab3f5858211354b62c497
