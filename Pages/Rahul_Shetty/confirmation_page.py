from playwright.async_api import Page, Locator

from costuFixture.common.playwright_wrapper import PlaywrightWrapper


class ConfirmationPage(PlaywrightWrapper):

    def __init__(self, page: Page, screenshot_step):
        super().__init__(page)
        self.screenshot_step = screenshot_step

        self.txt_order_confirmation_number: Locator = page.locator(
            ".ng-star-inserted"
        )

        self.txt_order_amount: Locator = page.get_by_text("$")

        self.txt_toast: Locator = page.locator(
            "#toast-container"
        )

    async def verify_order_confirmation_number(self):
        await self.screenshot_step(
            "Verify Order Confirmation Number",
            lambda: self.expect_visible(
                self.txt_order_confirmation_number,
                "Order Confirmation Number"
            )
        )

    async def verify_order_amount(self):
        await self.screenshot_step(
            "Verify Order Amount",
            lambda: self.expect_visible(
                self.txt_order_amount,
                "Order Amount"
            )
        )

    async def validate_toast_message(self, expected_text: str):
        async def action():
            await super(
                ConfirmationPage,
                self
            ).validate_toast_message(
                expected_text,
                "Confirmation Page"
            )

        await self.screenshot_step(
            "Validate Order Toast",
            action
        )