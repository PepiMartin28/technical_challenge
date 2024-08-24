from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TrackCreateSchema(BaseModel):
    name: str
    length_s: Optional[int] = None
    release_id: int
    

class TrackUpdateSchema(BaseModel):
    name: Optional[str] = None
    length_s: Optional[int] = None
    release_id: Optional[int] = None
    
        
class TrackSchema(BaseModel):
    id: int
    name: str
    length_s: Optional[int] = None
    active: bool
    release_id: Optional[int] = None
    created_at: datetime 
    
    class Config:
        from_attributes=True
