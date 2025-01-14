from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
)

from src.type import T


class Base(DeclarativeBase):
    id: T
    __name__: str

    __allow_unmapped = True

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()
