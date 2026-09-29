import os
import pytest_asyncio
from playwright.async_api import Page

from pages.rahul_shetty_app import RahulShettyApp


class MaheshCustomFixture:

    def __init__(self, page: Page, screenshot_step):
        self.page = page
        self.screenshot_step = screenshot_step

        self._rahul_shetty = None

    @property
    def rahul_shetty(self) -> RahulShettyApp:
        if self._rahul_shetty is None:
            self._rahul_shetty = RahulShettyApp(self.page)

        return self._rahul_shetty


@pytest_asyncio.fixture
async def mahesh_custom_fixture(page: Page, request):
    async def screenshot_step(name, fn):
        try:
            await fn()

            screenshot_path = os.path.join(
                "test-results",
                request.node.name,
                f"{name}.png"
            )

            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

            await page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            print(f"PASS: {name}")

        except Exception:
            screenshot_path = os.path.join(
                "test-results",
                request.node.name,
                f"{name}-FAILED.png"
            )

            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

            await page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            print(f"FAIL: {name}")
            raise

    yield MaheshCustomFixture(page, screenshot_step)