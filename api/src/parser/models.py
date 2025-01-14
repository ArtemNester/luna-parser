import uuid
from datetime import datetime

from sqlalchemy import (
    DateTime,
    func,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.infrastructure.database import Base


class Content(Base):
    __tablename__ = "Content"

    session_uuid: Mapped[str] = mapped_column(
        String(36),
        default=lambda: str(uuid.uuid4()),
        unique=True,
        index=True,
        primary_key=True,
    )
    domain: Mapped[str] = mapped_column(nullable=False, index=True)
    ip: Mapped[str | None] = mapped_column(nullable=False, index=True)
    white_page_url: Mapped[str | None] = mapped_column(nullable=True)
    black_page_url: Mapped[str | None] = mapped_column(nullable=True)
    text_ad: Mapped[str | None] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
