from sqlalchemy import ForeignKey, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.database.base import Base

class Insight(Base):
    __tablename__ = "insights"

    id: Mapped[int] = mapped_column(primary_key=True)
    analysis_id: Mapped[int] = mapped_column(ForeignKey("analyses.id"))
    summary: Mapped[str]
    recommendations: Mapped[str]
    confidence_score: Mapped[float | None]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
