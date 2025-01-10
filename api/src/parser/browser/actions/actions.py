from dataclasses import dataclass

from playwright.async_api import Page

from src.parser.browser.actions.base import (
    BasePageAction,
    BaseVisitAction,
)


@dataclass
class VisitPageAction(BaseVisitAction):
    async def visit(self, page: Page, domain: str) -> None:
        await page.goto(url=domain)


@dataclass
class PageAction(BasePageAction):
    async def click_button(self, page: Page, selector: str) -> None:
        await page.click(selector=selector)

    async def make_screenshot(self, page: Page, screenshot_path: str) -> None:
        await page.screenshot(path=screenshot_path)
