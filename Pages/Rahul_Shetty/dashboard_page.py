from playwright.async_api import Page, Locator

from costuFixture.common.playwright_wrapper import PlaywrightWrapper


class DashboardPage(PlaywrightWrapper):

    def __init__(self, page: Page, screenshot_step):
        super().__init__(page)
        self.screenshot_step = screenshot_step

        self.btn_view_product: Locator = page.get_by_role(
            "button",
            name="View"
        ).first

        self.btn_add_to_cart: Locator = page.get_by_role(
            "button",
            name="Add to Cart"
        )

        self.btn_cart: Locator = page.locator(
            'button[routerlink="/dashboard/cart"]'
        )

    async def click_first_product(self):
        async def action():
            async with self.page.expect_response(
                lambda response:
                    response.request.method == "GET"
                    and "/api/ecom/product/get-product-detail/" in response.url
            ):
                await self.click(
                    self.btn_view_product,
                    "View product"
                )

        await self.screenshot_step(
            "Click First Product",
            action
        )

    async def add_to_cart(self):
        await self.screenshot_step(
            "Add Product To Cart",
            lambda: self.click(
                self.btn_add_to_cart,
                "Add to Cart"
            )
        )

    async def validate_toast_message(self, expected_text: str):
        async def action():
            await super(DashboardPage, self).validate_toast_message(
                expected_text,
                "Dashboard Page"
            )

        await self.screenshot_step(
            "Validate Product Toast",
            action
        )

    async def go_to_cart(self):
        await self.screenshot_step(
            "Go To Cart",
            lambda: self.click(
                self.btn_cart,
                "Cart"
            )
        )