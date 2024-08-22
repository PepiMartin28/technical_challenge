from sqlalchemy import DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import List

from models import Base

class Release_Type(Base):
    __tablename__ = 'release_type'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(default=lambda: datetime.now())
    
    releases: Mapped[List["Release"]] = relationship("Release", back_populates='release_type')
