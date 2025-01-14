from typing import (
    Annotated,
    TypeVar,
)

from pydantic import BeforeValidator


T = TypeVar("T")


UUIDString = Annotated[str, BeforeValidator]
