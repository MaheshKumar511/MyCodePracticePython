from playwright.async_api import Page, Locator

from costuFixture.common.playwright_wrapper import PlaywrightWrapper


class LoginPage(PlaywrightWrapper):

    def __init__(self, page: Page, screenshot_step):
        super().__init__(page)
        self.screenshot_step = screenshot_step

        self.txt_email: Locator = page.get_by_role(
            "textbox",
            name="email@example.com"
        )
        self.txt_password: Locator = page.get_by_role(
            "textbox",
            name="enter your passsword"
        )
        self.btn_login: Locator = page.get_by_role(
            "button",
            name="Login"
        )
        self.login_toast = ""

    async def navigate(self):
        await self.screenshot_step(
            "Navigate to Login Page",
            lambda: self.goto(
                "https://rahulshettyacademy.com/client/#/auth/login"
            )
        )

    async def enter_email(self, email: str):
        await self.screenshot_step(
            "Enter Email",
            lambda: self.fill(
                self.txt_email,
                email,
                "Email"
            )
        )

    async def enter_password(self, password: str):
        await self.screenshot_step(
            "Enter Password",
            lambda: self.fill(
                self.txt_password,
                password,
                "Password"
            )
        )

    async def click_login(self, expected_text: str):
        async def action():
            await self.click(
                self.btn_login,
                "Login button"
            )

            await super(LoginPage, self).validate_toast_message(
                expected_text,
                "Login Page"
            )

            self.login_toast = expected_text

        await self.screenshot_step(
            "Click Login",
            action
        )

    async def validate_url(self, expected_text: str):
        async def action():
            await self.page.wait_for_url(
                lambda url: expected_text in url,
                timeout=5000
            )

        await self.screenshot_step(
            "Validate Dashboard URL",
            action
        )

    async def validate_toast_message(self, expected_text: str):
        async def action():
            assert expected_text.lower() in self.login_toast.lower()

        await self.screenshot_step(
            "Validate Login Toast",
            action
        )