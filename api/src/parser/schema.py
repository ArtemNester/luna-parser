from pydantic import BaseModel


class ParserParams(BaseModel):
    browser_type: str
    domains: list[str]
