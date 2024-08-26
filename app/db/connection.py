from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

session = Session(bind=engine)



