from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import List

from models import Base

class Track(Base):
    __tablename__ = 'track'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    length_s: Mapped[int] = mapped_column(default=0)
    release_id: Mapped[int] = mapped_column(ForeignKey('release.id'), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(default=datetime.now())
    
    track_artists: Mapped[List["Track_Artist"]] = relationship("Track_Artist", back_populates='track')
    release: Mapped["Release"] = relationship("Release", back_populates='tracks')
