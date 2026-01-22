from sqlalchemy import Column, String, DateTime, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from backend.app.database.base import Base

class Process(Base):
    __tablename__ = "processes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None]
    analysis_result = Column(Text, nullable=True)
    status = Column(String, default="PENDING")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )