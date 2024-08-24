from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import List

from app.db.models.base import BaseClass

class Track(BaseClass):
    __tablename__ = 'track'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    length_s: Mapped[int] = mapped_column(default=0)
    release_id: Mapped[int] = mapped_column(ForeignKey('release.id'), nullable=True)
    active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    
    track_artists: Mapped[List["Track_Artist"]] = relationship("Track_Artist", back_populates='track')
    release: Mapped["Release"] = relationship("Release", back_populates='tracks')
    
    
