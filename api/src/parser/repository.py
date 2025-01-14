import logging
from dataclasses import dataclass
from typing import Sequence

from sqlalchemy import (
    insert,
    select,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.parser.exceptions import SessionUUIDNotFound
from src.parser.models import Content
from src.parser.schema import ParserContent


logger = logging.getLogger(__name__)


@dataclass
class ParserRepository:
    db_session: AsyncSession

    async def save_parser_content(self, body: ParserContent) -> str:
        query = insert(Content).values(**body.dict(exclude_none=True)).returning(Content.session_uuid)
        try:
            async with self.db_session as session:
                session_uuid = (await session.execute(query)).scalar_one()
                await session.commit()
                return session_uuid
        except IntegrityError as e:
            logger.error("DB_DEAD_Error", exc_info=True)
            raise ValueError("Failed to save parser content") from e

    async def get_parser_content_by_session_uuid(self, session_uuid: str) -> Content:
        query = select(Content).where(Content.session_uuid == session_uuid)
        async with self.db_session as session:
            content = (await session.execute(query)).scalar_one_or_none()
            if not content:
                raise SessionUUIDNotFound
            return content

    async def get_parser_contents(self) -> Sequence[Content]:
        query = select(Content)

        async with self.db_session as session:
            contents = (await session.execute(query)).scalars().all()
            return contents
