from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import List

from app.db.models.base import BaseClass

class Release_Type(BaseClass):
    __tablename__ = 'release_type'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    
    releases: Mapped[List["Release"]] = relationship("Release", back_populates='release_type')
