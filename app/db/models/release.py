from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import List

from app.db.models.base import BaseClass

class Release(BaseClass):
    __tablename__ = 'release'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    release_type_id: Mapped[int] = mapped_column(ForeignKey('release_type.id'), nullable=True)
    active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    
    tracks: Mapped[List["Track"]] = relationship("Track", back_populates='release')
    release_type: Mapped["Release_Type"] = relationship("Release_Type", back_populates='releases')
    release_countries: Mapped[List["Release_Country"]] = relationship("Release_Country", back_populates='release')
    
