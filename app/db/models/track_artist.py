from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

from app.db.models.base import BaseClass

class Track_Artist(BaseClass):
    __tablename__ = 'track_artist'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    track_id: Mapped[int] = mapped_column(ForeignKey('track.id'))
    artist_id: Mapped[int] = mapped_column(ForeignKey('artist.id'))
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    
    track: Mapped["Track"] = relationship("Track", back_populates='track_artists')
    artist: Mapped["Artist"] = relationship("Artist", back_populates='track_artists')
    
