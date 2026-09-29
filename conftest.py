import os
from pathlib import Path

import pytest_asyncio
from dotenv import load_dotenv
from playwright.async_api import async_playwright, Page

from Pages.Rahul_Shetty.rahul_shetty_app import RahulShettyApp
from api.api_fixture import ApiFixture
from utils.pdf_report import PdfReport

load_dotenv()


@pytest_asyncio.fixture
async def mahesh_custom_fixture(request):
    report_steps = []
    request.node.report_steps = report_steps

    headed = request.config.getoption("--headed")

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(
            headless=not headed
        )

        context = await browser.new_context()
        page = await context.new_page()

        async def screenshot_step(name, fn):
            page_name = "RahulShetty"
            screenshot_dir = (
                Path("test-results")
                / request.node.name
            )
            screenshot_dir.mkdir(parents=True, exist_ok=True)

            try:
                await fn()

                screenshot = screenshot_dir / f"{name}.png"

                await page.screenshot(
                    path=str(screenshot),
                    full_page=True
                )

                report_steps.append({
                    "page": page_name,
                    "method": name,
                    "status": "PASS",
                    "screenshot": str(screenshot)
                })

                print(f"PASS: {name}")

            except Exception:
                screenshot = screenshot_dir / f"{name}-FAILED.png"

                await page.screenshot(
                    path=str(screenshot),
                    full_page=True
                )

                report_steps.append({
                    "page": page_name,
                    "method": name,
                    "status": "FAIL",
                    "screenshot": str(screenshot)
                })

                print(f"FAIL: {name}")
                raise

        yield MaheshCustomFixture(page, screenshot_step)

        await context.close()
        await browser.close()


class MaheshCustomFixture:

    def __init__(self, page: Page, screenshot_step):
        self.page = page
        self.screenshot_step = screenshot_step
        self._rahul_shetty = None

    @property
    def rahul_shetty(self) -> RahulShettyApp:
        if self._rahul_shetty is None:
            self._rahul_shetty = RahulShettyApp(
                self.page,
                self.screenshot_step
            )

        return self._rahul_shetty


@pytest_asyncio.fixture
async def api():
    async with async_playwright() as playwright:
        request = await playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )

        fixture = ApiFixture(request)

        yield fixture

        await request.dispose()


def pytest_runtest_makereport(item, call):
    if call.when != "call":
        return

    steps = getattr(item, "report_steps", [])

    if steps:
        PdfReport.generate(item.name, steps)