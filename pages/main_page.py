from playwright.sync_api import Page, Locator
from settings.params import settings


class MainPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def register_button(self) -> Locator:
        return self.page.locator("text=Register")

    @property
    def forgot_login_info_button(self) -> Locator:
        return self.page.locator("text=Forgot login info?")

    @property
    def customer_login_field(self) -> Locator:
        return self.page.locator("input[name=\"username\"]")

    @property
    def password_login_field(self) -> Locator:
        return self.page.locator("input[name=\"password\"]")

    @property
    def log_in_button(self) -> Locator:
        return self.page.locator("text=Log In")

    def login_to_app(self, user_data) -> None:
        self.customer_login_field.fill(user_data["username"])
        self.password_login_field.fill(user_data["password"])
        self.log_in_button.click()

    def go_to_forgot_login_info_form(self) -> None:
        self.forgot_login_info_button.click()

    def go_to_register_form(self) -> None:
        self.register_button.click()

    def navigate(self) -> None:
        self.page.goto(settings.TEST_URL)
