from playwright.sync_api import Page, Locator
from settings.params import settings


class TransferFunds:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def amount_field(self) -> Locator:
        return self.page.locator("input[name=\"input\"]")

    @property
    def transfer_funds_button(self) -> Locator:
        return self.page.locator("text=Transfer Funds")

    @property
    def transfer_button(self) -> Locator:
        return self.page.locator("input:has-text(\"Transfer\")")

    def transfer_complete_prompt(self, user_data: dict) -> Locator:
        return self.page.locator(
            f'text=${user_data["amount"]}.00 has been transferred'
        )

    def fill_amount_form(self, user_data: dict) -> None:
        self.amount_field.fill(user_data["amount"])

    def transfer(self, user_data: dict) -> None:
        self.transfer_funds_button.click()
        self.fill_amount_form(user_data)
        self.transfer_button.click()

    def navigate(self) -> None:
        self.page.goto(settings.TEST_URL)
