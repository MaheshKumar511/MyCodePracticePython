from playwright.async_api import Page

from Pages.Rahul_Shetty.login_page import LoginPage
from Pages.Rahul_Shetty.dashboard_page import DashboardPage
from Pages.Rahul_Shetty.cart_page import CartPage
from Pages.Rahul_Shetty.checkout_page import CheckoutPage
from Pages.Rahul_Shetty.confirmation_page import ConfirmationPage


class RahulShettyApp:

    def __init__(self, page: Page, screenshot_step):
        self.page = page
        self.screenshot_step = screenshot_step

        self._login_page = None
        self._dashboard_page = None
        self._cart_page = None
        self._checkout_page = None
        self._confirmation_page = None

    @property
    def login_page(self) -> LoginPage:
        if self._login_page is None:
            self._login_page = LoginPage(
                self.page,
                self.screenshot_step
            )

        return self._login_page

    @property
    def dashboard_page(self) -> DashboardPage:
        if self._dashboard_page is None:
            self._dashboard_page = DashboardPage(
                self.page,
                self.screenshot_step
            )

        return self._dashboard_page

    @property
    def cart_page(self) -> CartPage:
        if self._cart_page is None:
            self._cart_page = CartPage(
                self.page,
                self.screenshot_step
            )

        return self._cart_page

    @property
    def checkout_page(self) -> CheckoutPage:
        if self._checkout_page is None:
            self._checkout_page = CheckoutPage(
                self.page,
                self.screenshot_step
            )

        return self._checkout_page

    @property
    def confirmation_page(self) -> ConfirmationPage:
        if self._confirmation_page is None:
            self._confirmation_page = ConfirmationPage(
                self.page,
                self.screenshot_step
            )

        return self._confirmation_page