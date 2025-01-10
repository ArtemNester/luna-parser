from typing import Protocol

from playwright.async_api import Page


class BasePageAction(Protocol):
    async def click_button(self, page: Page, selector: str) -> None:
        raise NotImplementedError()

    async def make_screenshot(self, page: Page, screenshot_path: str) -> None:
        raise NotImplementedError()


class BaseVisitAction(Protocol):
    async def visit(self, page: Page, domain: str) -> None:
        raise NotImplementedError()
