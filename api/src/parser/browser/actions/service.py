from dataclasses import dataclass

from playwright.async_api import Page

from src.parser.browser.actions import (
    PageAction,
    VisitPageAction,
)


@dataclass
class ActionService:
    visit_action: VisitPageAction
    page_action: PageAction

    async def visit(self, page: Page, domain: str) -> None:
        await self.visit_action.visit(page=page, domain=domain)

    async def click_button(self, page: Page, selector: str) -> None:
        await self.page_action.click_button(page=page, selector=selector)

    async def make_screenshot(self, page: Page, screenshot_path: str) -> None:
        await self.page_action.make_screenshot(page=page, screenshot_path=screenshot_path)
