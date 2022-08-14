from playwright.sync_api import Page, Locator
from settings.params import settings


class RegisterPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def first_name_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.firstName"]')

    @property
    def last_name_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.lastName"]')

    @property
    def address_street_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.address\\.street"]')

    @property
    def address_city_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.address\\.city"]')

    @property
    def address_state_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.address\\.state"]')

    @property
    def address_zipcode_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.address\\.zipCode"]')

    @property
    def phone_number_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.phoneNumber"]')

    @property
    def ssn_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.ssn"]')

    @property
    def user_name_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.username"]')

    @property
    def password_field(self) -> Locator:
        return self.page.locator('input[name="customer\\.password"]')

    @property
    def repeated_password_field(self) -> Locator:
        return self.page.locator('input[name="repeatedPassword"]')

    @property
    def register_button(self) -> Locator:
        return self.page.locator('input:has-text("Register")')

    def user_registered_prompt(self, user_data: dict) -> Locator:
        return self.page.locator(
            f'text=Welcome {user_data["username"]} Your account was created successfully. You are now logged in.'
        )

    def fill_registration_form(self, user_data: dict) -> None:
        self.first_name_field.fill(user_data["first_name"])
        self.last_name_field.fill(user_data["last_name"])
        self.address_street_field.fill(user_data["address"])
        self.address_city_field.fill(user_data["city"])
        self.address_state_field.fill(user_data["state"])
        self.address_zipcode_field.fill(user_data["zip_code"])
        self.phone_number_field.fill(user_data["phone"])
        self.ssn_field.fill(user_data["ssn"])
        self.user_name_field.fill(user_data["username"])
        self.password_field.fill(user_data["password"])
        self.repeated_password_field.fill(user_data["password"])

    def register_new_user(self, user_data: dict) -> None:
        self.fill_registration_form(user_data)
        self.register_button.click()

    def navigate(self) -> None:
        self.page.goto(settings.TEST_URL)
