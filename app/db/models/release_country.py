from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

from app.db.models.base import BaseClass

class Release_Country(BaseClass):
    __tablename__ = 'release_country'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    release_id: Mapped[int] = mapped_column(ForeignKey('release.id'))
    country_id: Mapped[int] = mapped_column(ForeignKey('country.id'), nullable=True)
    release_year: Mapped[int] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    
    release: Mapped["Release"] = relationship("Release", back_populates='release_countries')
    country: Mapped["Country"] = relationship("Country", back_populates='release_countries')
    
