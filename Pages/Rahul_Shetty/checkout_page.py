import re

from playwright.async_api import Page, Locator

from costuFixture.common.playwright_wrapper import PlaywrightWrapper


class CheckoutPage(PlaywrightWrapper):

    def __init__(self, page: Page, screenshot_step):
        super().__init__(page)
        self.screenshot_step = screenshot_step

        self.cmb_expiry: Locator = page.get_by_role(
            "combobox"
        ).nth(1)

        self.txt_cvv: Locator = page.get_by_role(
            "textbox"
        ).nth(1)

        self.txt_card_holder_name: Locator = page.get_by_role(
            "textbox"
        ).nth(2)

        self.txt_country: Locator = page.get_by_role(
            "textbox",
            name="Select Country"
        )

        self.btn_place_order: Locator = page.get_by_text(
            "Place Order"
        )

    def btn_country_option(self, country: str) -> Locator:
        pattern = re.compile(
            rf"^\s*{re.escape(country)}\s*$",
            re.IGNORECASE
        )

        return (
            self.page.locator(
                "section.ta-results button.ta-item"
            )
            .filter(has_text=pattern)
            .first
        )

    async def select_expiry(self):
        await self.screenshot_step(
            "Select Expiry",
            lambda: self.select_option(
                self.cmb_expiry,
                "30",
                "Expiry"
            )
        )

    async def enter_cvv(self, cvv: str):
        await self.screenshot_step(
            "Enter CVV",
            lambda: self.fill(
                self.txt_cvv,
                cvv,
                "CVV"
            )
        )

    async def enter_card_holder_name(self, name: str):
        await self.screenshot_step(
            "Enter Card Holder Name",
            lambda: self.fill(
                self.txt_card_holder_name,
                name,
                "Card Holder Name"
            )
        )

    async def enter_country(self, country: str):
        async def action():
            await self.fill(
                self.txt_country,
                country,
                "Country"
            )
            await self.press(
                self.txt_country,
                "Backspace",
                "Country"
            )

        await self.screenshot_step(
            "Enter Country",
            action
        )

    async def select_country(self, country: str):
        async def action():
            country_option = self.btn_country_option(country)

            await self.wait_for_visible(
                country_option,
                "Country"
            )

            await self.click(
                country_option,
                country
            )

        await self.screenshot_step(
            "Select Country",
            action
        )

    async def place_order(self):
        await self.screenshot_step(
            "Place Order",
            lambda: self.click(
                self.btn_place_order,
                "Place Order"
            )
        )