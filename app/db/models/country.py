from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import List

from app.db.models.base import BaseClass

class Country(BaseClass):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    
    release_countries: Mapped[List["Release_Country"]] = relationship("Release_Country", back_populates='country')
