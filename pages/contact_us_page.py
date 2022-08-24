from playwright.sync_api import Page, Locator
from settings.params import settings

class ContactUsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def name_field(self) -> Locator:
        return self.page.locator("input[name=\"name\"]")

    @property
    def email_field(self) -> Locator:
        return self.page.locator("input[name=\"email\"]")

    @property
    def phone_field(self) -> Locator:
        return self.page.locator("input[name=\"phone\"]")

    @property
    def message_field(self) -> Locator:
        return self.page.locator("textarea[name=\"message\"]")

    def fill_message_form(self, user_data: dict) -> None:
        self.name_field.fill(user_data["first_name"])
        self.email_field.fill(user_data["email"])
        self.phone_field.fill(user_data["phone"])
        self.message_field.fill(user_data["message"])

    def send_message_button(self, user_data: dict) -> None:
        self.fill_message_form(user_data)
        self.page.locator("text=Send to Customer Care").click()

    def send_message_prompt(self, user_data: dict) -> Locator:
        return self.page.locator(
            f'text=Thank you {user_data["first_name"]} A Customer Care Representative will be contacting you.')

    def navigate(self) -> None:
        self.page.goto(settings.TEST_URL)