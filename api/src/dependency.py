from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from playwright.async_api import (
    BrowserType,
    Playwright,
)

from src.infrastructure.database import get_db_session
from src.parser.browser.actions import (
    PageAction,
    VisitPageAction,
)
from src.parser.browser.actions.service import ActionService
from src.parser.browser.browser import BrowserFactory
from src.parser.repository import ParserRepository
from src.parser.service import ParserService


def get_browser_factory(playwright: Playwright, browser_type: str) -> BrowserType:
    return BrowserFactory.get_browser(playwright=playwright, browser_type=browser_type)


async def get_visit_action() -> VisitPageAction:
    return VisitPageAction()


async def get_page_action() -> PageAction:
    return PageAction()


async def get_action_service(
    page_action: PageAction = Depends(get_page_action),
    visit_action: VisitPageAction = Depends(get_visit_action),
) -> ActionService:
    return ActionService(visit_action=visit_action, page_action=page_action)


async def get_parser_repository(db_session: AsyncSession = Depends(get_db_session)) -> ParserRepository:
    return ParserRepository(db_session=db_session)


async def get_parser_service(
    action_service: ActionService = Depends(get_action_service),
    parser_repository: ParserRepository = Depends(get_parser_repository),
) -> ParserService:
    return ParserService(action_service=action_service, parser_repository=parser_repository)
