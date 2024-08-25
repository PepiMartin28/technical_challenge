from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class TrackCreateSchema(BaseModel):
    name: str
    length_s: Optional[int] = None
    release_id: int
    artists_id: List[int]
    

class TrackUpdateSchema(BaseModel):
    name: Optional[str] = None
    length_s: Optional[int] = None
    
        
class TrackSchema(BaseModel):
    id: int
    name: str
    length_s: Optional[int] = None
    active: bool
    release_id: int
    created_at: datetime 
    
    class Config:
        from_attributes=True
