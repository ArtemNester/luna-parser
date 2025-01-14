from pydantic import (
    BaseModel,
    field_validator,
)


class ParserParams(BaseModel):
    browser_type: str
    domains: list[str]


class ParserContent(BaseModel):
    session_uuid: str
    domain: str
    ip: str | None = None
    white_page_url: str | None = None
    black_page_url: str | None = None
    text_ad: str | None = None
    status: str

    @field_validator("session_uuid", mode="before")
    @classmethod
    def validate_session_uuid(cls, value: str) -> str:
        if len(value) >= 36:
            raise ValueError(f"{value} len must not exceed 36 char")
        return value
