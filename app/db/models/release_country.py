from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

from models import Base

class Release_Country(Base):
    __tablename__ = 'release_country'

    id: Mapped[int] = mapped_column(primary_key=True)
    release_id: Mapped[int] = mapped_column(ForeignKey('release.id'))
    country_id: Mapped[int] = mapped_column(ForeignKey('country.id'), nullable=True)
    release_year: Mapped[int] = mapped_column(nullable=True)
    created_at: Mapped[DateTime] = mapped_column(default=lambda: datetime.now())
    
    release: Mapped["Release"] = relationship("Release", back_populates='release_countries')
    country: Mapped["Country"] = relationship("Country", back_populates='release_countries')
