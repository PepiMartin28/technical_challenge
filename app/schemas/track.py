from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TrackSchema(BaseModel):
    id: Optional[int] = None
    name: str
    length_s: Optional[int] = None
    active: Optional[bool] = None
    release_id: int
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes=True
        
