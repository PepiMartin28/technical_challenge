from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import List

from models import Base

class Release(Base):
    __tablename__ = 'release'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    release_type_id: Mapped[int] = mapped_column(ForeignKey('release_type.id'), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(default=datetime.now())
    
    tracks: Mapped[List["Track"]] = relationship("Track", back_populates='release')
    release_type: Mapped["Release_Type"] = relationship("Release_Type", back_populates='releases')
    release_countries: Mapped[List["Release_Country"]] = relationship("Release_Country", back_populates='release')
