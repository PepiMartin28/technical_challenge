from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ReleaseCreateSchema(BaseModel):
    name: str
    release_type_id: int
        
class ReleaseUpdateSchema(BaseModel):
    name: Optional[str] = None
    release_type_id: Optional[int] = None
        
class ReleaseSchema(BaseModel):
    id: int
    name: str
    active: bool
    release_type_id: int
    created_at: datetime
    
    class Config:
        from_attributes=True
        
