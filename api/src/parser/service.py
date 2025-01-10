from dataclasses import dataclass

from playwright.async_api import async_playwright

from src.parser.browser.actions import ActionService
from src.parser.schema import ParserParams


@dataclass
class ParserService:
    action_service: ActionService

    async def start_parsing(self, body: ParserParams) -> None:
        from src.dependency import get_browser_factory

        async with async_playwright() as p:
            browser_fct = get_browser_factory(playwright=p, browser_type=body.browser_type)
            browser = await browser_fct.launch()
            page = await browser.new_page()

            for domain in body.domains:
                await self.action_service.visit(page=page, domain=domain)
                await self.action_service.make_screenshot(page=page, screenshot_path="image.jpg")
