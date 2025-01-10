from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)

from starlette.responses import JSONResponse

from src.dependency import get_parser_service
from src.parser.schema import ParserParams
from src.parser.service import ParserService


router = APIRouter(prefix="/api/v1/parser", tags=["parser"])


@router.post("/start")
async def start_parsing(body: ParserParams, parser_service: Annotated[ParserService, Depends(get_parser_service)]):
    await parser_service.start_parsing(body=body)
    return JSONResponse(content="parser started")
