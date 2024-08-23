from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import List

from app.db.models.base import BaseClass

class Artist(BaseClass):
    __tablename__ = 'artist'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now())

    track_artists: Mapped[List["Track_Artist"]] = relationship("Track_Artist", back_populates='artist')
