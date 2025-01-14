from dataclasses import dataclass

from fastapi import (
    HTTPException,
    status,
)

from playwright.async_api import async_playwright

from src.parser.browser.actions import ActionService
from src.parser.exceptions import SessionUUIDNotFound
from src.parser.repository import ParserRepository
from src.parser.schema import (
    ParserContent,
    ParserParams,
)
from src.settings import settings


@dataclass
class ParserService:
    action_service: ActionService
    parser_repository: ParserRepository

    async def start_parsing(self, body: ParserParams) -> None:
        from src.dependency import get_browser_factory

        async with async_playwright() as p:
            browser_fct = get_browser_factory(playwright=p, browser_type=body.browser_type)
            browser = await browser_fct.launch(headless=settings.HEADLESS_TOGGLE)
            page = await browser.new_page()

            for domain in body.domains:
                try:
                    await self.action_service.visit(page=page, domain=domain)
                    await self.action_service.make_screenshot(page=page, screenshot_path=settings.IMAGE_PATH)
                except ValueError as e:
                    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    async def _save_parser_content(self, body: ParserContent) -> str:
        session_uuid = await self.parser_repository.save_parser_content(body=body)
        return session_uuid

    async def get_parser_content_by_session_uuid(self, session_uuid: str) -> ParserContent:
        try:
            content = await self.parser_repository.get_parser_content_by_session_uuid(session_uuid=session_uuid)
            return ParserContent.model_validate(content)
        except SessionUUIDNotFound as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

    async def get_parser_contents(self) -> list[ParserContent]:
        contents = await self.parser_repository.get_parser_contents()
        contents_schema = [ParserContent.model_validate(content) for content in contents]
        return contents_schema
