from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)

from starlette.responses import JSONResponse

from src.dependency import get_parser_service
from src.parser.schema import (
    ParserContent,
    ParserParams,
)
from src.parser.service import ParserService


router = APIRouter(prefix="/api/v1/parser", tags=["parser"])


@router.post("/start", description="Start worker parser processes")
async def start_parsing(body: ParserParams, parser_service: Annotated[ParserService, Depends(get_parser_service)]):
    await parser_service.start_parsing(body=body)
    return JSONResponse(content="parser started")


@router.get("/content/{session_uuid}", response_model=ParserContent, description="Get content to session_uuid")
async def get_parser_content(session_uuid: str, parser_service: Annotated[ParserService, Depends(get_parser_service)]):
    return await parser_service.get_parser_content_by_session_uuid(session_uuid=session_uuid)
