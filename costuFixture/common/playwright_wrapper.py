from datetime import datetime

from playwright.async_api import Locator, Page, expect


class PlaywrightWrapper:

    def __init__(self, page: Page):
        self.page = page

    # =========================
    # Timestamp
    # =========================

    def _get_timestamp(self) -> str:
        return datetime.now().strftime("%H:%M:%S.%f")[:-3]

    # =========================
    # Console Logger
    # =========================

    def _log(self, message: str) -> None:
        print(f"[{self._get_timestamp()}] {message}")

    # =========================
    # Navigation
    # =========================

    async def goto(self, url: str) -> None:
        self._log("Started goto method")

        try:
            await self.page.goto(url)

            self._log(f"Navigated to: {url}")
            self._log("Completed goto method")

        except Exception:
            self._log("Failed goto method")
            raise

    # =========================
    # Click
    # =========================

    async def click(
        self,
        locator: Locator,
        element_name: str | None = None
    ) -> None:
        self._log("Started click method")

        try:
            await locator.click()

            self._log(
                f"Clicked: {element_name}"
                if element_name
                else "Clicked"
            )

            self._log("Completed click method")

        except Exception:
            self._log("Failed click method")
            raise

    # =========================
    # Fill
    # =========================

    async def fill(
        self,
        locator: Locator,
        value: str,
        element_name: str | None = None
    ) -> None:
        self._log("Started fill method")

        try:
            await locator.fill(value)

            self._log(
                f"Filled: {element_name}"
                if element_name
                else "Filled"
            )

            self._log("Completed fill method")

        except Exception:
            self._log("Failed fill method")
            raise

    # =========================
    # Select Option
    # =========================

    async def select_option(
        self,
        locator: Locator,
        value: str,
        element_name: str | None = None
    ) -> None:
        self._log("Started select_option method")

        try:
            await locator.select_option(value)

            self._log(
                f"Selected: {element_name}"
                if element_name
                else f"Selected option: {value}"
            )

            self._log("Completed select_option method")

        except Exception:
            self._log("Failed select_option method")
            raise

    # =========================
    # Verify Element Visible
    # =========================

    async def expect_visible(
        self,
        locator: Locator,
        element_name: str | None = None
    ) -> None:
        self._log("Started expect_visible method")

        try:
            await expect(locator).to_be_visible()

            self._log(
                f"Verified visible: {element_name}"
                if element_name
                else "Verified element is visible"
            )

            self._log("Completed expect_visible method")

        except Exception:
            self._log("Failed expect_visible method")
            raise

    # =========================
    # Get Text
    # =========================

    async def get_text(
        self,
        locator: Locator,
        element_name: str | None = None
    ) -> str:
        self._log("Started get_text method")

        try:
            text = await locator.text_content()

            self._log(
                f"Text retrieved from: {element_name}"
                if element_name
                else "Text retrieved"
            )

            self._log("Completed get_text method")

            return text or ""

        except Exception:
            self._log("Failed get_text method")
            raise

    # =========================
    # Check
    # =========================

    async def check(
        self,
        locator: Locator,
        element_name: str | None = None
    ) -> None:
        self._log("Started check method")

        try:
            await locator.check()

            self._log(
                f"Checked: {element_name}"
                if element_name
                else "Checked"
            )

            self._log("Completed check method")

        except Exception:
            self._log("Failed check method")
            raise

    # =========================
    # Uncheck
    # =========================

    async def uncheck(
        self,
        locator: Locator,
        element_name: str | None = None
    ) -> None:
        self._log("Started uncheck method")

        try:
            await locator.uncheck()

            self._log(
                f"Unchecked: {element_name}"
                if element_name
                else "Unchecked"
            )

            self._log("Completed uncheck method")

        except Exception:
            self._log("Failed uncheck method")
            raise

    # =========================
    # Press Keyboard Key
    # =========================

    async def press(
        self,
        locator: Locator,
        key: str,
        element_name: str | None = None
    ) -> None:
        self._log("Started press method")

        try:
            await locator.press(key)

            self._log(
                f"Pressed {key} on: {element_name}"
                if element_name
                else f"Pressed: {key}"
            )

            self._log("Completed press method")

        except Exception:
            self._log("Failed press method")
            raise

    # =========================
    # Hover
    # =========================

    async def hover(
        self,
        locator: Locator,
        element_name: str | None = None
    ) -> None:
        self._log("Started hover method")

        try:
            await locator.hover()

            self._log(
                f"Hovered: {element_name}"
                if element_name
                else "Hovered"
            )

            self._log("Completed hover method")

        except Exception:
            self._log("Failed hover method")
            raise

    # =========================
    # Toast / Snackbar Capture
    # =========================

    async def get_all_toast_messages(self) -> list[str]:
        self._log("Started get_all_toast_messages method")

        try:
            selectors = [
                '[role="alert"]',
                '[role="status"]',
                ".toast",
                ".toast-message",
                ".mat-snack-bar-container",
                ".toast-container",
                ".ng-trigger",
                ".toast-wrap",
                "[aria-live]",
                ".mat-simple-snackbar",
                ".md-toast",
                ".snackbar"
            ]

            messages = set()

            for selector in selectors:
                locator = self.page.locator(selector)
                count = await locator.count()

                for index in range(count):
                    text = (await locator.nth(index).inner_text()).strip()
                    text = " ".join(text.split())

                    if text:
                        messages.add(text)

            result = list(messages)

            self._log(
                f"Captured toast messages: {' | '.join(result)}"
                if result
                else "No toast messages found"
            )

            self._log("Completed get_all_toast_messages method")

            return result

        except Exception:
            self._log("Failed get_all_toast_messages method")
            raise

    async def verify_toast_messages(
        self,
        expected_messages: list[str]
    ) -> None:
        actual_messages = await self.get_all_toast_messages()

        for expected_message in expected_messages:
            match_found = any(
                expected_message.lower() in message.lower()
                for message in actual_messages
            )

            assert match_found, (
                f'Expected toast message "{expected_message}" '
                f"was not found"
            )

    # =========================
    # Validate Toast Message
    # =========================

    async def validate_toast_message(
        self,
        expected_text: str,
        page_name: str
    ) -> None:

        selectors = [
            '[role="alert"]',
            '[role="status"]',
            ".toast",
            ".toast-message",
            ".mat-snack-bar-container",
            ".toast-container",
            ".ng-trigger",
            ".toast-wrap",
            "[aria-live]",
            ".mat-simple-snackbar",
            ".md-toast",
            ".snackbar"
        ]

        end_time = datetime.now().timestamp() + 5
        matched = False

        while datetime.now().timestamp() < end_time:

            for selector in selectors:
                locator = self.page.locator(selector)
                count = await locator.count()

                for index in range(count):
                    message = (await locator.nth(index).inner_text()).strip()
                    message = " ".join(message.split())

                    if expected_text.lower() in message.lower():
                        matched = True
                        break

                if matched:
                    break

            if matched:
                break

            await self.page.wait_for_timeout(200)

        assert matched, (
            f'Expected toast message "{expected_text}" '
            f"on {page_name}"
        )

    # =========================
    # Wait For Element
    # =========================

    async def wait_for_visible(
        self,
        locator: Locator,
        element_name: str | None = None
    ) -> None:
        self._log("Started wait_for_visible method")

        try:
            await locator.wait_for(state="visible")

            self._log(
                f"Element visible: {element_name}"
                if element_name
                else "Element is visible"
            )

            self._log("Completed wait_for_visible method")

        except Exception:
            self._log("Failed wait_for_visible method")
            raise

    # =========================
    # Is Visible
    # =========================

    async def is_visible(
        self,
        locator: Locator,
        element_name: str | None = None
    ) -> bool:
        self._log("Started is_visible method")

        try:
            visible = await locator.is_visible()

            self._log(
                f"{element_name} visible: {visible}"
                if element_name
                else f"Element visible: {visible}"
            )

            self._log("Completed is_visible method")

            return visible

        except Exception:
            self._log("Failed is_visible method")
            raise