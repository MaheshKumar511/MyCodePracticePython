from playwright.async_api import Page, Locator

from costuFixture.common.playwright_wrapper import PlaywrightWrapper


class CartPage(PlaywrightWrapper):

    def __init__(self, page: Page, screenshot_step):
        super().__init__(page)
        self.screenshot_step = screenshot_step

        self.txt_cart_price1: Locator = page.get_by_text("$").nth(2)
        self.txt_cart_price2: Locator = page.get_by_text("$").nth(3)
        self.btn_checkout: Locator = page.get_by_role(
            "button",
            name="Checkout"
        )
        self.txt_product_id: Locator = page.locator(".itemNumber")

    async def verify_cart_price1(self):
        await self.screenshot_step(
            "Verify Cart Price 1",
            lambda: self.expect_visible(
                self.txt_cart_price1,
                "Cart Price 1"
            )
        )

    async def verify_cart_price2(self):
        await self.screenshot_step(
            "Verify Cart Price 2",
            lambda: self.expect_visible(
                self.txt_cart_price2,
                "Cart Price 2"
            )
        )

    async def verify_product_id(self):
        await self.screenshot_step(
            "Verify Product ID",
            lambda: self.expect_visible(
                self.txt_product_id,
                "Product ID"
            )
        )

    async def checkout(self):
        await self.screenshot_step(
            "Checkout",
            lambda: self.click(
                self.btn_checkout,
                "Checkout"
            )
        )