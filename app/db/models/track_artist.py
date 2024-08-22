from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

from models import Base

class Track_Artist(Base):
    __tablename__ = 'track_artist'

    id: Mapped[int] = mapped_column(primary_key=True)
    track_id: Mapped[int] = mapped_column(ForeignKey('track.id'))
    artist_id: Mapped[int] = mapped_column(ForeignKey('artist.id'))
    created_at: Mapped[DateTime] = mapped_column(default=lambda: datetime.now())
    
    track: Mapped["Track"] = relationship("Track", back_populates='track_artists')
    artist: Mapped["Artist"] = relationship("Artist", back_populates='track_artists')
