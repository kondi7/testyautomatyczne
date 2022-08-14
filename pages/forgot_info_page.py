from playwright.sync_api import Page, Locator
from settings.params import settings


class ForgotPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def first_name_field(self) -> Locator:
        return self.page.locator("input[name=\"firstName\"]")

    @property
    def last_name_field(self) -> Locator:
        return self.page.locator("input[name=\"lastName\"]")

    @property
    def address_field(self) -> Locator:
        return self.page.locator("input[name=\"address\\.street\"]")

    @property
    def address_city_field(self) -> Locator:
        return self.page.locator("input[name=\"address\\.city\"]")

    @property
    def address_state_field(self) -> Locator:
        return self.page.locator("input[name=\"address\\.state\"]")

    @property
    def address_zipcode_field(self) -> Locator:
        return self.page.locator("input[name=\"address\\.zipCode\"]")

    @property
    def ssn_field(self) -> Locator:
        return self.page.locator("input[name=\"ssn\"]")

    @property
    def forgot_login_info_button(self) -> Locator:
        return self.page.locator("text=Forgot login info?")

    @property
    def find_login_info_button(self) -> Locator:
        return self.page.locator("text=Find My Login Info")

    def fill_forgotinfo_form(self, user_data: dict) -> None:
        self.first_name_field.fill(user_data["first_name"])
        self.last_name_field.fill(user_data["last_name"])
        self.address_field.fill(user_data["address"])
        self.address_city_field.fill(user_data["city"])
        self.address_state_field.fill(user_data["state"])
        self.address_zipcode_field.fill(user_data["zip_code"])
        self.ssn_field.fill(user_data["ssn"])

    def find_my_login_info(self, user_data: dict) -> None:
        self.fill_forgotinfo_form(user_data)
        self.find_login_info_button.click()

    def navigate(self) -> None:
        self.page.goto(settings.TEST_URL)
