from fastapi import Depends

from playwright.async_api import (
    BrowserType,
    Playwright,
)

from src.parser.browser.actions import (
    PageAction,
    VisitPageAction,
)
from src.parser.browser.actions.service import ActionService
from src.parser.browser.browser import BrowserFactory
from src.parser.service import ParserService


def get_browser_factory(playwright: Playwright, browser_type: str) -> BrowserType:
    return BrowserFactory.get_browser(playwright=playwright, browser_type=browser_type)


async def get_visit_action() -> VisitPageAction:
    return VisitPageAction()


async def get_page_action() -> PageAction:
    return PageAction()


async def get_action_service(
    page_action: PageAction = Depends(get_page_action),
    visit_action: VisitPageAction = Depends(VisitPageAction),
) -> ActionService:
    return ActionService(visit_action=visit_action, page_action=page_action)


async def get_parser_service(action_service: ActionService = Depends(get_action_service)):
    return ParserService(action_service=action_service)
