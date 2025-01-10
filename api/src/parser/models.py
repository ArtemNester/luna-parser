from datetime import datetime
from typing import Optional

from sqlalchemy import (
    DateTime,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.infrastructure.database import Base


class Content(Base):
    __tablename__ = "Content"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    domain: Mapped[str] = mapped_column(nullable=False, index=True)
    ip: Mapped[Optional[str]] = mapped_column(nullable=False, index=True)
    white_page_url: Mapped[Optional[str]] = mapped_column(nullable=True)
    black_page_url: Mapped[Optional[str]] = mapped_column(nullable=True)
    text: Mapped[Optional[str]] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
